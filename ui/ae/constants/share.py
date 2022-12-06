AE_WINDOW_NAME = 'Adobe After Effects'
BASE_DIR = 'D:/data_files/notes/ui/ae/'
# 脚本调用间隔，否则会各种报错
CALL_INTERVAL = 0.5

# Comp默认设置
PIXEL_ASPECT = 1
FRAME_RATE = 30

INIT_ENV = [
    f'var file = new File("{BASE_DIR}utils/jsx/init.jsx");',
    'file.open("r");',
    'eval(file.read());',
    'file.close();',
]
