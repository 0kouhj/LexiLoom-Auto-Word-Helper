import PyInstaller.__main__
import os

# 获取当前项目根目录
root = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'run_old.py',                      # 主入口文件
    '--name=LexiLoom',             # 生成的 exe 名称
    '--noconsole',                 # 运行时不显示黑窗口
    '--onedir',                    # 产生一个文件夹（实战最稳，方便放 adb 和 models）
    '--clean',                     # 打包前清理临时文件
    
    # 核心数据文件包含
    f'--add-data={os.path.join(root, "app", "gui", "main_window.ui")}{os.pathsep}app/gui',
    f'--add-data={os.path.join(root, "bin")}{os.pathsep}bin',
    
    # 强制收集 EasyOCR 的隐藏依赖
    '--collect-all=easyocr',
    '--collect-all=skimage',
    '--collect-all=pywt',
])