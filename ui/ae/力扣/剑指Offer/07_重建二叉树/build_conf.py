import json
from pprint import pprint as pp
import re
import math
import inspect
from glob import glob
from operator import itemgetter

from moviepy.audio.io.AudioFileClip import AudioFileClip
from mutagen.mp3 import MP3

import conf_utils
from constants.share import *

ASSETS_DIR = ASSETS_DIR + '/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树'

files = glob(f'{ASSETS_DIR}/audios/*.mp3')
names = []
for f in files:
    elems = []
    for x in f.split('\\')[-1].split('.'):
        try:
            elems.append(int(x))
        except ValueError:
            pass
    elems.append(f)
    elems = tuple(elems)
    names.append(elems)

names = sorted(names, key=itemgetter(0, 1))
audios_files = []
startTime = 0
for i, af in enumerate(names):
    audio = MP3(af[-1])
    audios_files.append(
        {
            'path': af[-1],
            'layers': [
                {
                    'name': af[-1].split('\\')[-1],
                    'startTime': startTime,
                    'Anchor Point': 'null',
                }
            ],
        }
    )
    startTime += audio.info.length + 0.5


conf = {
    'files': [
        {
            'path': f'{ASSETS_DIR}/Elements.ai', 'import_as_type': IMPORT_AS_TYPE[0]
        },
        {
            'path': f'{ASSETS_DIR}/题目描述.jpg',
        },
        {
            'folder': 'audios',
            'files': audios_files,
            # 'layers': [
            #     {
            #         'name': 'test.mp3',
            #         'startTime': 1.2,
            #         'Anchor Point': 'null',
            #     }
            # ],
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
    'scenes': {},
    'theme': THEME,
}

start_time = 0
for name, func in inspect.getmembers(conf_utils, inspect.isfunction):
    print(name, func)
    scene_name, scene, start_time = func(start_time)
    conf['scenes'][scene_name] = scene

obj = json.dumps(conf, indent=4)
with open(f"{BASE_DIR}/力扣/剑指Offer/07_重建二叉树/conf.json", 'w', encoding='utf-8') as f:
    f.write(obj)
