# -*- mode: python -*-

block_cipher = None


a = Analysis(['gene_expression.tkinter.py'],
             pathex=['E:\\gene_expression\\Personal-Projects\\gene expression'],
             binaries=[],
             datas=[("Assets\\icon.ico", "Assets\\")],
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
          name='gene expression',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='Assets\\icon.ico')
