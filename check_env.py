from src.utils.path_utils import get_config_path
from src.utils.exceptions import ConfigError
from src.models.error_codes import ErrorCode
import os

path = get_config_path()
print(f"检测到配置文件路径: {path}")

if not os.path.exists(path):
    # 模拟抛出我们定义的异常
    raise ConfigError(ErrorCode.CONFIG_LOAD_FAILED, f"路径不存在: {path}")
else:
    print("✅ 地基检查通过，配置文件已就绪！")