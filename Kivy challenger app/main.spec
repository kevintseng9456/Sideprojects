#coding: utf-8 -*-

import sys
import os

from kivy_deps import sdl2, glew

from kivymd import hooks_path as kivymd_hooks_path

path = os.path.abspath("C:\\Users\\love2\\OneDrive - 明志科技大學\\創業競賽\\Mission\\Chanlleger")
path_data = os.path.abspath("C:\\Users\\love2\\OneDrive - 明志科技大學\\創業競賽\\Mission\\Chanlleger\\resources")

a = Analysis(
    ["main.py"],
    pathex=[path],
    datas=[(path_data,"resources")],
    binaries=[],
    hookspath=[kivymd_hooks_path,
    "C:\\Users\\love2\\OneDrive - 明志科技大學\\創業競賽\\Mission\\Chanlleger"],
    hiddenimports=['pkg_resources.py2_warn'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    debug=False,
    strip=False,
    upx=True,
    name="Chanlleger",
    console=True,
)
