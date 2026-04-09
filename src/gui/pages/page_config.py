import json
import os
import uuid
from PySide6.QtGui import QPixmap, QImage, QColor, QPainter, QPen
from PySide6.QtWidgets import QInputDialog, QMessageBox

from src.gui.widgets.calibration_dialog import CalibrationDialog
from src.models.error_codes import ErrorCode 
from src.utils.logger import LogLevel


class PageConfig:

    # ================= 初始化 =================
    def init_page_config(self):
        self.config_path = "devices.json"
        self.devices_data = self._load_all_configs_from_file()

        self.calibrate_steps = ["topic", "A", "B", "C", "D"]
        self.current_step_idx = -1
        self.temp_roi = {}
        self.temp_tap = {}
        self.p1_cache = None

        self.active_config = None
        self.current_config_id = None  # ✅ 关键

        self._refresh_model_list_ui()
        self._refresh_ui_combo()

    # ================= 预览 =================
    def on_btn_refresh_clicked(self):
        self.append_log(LogLevel.INFO,"正在同步手机画面并准备弹出预览...")

        try:            
            pil_img = self.dm.take_screenshot() 
            q_img = self._pil_to_qimage(pil_img)
            pixmap = QPixmap.fromImage(q_img)

            # 2. 如果当前有选中的配置，就在预览图上画出物理框
            if hasattr(self, 'active_config') and self.active_config:
                self._draw_roi_on_pixmap(pixmap, self.active_config)
            else:
                self.append_log(LogLevel.WARN,"当前未加载任何配置，显示原始截图")

            # 3. 更新主界面上的小预览图
            self.ui.label_canvas.setPixmap(pixmap)

            # 4. 弹出大窗口 (确保顶部已 from src.gui.widgets.calibration_dialog import CalibrationDialog)
            self.preview_dial = CalibrationDialog(pixmap, self)
            self.preview_dial.setWindowTitle("配置预览 - 检查识别区域")
            # 设置为非模态，这样你可以一边看大图一边在主界面操作
            self.preview_dial.show()
            
            self.append_log(LogLevel.INFO,"预览窗口已成功弹出")

        except Exception as e:
            self.append_log(LogLevel.ERRO,"预览失败",error = e)
            self.show_error_dialog(ErrorCode.PREVIEW_FAILED,str(e))

    def _draw_roi_on_pixmap(self, pixmap, config):
        painter = QPainter(pixmap)
        colors = {
            "topic": QColor(255, 87, 34, 200),
            "A": QColor(76, 175, 80, 200),
            "B": QColor(33, 150, 243, 200),
            "C": QColor(255, 193, 7, 200),
            "D": QColor(156, 39, 176, 200)
        }

        for key, roi in config.get("roi", {}).items():
            if len(roi) == 4:
                x1, y1, x2, y2 = roi
                color = colors.get(key, QColor(255, 255, 255, 200))
                painter.setPen(QPen(color, 4))
                painter.drawRect(x1, y1, x2-x1, y2-y1)

        painter.end()

    # ================= 创建标定 =================
    def on_btn_create_clicked(self):
        try:
            self.append_log(LogLevel.INFO,"启动标定")

            pil_img = self.dm.take_screenshot()
            self.raw_w, self.raw_h = pil_img.size

            pixmap = QPixmap.fromImage(self._pil_to_qimage(pil_img))

            if hasattr(self, 'dial') and self.dial:
                self.dial.close()

            self.dial = CalibrationDialog(pixmap, self)
            self.dial.canvas.clicked_pos.connect(self._handle_calibration_click)

            # ✅ 重置状态
            self.current_config_id = None
            self.current_step_idx = 0
            self.temp_roi.clear()
            self.temp_tap.clear()
            self.p1_cache = None

            self.dial.show()

        except Exception as e:
            self.show_error_dialog(ErrorCode.ADB_CMD_FAILED, str(e))

    # ================= 标定逻辑 =================
    def _handle_calibration_click(self, lx, ly):
        if self.current_step_idx == -1:
            return

        rx, ry = self.dial.get_real_coords(lx, ly)
        step_key = self.calibrate_steps[self.current_step_idx]

        if self.p1_cache is None:
            self.p1_cache = (rx, ry, lx, ly)
            self.dial.canvas.set_overlay_rect(lx-2, ly-2, 4, 4, QColor(255, 255, 255, 200))
            self.append_log(LogLevel.INFO,f"[{step_key}] 起点已记录，请点击右下角终点")
            return

        p1_rx, p1_ry, p1_lx, p1_ly = self.p1_cache

        x1, y1 = min(p1_rx, rx), min(p1_ry, ry)
        x2, y2 = max(p1_rx, rx), max(p1_ry, ry)

        self.temp_roi[step_key] = [x1, y1, x2, y2]

        if step_key != "topic":
            self.temp_tap[step_key] = [int((x1 + x2) / 2), int((y1 + y2) / 2)]


        self._sync_roi_to_ui(step_key, [x1, y1, x2, y2])
        # 画半透明绿色框反馈
        self.dial.canvas.set_overlay_rect(
            min(p1_lx, lx), min(p1_ly, ly),
            abs(p1_lx - lx), abs(p1_ly - ly),
            QColor(76, 175, 80, 80)
        )

        self.current_step_idx += 1
        self.p1_cache = None

        if self.current_step_idx < len(self.calibrate_steps):
            self.append_log(LogLevel.INFO,f"👉 下一步：请框选 [{self.calibrate_steps[self.current_step_idx]}]")
        else:
            self.append_log(LogLevel.INFO,"标定完成，自动唤起保存流程...")
            self.current_step_idx = -1
            self.dial.close()
            self._finalize_new_config()

    # ================= 新建配置 =================
    def _finalize_new_config(self):
        name, ok = QInputDialog.getText(self, "新建配置", "请输入设备标识:")
        if not ok or not name.strip():
            return

        try:
            cfg_id = str(uuid.uuid4())[:8]

            self.devices_data[cfg_id] = {
                "name": f"{name} ({self.raw_w}x{self.raw_h})",
                "ai_model": self.ui.combo_ai_model.currentText(),
                "roi": self.temp_roi.copy(),
                "tap": self.temp_tap.copy()
            }

            self._save_to_file()
            self._refresh_ui_combo()

            self.current_config_id = cfg_id
            self.active_config = self.devices_data[cfg_id]

            self.append_log(LogLevel.INFO,"新配置已创建")

        except Exception as e:
            self.show_error_dialog(ErrorCode.CONFIG_SAVE_FAILED, str(e))

    # ================= 保存（仅更新） =================
    def on_btn_save_config_clicked(self):
        if not self.current_config_id:
            self.append_log(LogLevel.WARN,"未加载配置")
            return

        try:
            cfg = self.devices_data[self.current_config_id]

            updated_roi = {}
            for step in self.calibrate_steps:
                try:
                    s_low = step.lower()
                    x1 = int(getattr(self.ui, f"edit_{s_low}_x1").text())
                    y1 = int(getattr(self.ui, f"edit_{s_low}_y1").text())
                    x2 = int(getattr(self.ui, f"edit_{s_low}_x2").text())
                    y2 = int(getattr(self.ui, f"edit_{s_low}_y2").text())
                    updated_roi[step] = [x1, y1, x2, y2]
                except:
                    continue

            updated_tap = {
                k: [(v[0]+v[2])//2, (v[1]+v[3])//2]
                for k, v in updated_roi.items() if k != "topic"
            }

            cfg["roi"] = updated_roi
            cfg["tap"] = updated_tap
            cfg["ai_model"] = self.ui.combo_ai_model.currentText()

            self._save_to_file()
            self.append_log(LogLevel.INFO,"配置已更新")

        except Exception as e:
            self.show_error_dialog(ErrorCode.CONFIG_SAVE_FAILED, str(e))

    # ================= 加载 =================
    def on_btn_load_clicked(self):
        cfg_id = self.ui.combo_configs.currentData()
        if not cfg_id or cfg_id not in self.devices_data:
            self.append_log(LogLevel.WARN,"无效的配置 ID")
            return

        self.current_config_id = cfg_id
        self.active_config = self.devices_data[cfg_id]

        # --- 🟢 新增：同步 AI 模型到下拉框 ---
        saved_model = self.active_config.get("ai_model", "")
        if saved_model:
            # 在下拉框中寻找保存的模型名称
            index = self.ui.combo_ai_model.findText(saved_model)
            if index >= 0:
                self.ui.combo_ai_model.setCurrentIndex(index)
                self.append_log(LogLevel.INFO,f"已同步 AI 模型: {saved_model}")
            else:
                self.append_log(LogLevel.WARN,f"配置要求的模型 '{saved_model}' 当前不可用")
        # ------------------------------------

        for step in self.calibrate_steps:
            self._sync_roi_to_ui(step, ["", "", "", ""])

        for k, roi in self.active_config.get("roi", {}).items():
            self._sync_roi_to_ui(k, roi)

        self.append_log(LogLevel.INFO,"配置已加载")

    # ================= 删除 =================
    def on_btn_delete_clicked(self):
        cfg_id = self.ui.combo_configs.currentData()
        if not cfg_id:
            return

        reply = QMessageBox.question(self, "确认删除", f"是否彻底删除此配置？\n此操作不可逆。", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                del self.devices_data[cfg_id]
                self._save_to_file()
                self._refresh_ui_combo()
                self.append_log(LogLevel.INFO,"配置已删除")
                self.active_config = None
            except Exception as e:
                self.show_error_dialog("DELETE_FAILED", str(e))

    # ================= 工具 =================
    def _sync_roi_to_ui(self, key, roi):
        try:
            getattr(self.ui, f"edit_{key.lower()}_x1").setText(str(roi[0]))
            getattr(self.ui, f"edit_{key.lower()}_y1").setText(str(roi[1]))
            getattr(self.ui, f"edit_{key.lower()}_x2").setText(str(roi[2]))
            getattr(self.ui, f"edit_{key.lower()}_y2").setText(str(roi[3]))
        except AttributeError:
            pass

    def _refresh_ui_combo(self):
        self.ui.combo_configs.clear()
        for cid, cfg in self.devices_data.items():
            self.ui.combo_configs.addItem(cfg["name"], cid)

    def _refresh_model_list_ui(self):
        if hasattr(self, 'all_ai_models'):
            self.ui.combo_ai_model.clear()
            self.ui.combo_ai_model.addItems(self.all_ai_models)
            if self.all_ai_models:
                self.ui.combo_ai_model.setCurrentIndex(0)

    def _save_to_file(self):
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.devices_data, f, indent=4, ensure_ascii=False)

    def _load_all_configs_from_file(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _pil_to_qimage(self, pil_img):
        if pil_img.mode != "RGB":
            pil_img = pil_img.convert("RGB")
        return QImage(pil_img.tobytes("raw","RGB"), pil_img.width, pil_img.height, QImage.Format_RGB888)