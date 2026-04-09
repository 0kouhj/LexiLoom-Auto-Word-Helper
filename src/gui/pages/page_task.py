# src/gui/pages/page_task.py
from src.core.run_thread import AutoRunThread
from src.utils.logger import LogLevel
class PageTask:
    
    # ================= 初始化 =================
    def init_page_task(self):
        """主窗口 __init__ 中调用此方法进行初始化"""
        # 初始化按钮状态：未运行状态下，启动可用，停止禁用
        if hasattr(self.ui, 'btn_start_task'):
            self.ui.btn_start_task.setEnabled(True)
        if hasattr(self.ui, 'btn_stop_task'):
            self.ui.btn_stop_task.setEnabled(False)
            
        self.run_thread = None  # 用于保存当前运行的线程实例

    # ================= 按钮交互控制 =================
    def on_btn_start_task_clicked(self):
        """点击【开始运行】按钮"""
        self.append_task_log(LogLevel.INFO,"-----------------------")
        # 1. 检查配置是否已加载
        if not getattr(self, 'active_config', None):
            self.append_task_log(LogLevel.ERRO,"无法启动：请先在【配置管理】页面加载一个设备配置！")
            return

        self.append_task_log(LogLevel.INFO,"准备启动自动化任务...")

        # 2. 切换 UI 按钮状态，防止用户重复点击开启多个线程
        self.ui.btn_start_task.setEnabled(False)
        self.ui.btn_stop_task.setEnabled(True)

        # 3. 实例化我们封装好的核心运行线程
        self.run_thread = AutoRunThread(self.dm, self.active_config)
        
        # 4. 绑定线程的信号到 UI 的槽函数
        self.run_thread.log_signal.connect(self.append_task_log)
        self.run_thread.finished_signal.connect(self._on_task_finished)
        
        # 5. 正式启动线程
        self.run_thread.start()

    def on_btn_stop_task_clicked(self):
        """点击【停止运行】按钮"""
        if self.run_thread and self.run_thread.isRunning():
            self.append_task_log(LogLevel.WARN,"正在发送停止指令，请等待当前循环结束...")
            # 调用线程安全的停止方法
            self.run_thread.stop()
            # 禁用停止按钮，防止狂点报错
            self.ui.btn_stop_task.setEnabled(False) 

    # ================= 回调与辅助 =================
    def _on_task_finished(self):
        """线程运行结束后的回调（无论是正常结束、报错崩溃还是手动停止，都会走这里）"""
        # 恢复初始状态的按钮
        if hasattr(self.ui, 'btn_start_task'):
            self.ui.btn_start_task.setEnabled(True)
        if hasattr(self.ui, 'btn_stop_task'):
            self.ui.btn_stop_task.setEnabled(False)
            
        self.run_thread = None
        self.append_task_log(LogLevel.INFO,"线程已彻底释放，准备就绪。")

    def append_task_log(self, level: LogLevel, msg: str, error: Exception = None):
        self.append_log(level, msg, error)