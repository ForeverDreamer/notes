import json
from pprint import pprint as pp
import re
import math
import inspect

import conf_utils
from ae.constants.share import *

BASE_DIR = 'D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/'
IMPORT_AS_TYPE = ('COMP_CROPPED_LAYERS', 'FOOTAGE', 'COMP', 'PROJECT')

conf = {
    'files': [
        {
            'path': f'{BASE_DIR}Elements.ai', 'import_as_type': IMPORT_AS_TYPE[0]
        },
        {
            'path': f'{BASE_DIR}题目描述.jpg', 'import_as_type': IMPORT_AS_TYPE[1]
        },
        {
            'path': f'{BASE_DIR}test.mp3', 'import_as_type': IMPORT_AS_TYPE[1],
            'layers': [
                {
                    'name': 'test.mp3',
                    'startTime': 1.2,
                    'Anchor Point': 'null',
                }
            ],
        },
        # {
        #     'path': 'G:/BaiduNetdiskDownload/AtomX 2021-08 整理/AtomX Packages/AtomX All-In-One_Trendy Graphics v5.4/Atom Preview Assets/Sound Effects/Magic/SFX - Magic 25.wav',
        #     'import_as_type': IMPORT_AS_TYPE[1],
        # },
        # {
        #     'path': 'G:/BaiduNetdiskDownload/AtomX 2021-08 整理/AtomX Packages/AtomX All-In-One_Trendy Graphics v5.4/Atom Preview Assets/Sound Effects/Fast Swooshes/SFX - Fast Swoosh 15.wav',
        #     'import_as_type': IMPORT_AS_TYPE[1],
        # },
    ],
    'scenes': {},
}
for name, func in inspect.getmembers(conf_utils, inspect.isfunction):
    print(name, func)
    scene_name, scene = func()
    conf['scenes'][scene_name] = scene
# Serializing json
obj = json.dumps(conf, indent=4)
# print(obj)
with open("D:/data_files/notes/ui/ae/力扣/剑指Offer/07_重建二叉树/conf.json", 'w', encoding='utf-8') as f:
    f.write(obj)
