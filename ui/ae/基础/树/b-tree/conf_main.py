import inspect
import json

from ae.constants.share import *
import scenes

CONF_BASE_DIR = 'D:/沉浸式学习/数据结构与算法/基础/树/b-tree/'

conf = {
    'files': [
        {
            'path': f'{CONF_BASE_DIR}Elements.ai', 'import_as_type': IMPORT_AS_TYPE[0]
        },
        # {
        #     'path': f'{CONF_BASE_DIR}题目描述.jpg', 'import_as_type': IMPORT_AS_TYPE[1]
        # },
        # {
        #     'path': f'{CONF_BASE_DIR}test.mp3', 'import_as_type': IMPORT_AS_TYPE[1],
        #     'layers': [
        #         {
        #             'name': 'test.mp3',
        #             'startTime': 1.2,
        #             'Anchor Point': 'null',
        #         }
        #     ],
        # },
        # {
        #     'path': f'{CONF_BASE_DIR}Linus Torvalds.jfif', 'import_as_type': IMPORT_AS_TYPE[1],
        # },
        # {
        #     'path': f'{CONF_BASE_DIR}linux.png', 'import_as_type': IMPORT_AS_TYPE[1],
        # },
        # {
        #     'path': f'{CONF_BASE_DIR}git.bmp', 'import_as_type': IMPORT_AS_TYPE[1],
        # },
    ],
    'scenes': {},
    'theme': THEME,
}

start_time = 0
for name, func in inspect.getmembers(scenes, inspect.isfunction):
    print(name, func)
    scene_name, scene, start_time = func(start_time)
    conf['scenes'][scene_name] = scene

obj = json.dumps(conf, indent=4)
with open(f"{BASE_DIR}基础/树/b-tree/conf.json", 'w', encoding='utf-8') as f:
    f.write(obj)
