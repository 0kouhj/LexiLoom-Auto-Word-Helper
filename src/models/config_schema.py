# src/models/config_schema.py
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Literal

class SystemConfig(BaseModel):
    """程序全局通用配置"""
    # UI 相关
    theme: Literal["light", "dark", "auto"] = Field(default="dark", description="主题模式")
    language: str = Field(default="zh_CN", description="界面语言")
    window_opacity: float = Field(default=1.0, ge=0.1, le=1.0, description="窗口透明度")
    
    # 运行策略相关
    loop_delay: float = Field(default=0.5, ge=0.1, description="答题循环基础延时(秒)")
    random_delay_range: float = Field(default=0.1, description="随机抖动延时上限(秒)")
    auto_start_adb: bool = Field(default=True, description="启动程序时是否自动拉起ADB")
    
    # 调试相关
    save_debug_images: bool = Field(default=True, description="是否保存ROI裁剪图用于调试")
    log_level: str = Field(default="INFO", description="日志等级: DEBUG, INFO, WARNING, ERROR")

    theme_color: str = Field(default="#4CAF50", description="主界面主题色")
    roi_color: str = Field(default="#55FF5736", description="标定框颜色 (带透明度的Hex: #AARRGGBB)")
    
    # 也可以为不同步骤定义颜色字典
    step_colors: Dict[str, str] = Field(default={
        "topic": "#50FF5722", # 橙色半透明
        "A": "#504CAF50",     # 绿色半透明
        "B": "#502196F3",     # 蓝色半透明
        "C": "#50FFC107",     # 黄色半透明
        "D": "#509C27B0"      # 紫色半透明
    })
    
class ROIConfig(BaseModel):
    """区域坐标模型"""
    topic: List[int] = Field(default_factory=list)
    A: List[int] = Field(default_factory=list)
    B: List[int] = Field(default_factory=list)
    C: List[int] = Field(default_factory=list)
    D: List[int] = Field(default_factory=list)

class DeviceConfig(BaseModel):
    """单个设备的完整数据模型"""
    id: str
    name: str = "Default Device"
    resolution: str = "1080x1920"
    roi: ROIConfig = Field(default_factory=ROIConfig)
    tap: Dict[str, List[int]] = Field(default_factory=dict)

class LLMConfig(BaseModel):
    """LLM 核心参数配置"""
    mode: str = Field(default="local", description="local 或 cloud")
    model_name: str = Field(default="qwen2.5:7b")
    
    # 云端专用
    api_key: str = Field(default="")
    api_url: str = Field(default="http://localhost:11434/api/generate")
    
    # 策略参数
    temperature: float = Field(default=0.0, ge=0.0, le=1.0)
    timeout: int = Field(default=10, description="回答时长限制(秒)")
    max_tokens: int = Field(default=10)
    
    # 提示词工程
    prompt_template: str = Field(
        default="""You are an English Exam Expert. 
        Task: Find the BEST synonym or translation for the Topic.
        ---
        Question:
        {context}
        ---
        Rules:
        1. ONLY output the single letter (A, B, C, or D).
        2. If multiple options are close, choose the most professional and precise one.
        3. Ignore OCR noise like '@', '_', or '.'.
        Answer: """,
        description="支持 {context} 占位符的模板"
    )


class AppConfig(BaseModel):
    """全局配置总入口"""
    system: SystemConfig = Field(default_factory=SystemConfig)  # 新增系统配置项
    llm: LLMConfig = Field(default_factory=LLMConfig)
    devices: List[DeviceConfig] = []
    last_device_id: Optional[str] = None