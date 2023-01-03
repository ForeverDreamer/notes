import importlib

AE_WINDOW_NAME = 'Adobe After Effects'
BASE_DIR = 'D:/data_files/notes/ui/ae/'
# 脚本调用间隔，否则会各种报错
CALL_INTERVAL = 0

# Comp默认设置
PIXEL_ASPECT = 1
FRAME_RATE = 30

IMPORT_AS_TYPE = ('COMP_CROPPED_LAYERS', 'FOOTAGE', 'COMP', 'PROJECT')

SUBTITLES_INTERVAL = 5

mdl = importlib.import_module(f'ae.constants.themes.t{3}')

# 这种方式虽然可行但会导致ide报错提示！
# # is there an __all__?  if so respect it
# if "__all__" in mdl.__dict__:
#     names = mdl.__dict__["__all__"]
# else:
#     # otherwise we import all names that don't begin with _
#     names = [x for x in mdl.__dict__ if not x.startswith("_")]
#
# # now drag them in
# globals().update({k: getattr(mdl, k) for k in names})
FONTS = mdl.FONTS
COLORS = mdl.COLORS
CODE_COLORS = mdl.CODE_COLORS
VECTORS = mdl.VECTORS
