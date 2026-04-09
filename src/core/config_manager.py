# src/core/config_manager.py
import json
import os
from src.utils.path_utils import get_config_path
from src.models.config_schema import AppConfig, DeviceConfig
from src.models.error_codes import ErrorCode
from src.utils.exceptions import ConfigError
from src.utils.logger import logger

class ConfigManager:
    def __init__(self):
        self.path = get_config_path()
        self.config_data: AppConfig = self._load()
        logger.info(f"配置管理器就绪，已加载 {len(self.config_data.devices)} 个设备配置")

    def _load(self) -> AppConfig:
        """从磁盘加载配置，并进行 Pydantic 校验"""
        # 1. 检查文件是否存在
        if not os.path.exists(self.path):
            logger.warning(f"未找到配置文件，将创建默认配置: {self.path}")
            return AppConfig()
        
        # 2. 检查文件是否为空 (资深建议：增加文件大小判断)
        if os.path.getsize(self.path) == 0:
            logger.warning("检测到配置文件为空，正在初始化默认结构...")
            return AppConfig()

        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
                return AppConfig(**raw_data)
        except json.JSONDecodeError as e:
            # 如果文件不是空的但格式乱了，报 1001
            logger.error(f"配置文件格式损坏: {e}")
            raise ConfigError(ErrorCode.CONFIG_LOAD_FAILED, detail="JSON 语法错误，请手动检查或删除 configs.json")
        except Exception as e:
            logger.error(f"加载配置时发生未知错误: {e}")
            raise ConfigError(ErrorCode.UNKNOWN_ERROR, detail=str(e))

    def save(self):
        """将内存中的 AppConfig 对象持久化到磁盘"""
        try:
            json_str = self.config_data.model_dump_json(indent=2)
            with open(self.path, 'w', encoding='utf-8') as f:
                f.write(json_str)
            logger.info("配置文件保存成功")
        except Exception as e:
            logger.error(f"写入配置文件失败: {e}")
            raise ConfigError(ErrorCode.CONFIG_SAVE_FAILED, detail=str(e))

    def add_or_update_device(self, device: DeviceConfig):
        """添加新设备或更新现有设备信息"""
        # 查找是否存在同 ID 设备
        for i, d in enumerate(self.config_data.devices):
            if d.id == device.id:
                self.config_data.devices[i] = device
                logger.info(f"更新设备配置: {device.name} ({device.id})")
                break
        else:
            self.config_data.devices.append(device)
            logger.info(f"新增设备配置: {device.name}")
        
        self.save()

    def delete_device(self, device_id: str):
        """根据 ID 删除设备"""
        original_count = len(self.config_data.devices)
        self.config_data.devices = [d for d in self.config_data.devices if d.id != device_id]
        
        if len(self.config_data.devices) < original_count:
            logger.info(f"已删除设备: {device_id}")
            self.save()
        else:
            logger.warning(f"尝试删除不存在的设备: {device_id}")