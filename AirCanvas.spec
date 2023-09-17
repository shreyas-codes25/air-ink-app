# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['gui.py', 'AirCanvasDemo.py', 'hand_tracking_module.py', 'Gesture_Controller.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['mediapipe', 'mediapipe.python', 'mediapipe.python.solutions', 'mediapipe.python.solutions.drawing_utils', 'mediapipe.python.solutions.drawing_styles', 'mediapipe.python.solutions.face_detection', 'mediapipe.python.solutions.hands', 'mediapipe.python.solutions.pose', 'mediapipe.python.solutions.selfie_segmentation', 'mediapipe.python.solutions.objectron', 'tensorflow', 'cv2', 'numpy', 'mediapipe.python.solutions.hands', 'mediapipe.solution_base'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AirCanvas',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
