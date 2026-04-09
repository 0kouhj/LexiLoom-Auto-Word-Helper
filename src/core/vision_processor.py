# src/core/vision_processor.py
import os
import re
import numpy as np
from PIL import Image
import cv2

from rapidocr_onnxruntime import RapidOCR

from src.utils.path_utils import get_debug_dir
from src.utils.logger import logger
from src.models.error_codes import ErrorCode
from src.utils.exceptions import VisionError
from src.models.config_schema import ROIConfig


class VisionProcessor:
    def __init__(self, use_gpu=True, max_width=800, enhance=True):
        """
        :param use_gpu: 是否启用 GPU 加速
        :param max_width: OCR 输入图像最大宽度
        :param enhance: 是否进行二值化增强
        """
        logger.info("👁️ 正在初始化 RapidOCR 视觉引擎...")

        try:
            self.ocr = RapidOCR(provider="CUDAExecutionProvider" if use_gpu else "CPUExecutionProvider")
            logger.info(f"✅ RapidOCR 引擎就绪 (GPU={use_gpu})")
        except Exception as e:
            logger.error(f"OCR 引擎启动失败: {e}")
            raise VisionError(ErrorCode.OCR_INIT_ERROR, detail=str(e))

        self.max_width = max_width
        self.enhance = enhance

    def analyze(self, full_img: Image.Image, roi: ROIConfig) -> dict:
        """
        优化版 analyze：单次 OCR + 拼接 + 自动缩放 + 二值化增强
        """
        q_data = {}
        roi_dict = roi.model_dump()
        order = ["topic", "A", "B", "C", "D"]

        roi_imgs = []
        valid_keys = []

        # =========================
        # 1️⃣ 裁剪 ROI 并按顺序
        # =========================
        for key in order:
            coords = roi_dict.get(key)
            if not coords or len(coords) < 4:
                logger.warning(f"跳过未定义的区域: {key}")
                continue
            try:
                roi_img = full_img.crop((coords[0], coords[1], coords[2], coords[3]))
                roi_imgs.append(roi_img)
                valid_keys.append(key)
            except Exception as e:
                logger.error(f"裁剪区域 {key} 失败: {e}")

        if not roi_imgs:
            return q_data

        # =========================
        # 2️⃣ 拼接图像 (纵向 + 间隔)
        # =========================
        gap = 20
        widths = [img.width for img in roi_imgs]
        heights = [img.height for img in roi_imgs]

        total_height = sum(heights) + gap * (len(roi_imgs) - 1)
        max_width = max(widths)
        merged = Image.new("RGB", (max_width, total_height), (255, 255, 255))

        y_offset = 0
        for img in roi_imgs:
            merged.paste(img, (0, y_offset))
            y_offset += img.height + gap

        # =========================
        # 3️⃣ 缩放到 max_width
        # =========================
        if merged.width > self.max_width:
            scale = self.max_width / merged.width
            new_h = int(merged.height * scale)
            merged = merged.resize((self.max_width, new_h), Image.LANCZOS)

        # =========================
        # 4️⃣ 二值化增强 (可选)
        # =========================
        ocr_img = np.array(merged)
        if self.enhance:
            gray = cv2.cvtColor(ocr_img, cv2.COLOR_RGB2GRAY)
            _, bin_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            ocr_img = bin_img

        # =========================
        # 5️⃣ 单次 OCR
        # =========================
        try:
            result, _ = self.ocr(
                ocr_img,
                use_det=True,    # 必须检测文本块
                use_cls=False
            )
            texts = []
            if result:
                for item in result:
                    if len(item) >= 2:
                        texts.append(item[1].strip())
        except Exception as e:
            logger.error(f"OCR 失败: {e}")
            raise VisionError(ErrorCode.OCR_RUN_ERROR, detail=str(e))

        # =========================
        # 6️⃣ 按顺序还原 topic + A/B/C/D
        # =========================
        for i, key in enumerate(valid_keys):
            text = texts[i] if i < len(texts) else ""
            if key in "ABCD":
                content = re.sub(rf'^[A-D0@\s\._]+', '', text, flags=re.I)
                text = f"{key}: {content}"
            q_data[key] = text
            logger.debug(f"🔍 ROI[{key}] => {text}")

        # =========================
        # 7️⃣ 保存 Debug 图（可选）
        # =========================
        try:
            debug_save_path = os.path.join(get_debug_dir(), "merged_debug.png")
            merged.save(debug_save_path)
        except:
            pass

        return q_data