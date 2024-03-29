import importlib
from Ae.utils.py.color import hex_to_rgb1

mdl = importlib.import_module(f'Ae.constants.themes.t{3}')

AE_WINDOW_NAME = 'Adobe After Effects'
ASSETS_DIR = 'G:/沉浸式学习'
BASE_DIR = 'D:/data_files/notes/ui/Ae'
# 脚本调用间隔，否则会各种报错
CALL_INTERVAL = 0

# Comp
PIXEL_ASPECT = 1
FRAME_RATE = 30

# 队列
QUE_ELEM_WIDTH = 60
QUE_ELEM_HEIGHT = 60
QUE_UNIT = {
    'pathGroup': {'type': 'Rect', 'Size': [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT], 'Roundness': 10},
    'Fill': {'Color': hex_to_rgb1('#FFFFFF')},
    'Stroke': {'Stroke Width': 1, 'Color': hex_to_rgb1(mdl.COLORS['text'])},
    'fontSize': 25,
}
STROKE_ADD = QUE_UNIT['Stroke']['Stroke Width'] * 4

# 栈
STACK_ELEM_WIDTH = 150
STACK_ELEM_HEIGHT = 50
STACK_UNIT = {
    'pathGroup': {'type': 'Rect', 'Size': [STACK_ELEM_WIDTH, STACK_ELEM_HEIGHT], 'Roundness': 10},
    "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
    "Stroke": {'Stroke Width': 1, "Color": hex_to_rgb1("#000000")},
    'fontSize': 25,
}

IMPORT_AS_TYPE = ('COMP_CROPPED_LAYERS', 'FOOTAGE', 'COMP', 'PROJECT')

SUBTITLES_INTERVAL = 0.5
SHOTS_INTERVAL = 1

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

PATH_EFFECTS = {'ADBE Glo2': {}}
PATH_STROKE = 10

FONTS = mdl.FONTS
FONT_SIZES = mdl.FONT_SIZES
COLORS = mdl.COLORS
CODE_COLORS = mdl.CODE_COLORS
VECTORS = mdl.VECTORS
SPATIAL_HOLD = [{"type": 'HOLD'}]

THEME = {
    'FONTS': FONTS,
    'FONT_SIZES': FONT_SIZES,
    'COLORS': COLORS,
    'CODE_COLORS': CODE_COLORS,
    'VECTORS': VECTORS,
    'SPATIAL_HOLD': SPATIAL_HOLD,
    'QUE_ELEM_WIDTH': QUE_ELEM_WIDTH,
    'QUE_ELEM_HEIGHT': QUE_ELEM_HEIGHT,
    'QUE_UNIT': QUE_UNIT,
    'STROKE_ADD': STROKE_ADD
}

PATH_COLOR = COLORS['tree']['fillColor']['pathColor']
