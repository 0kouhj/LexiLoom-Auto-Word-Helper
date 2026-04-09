# build.py
import PyInstaller.__main__
import os
import shutil
from src.utils.path_utils import get_project_root

def build_with_spec():
    root = get_project_root()
    spec_path = os.path.join(root, "LexiLoom.spec")
    dist_path = os.path.join(root, "dist")

    print("🚀 使用白名单模式打包...")
    PyInstaller.__main__.run([spec_path, '--clean'])

    # 处理 configs.json
    output_dir = os.path.join(dist_path, "LexiLoom")
    src_config = os.path.join(root, "configs.json")
    dst_config = os.path.join(output_dir, "configs.json")
    
    if os.path.exists(src_config) and not os.path.exists(dst_config):
        shutil.copy(src_config, dst_config)
        print("✅ 配置文件已外置。")

if __name__ == "__main__":
    build_with_spec()