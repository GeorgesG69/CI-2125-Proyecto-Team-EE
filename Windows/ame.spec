# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Calculadora de Resistores'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ame',
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
    version='C:\\Users\\Georges\\AppData\\Local\\Temp\\c4dcee65-c42f-4996-aa1b-53a04779578d',
    icon=['C:\\Users\\Georges\\Documents\\Uni\\EM 2024\\Compu 1\\CI2125\\Proyecto\\CI-2125-Proyecto-Team-EE\\Main_dev\\assets\\icon.ico'],
)