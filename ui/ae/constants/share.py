AE_WINDOW_NAME = 'Adobe After Effects'
BASE_DIR = 'D:/data_files/notes/ui/ae/'
# 脚本调用间隔，否则会各种报错
CALL_INTERVAL = 0.5

# Comp默认设置
PIXEL_ASPECT = 1
FRAME_RATE = 30

INCLUDES = '''
#includepath "../utils/jsx";\n
#include "json.jsx";\n
#include "share.jsx";\n
#include "color.jsx";\n
#include "effects.jsx";\n
#include "presets.jsx";\n
#include "text.jsx";\n
#include "shape.jsx";\n
#include "precomp.jsx";\n
#include "animation.jsx"\n;
'''

INIT_ENV = [
    f'var file = new File("{BASE_DIR}utils/jsx/init.jsx");',
    'file.open("r");',
    'eval(file.read());',
    'file.close();',
]
