# -*- mode: python -*-

block_cipher = None



a = Analysis(['management_log.py'],
             pathex=['C:\\Users\\tomal\\Desktop\\Programs\\classroom_management_plan'],
             binaries=[],
             datas=[('Assets\\icon.ico', 'Assets'), ( 'Assets\\addicon.png', 'Assets'), ( 'Assets\\deleteicon.png', 'Assets'), ( 'Assets\\exiticon.png', 'Assets'), ( 'Assets\\openicon.png', 'Assets'), ( 'Assets\\refreshicon.png', 'Assets'), ( 'Assets\\saveicon.png', 'Assets'), ( 'Assets\\transfericon.png', 'Assets'), ( 'Assets\\logo.png', 'Assets')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='management_log',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='Assets\\icon.ico')
