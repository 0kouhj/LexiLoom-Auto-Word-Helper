# -*- mode: python ; coding: utf-8 -*-
import os
import rapidocr_onnxruntime
# 🔥 引入官方强力收集工具
from PyInstaller.utils.hooks import collect_dynamic_libs

block_cipher = None

# 🔥 强制抓取 NumPy 和 ONNX 的所有底层 DLL (直接破除 _multiarray_umath 丢失的诅咒)
numpy_binaries = collect_dynamic_libs('numpy')
onnx_binaries = collect_dynamic_libs('onnxruntime')

# 获取 OCR 资源路径 (保住脑子)
rapid_root = os.path.dirname(rapidocr_onnxruntime.__file__)

# 纯黑名单：只杀大毒瘤，保住 ADB
SAFE_BLACKLIST = [
    'Qt6WebEngine', 'Qt6WebEngineCore', 'Qt6WebEngineWidgets', 
    'opencv_videoio_ffmpeg', 
    'opengl32sw.dll',
    'Qt6Pdf', 'Qt6Qml', 'Qt6Quick', 'Qt6VirtualKeyboard'
]

a = Analysis(
    ['D:\\files\\University\\beidanci\\run.py'],
    pathex=[],
    # 🔥 将收集到的底层库硬塞进 binaries，优先级最高！
    binaries=numpy_binaries + onnx_binaries,
    datas=[
        ('D:\\files\\University\\beidanci\\bin', 'bin'), 
        ('D:\\files\\University\\beidanci\\src/gui/resources', 'src/gui/resources'),
        (rapid_root, 'rapidocr_onnxruntime'),
    ],
    hiddenimports=['cv2', 'numpy', 'rapidocr_onnxruntime', 'onnxruntime'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    # 🔥 撤销对 scipy 和 pandas 的排除，防止牵连 numpy 的数学底座
    excludes=['paddle', 'torch', 'tensorflow', 'matplotlib', 'tzdata', 'tkinter'],
    noarchive=False,
    optimize=0, # 必须为 0
)

# 稳健过滤：只杀名单里的，其他全部放行
filtered_binaries = []
for (dest, source, kind) in a.binaries:
    d_lower = dest.lower()
    if any(bad.lower() in d_lower for bad in SAFE_BLACKLIST):
        continue
    filtered_binaries.append((dest, source, kind))

a.binaries = filtered_binaries

# 清理重复冗余代码
filtered_datas = []
for (dest, source, kind) in a.datas:
    if 'rapidocr_onnxruntime' in dest and dest.endswith(('.py', '.pyc')):
        continue
    filtered_datas.append((dest, source, kind))
a.datas = filtered_datas

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LexiLoom',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False, 
    upx=False, 
    console=False, 
    icon=['D:\\files\\University\\beidanci\\src\\gui\\resources\\icon.ico'],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name='LexiLoom',
)