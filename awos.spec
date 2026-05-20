# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller Specification File for AWOS Desktop App
This bundles everything into a single executable
"""

block_cipher = None

a = Analysis(
    ['awos_gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('public', 'public'),  # Include all HTML/CSS/JS/images
    ],
    hiddenimports=[
        'flask',
        'flask_cors',
        'webview',
        'numpy',
        'pandas',
        'sklearn',
        'sklearn.ensemble',
        'sklearn.preprocessing',
        'sklearn.metrics',
        'requests',
        'awos_server',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'IPython',
        'jupyter',
    ],
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
    name='AWOS_Weather_Station',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'
)