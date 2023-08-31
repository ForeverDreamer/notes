from constants.share import FONTS
from .consts import ASSETS_DIR
from .transcript_cn import subtitles as all_subtitles_cn
from .transcript_en import subtitles as all_subtitles_en
from utils_v0.py.audio import audios_subtitles
from utils_v0.py.color import hex_to_rgb1

sn = 7
prefix = f's{sn}'


def build_conf(start_time):
    all_subtitles = list(map(list, zip(all_subtitles_cn[sn], all_subtitles_en[sn])))
    audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles, start_time)
    duration = end_time - start_time

    conf = {
        'layerName': prefix, 'startTime': start_time, 'duration': duration,
        'subtitles': subtitles,
        'files': [
            {
                'folder': 'audios',
                'files': audios,
            },
            {
                'path': f'{ASSETS_DIR}/题目描述.jpg',
                'layers': [
                    {
                        'sourceName': '题目描述.jpg',
                        'layerName': f'{prefix}.题目描述',
                        'Scale': [90, 90, 90],
                        'Position': [960, 540],
                    }
                ],
            }
        ],
        'shapes': [
            {
                'layerName': '选中框', 'Position': [441, 312],
                'pathGroup': {'type': 'Rect', 'Size': [315, 25]},
                'Stroke': {'Stroke Width': 3, 'Color': hex_to_rgb1('#FF0000')},
                'keyframes': {
                    "Opacity": [
                        [1, 1.5, 4.5, 5],
                        [0, 100, 100, 0],
                        # {"spatial": [{"type": 'HOLD'}] * 3}
                    ]
                },
                'effects': {
                    "ADBE Glo2": {}
                }
            },
        ],
        # '3D': True,
        # 'camera': {
        #     # 'Point of Interest': [[1, 0.5, 4, 4.5], [[960, 540, 0], [600, 311, 0], [600, 311, 0], [960, 540, 0]]],
        #     'Position': [
        #         [start_time+1, start_time+1.5, start_time+4.5, start_time+5],
        #         [[960, 540, -800], [960, 540, -570], [960, 540, -570], [960, 540, -800]]
        #     ],
        # },
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf = build_conf(start_time)
    return sn, conf, conf['end_time']
