import json
import inspect

from constants.share import IMPORT_AS_TYPE, THEME, BASE_DIR
import shots
from shots.consts import ASSETS_BASE, ASSETS_DIR, CONF_PATH


conf = {
    'files': [
        # {
        #     'path': f'{ASSETS_BASE}/Elements.ai', 'import_as_type': IMPORT_AS_TYPE[0]
        # },
        # {
        #     'path': f'{ASSETS_DIR}/题目描述.jpg',
        # },
        # {
        #     'path': f'{ASSETS_DIR}/Linus Torvalds.jfif',
        # },
        # {
        #     'path': f'{ASSETS_DIR}/linux.png',
        # },
        # {
        #     'path': f'{ASSETS_DIR}/git.bmp',
        # },
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
        # {
        #     'folder': 'Atom',
        #     'files': [
        #         {
        #             'folder': 'Trendy Graphics',
        #             'files': [
        #                 {
        #                     'path': 'G:\BaiduNetdiskDownload\AtomX 2021-08 整理\AtomX Packages\AtomX All-In-One_Trendy Graphics v5.4\Atom After Effects\Typography\Clean\Minimal\Minimal II.aep',
        #                     'import_as_type': IMPORT_AS_TYPE[3]
        #                 }
        #             ]
        #         }
        #     ]
        # },
    ],
    'shots': {},
    'theme': THEME,
}

start_time = 0
for name, func in inspect.getmembers(shots, inspect.isfunction):
    print(name, func)
    presets = [
        {
            'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Transitions - Wipes/Grid Wipe.ffx',
            'keyframes': {
                'Grid Wipe.Transition Completion': [
                    [start_time, start_time+0.3],
                    [0, 100],
                    None,
                    True
                ]
            }
        }
    ]
    sn, shot, start_time = func(start_time)
    # shot['presets'] = presets
    conf['shots'][sn] = shot
conf['duration'] = start_time

obj = json.dumps(conf, ensure_ascii=False, indent=4)
with open(CONF_PATH, 'w', encoding='utf-8') as f:
    f.write(obj)
