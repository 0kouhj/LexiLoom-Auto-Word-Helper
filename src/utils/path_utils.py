# src/utils/path_utils.py
import os
import sys

def get_project_root():
    """获取项目的物理根目录 (beidanci/)"""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 打包后的临时路径
        return sys._MEIPASS
    
    # 当前文件在 src/utils/path_utils.py
    # 向上回溯三级得到根目录
    curr_path = os.path.abspath(__file__)
    return os.path.dirname(os.path.dirname(os.path.dirname(curr_path)))

def get_config_path():
    """获取根目录下的 configs.json"""
    return os.path.join(get_project_root(), "configs.json")

def get_bin_resource(filename=""):
    """获取 bin 文件夹内的资源 (如 adb.exe)"""
    return os.path.join(get_project_root(), "bin", filename)

def get_debug_dir():
    """获取调试日志目录，不存在则创建"""
    path = os.path.join(get_project_root(), "debug")
    if not os.path.exists(path):
        os.makedirs(path)
    return path