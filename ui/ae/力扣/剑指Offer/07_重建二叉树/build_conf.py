import json
from pprint import pprint as pp
import re
import math
import inspect

import shots
from constants.share import *

ASSETS_DIR = ASSETS_DIR + '/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树'


conf = {
    'files': [
        {
            'path': f'{ASSETS_DIR}/Elements.ai', 'import_as_type': IMPORT_AS_TYPE[0]
        },
        {
            'path': f'{ASSETS_DIR}/题目描述.jpg',
        },
        {
            'path': f'{ASSETS_DIR}/Linus Torvalds.jfif',
        },
        {
            'path': f'{ASSETS_DIR}/linux.png',
        },
        {
            'path': f'{ASSETS_DIR}/git.bmp',
        },
        # {
        #     'path': f'{BASE_DIR}代码调试.mp4',
        # },
        # {
        #     'path': 'G:/BaiduNetdiskDownload/AtomX 2021-08 整理/AtomX Packages/AtomX All-In-One_Trendy Graphics v5.4/Atom Preview Assets/Sound Effects/Magic/SFX - Magic 25.wav',
        #     'import_as_type': IMPORT_AS_TYPE[1],
        # },
        # {
        #     'path': 'G:/BaiduNetdiskDownload/AtomX 2021-08 整理/AtomX Packages/AtomX All-In-One_Trendy Graphics v5.4/Atom Preview Assets/Sound Effects/Fast Swooshes/SFX - Fast Swoosh 15.wav',
        #     'import_as_type': IMPORT_AS_TYPE[1],
        # },
    ],
    'shots': {},
    'theme': THEME,
}

start_time = 0
for name, func in inspect.getmembers(shots, inspect.isfunction):
    print(name, func)
    sn, shot, start_time = func(start_time)
    conf['shots'][sn] = shot

obj = json.dumps(conf, indent=4)
with open(f"{BASE_DIR}/力扣/剑指Offer/07_重建二叉树/conf.json", 'w', encoding='utf-8') as f:
    f.write(obj)
