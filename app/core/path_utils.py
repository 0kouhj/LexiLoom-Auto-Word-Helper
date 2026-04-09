import os
import sys

def get_root_path():
    """获取程序运行的根目录"""
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_bin_path(filename=""):
    """获取 bin 目录下文件的绝对路径"""
    return os.path.join(get_root_path(), "bin", filename)

def get_debug_path(filename=""):
    """获取 debug 目录下文件的绝对路径"""
    path = os.path.join(get_root_path(), "debug")
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.join(path, filename)