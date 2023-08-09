import inspect
import json

from Ae.constants.share import *
import scenes

ASSETS_DIR = ASSETS_DIR + '/数据结构与算法/基础/树/b-tree'

conf = {
    'files': [
        {
            'path': f'{ASSETS_DIR}/Elements.ai', 'import_as_type': IMPORT_AS_TYPE[0]
        },
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
with open(f"{BASE_DIR}/基础/树/b-tree/conf.json", 'w', encoding='utf-8') as f:
    f.write(obj)
