from .consts import ASSETS_DIR
from .transcript import subtitles as all_subtitles
from utils_v0.py.audio import audios_subtitles

sn = 0
prefix = f's{sn}'


def build_conf(start_time):
    audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles[sn], start_time)
    times = subtitles[0]
    duration = end_time - start_time

    conf = {
        'layerName': prefix, 'startTime': start_time, 'duration': duration,
        'subtitles': subtitles,
        # 'presets': [
        #     {
        #         'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Transitions - Movement/Slide - drop.ffx',
        #         'keyframes': {
        #             'Slide Master Control.Transition Completion': [
        #                 [0, 1],
        #                 [0, 100],
        #                 {"temporal": [[[0, 0.1], [200, 50]], [[0, 30], [0, 0.1]]]},
        #                 True
        #             ]
        #         }
        #     }
        # ],
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
                        'startTime': start_time,
                        # 'span': {'inPoint': start_time, 'outPoint': end_time},
                    }
                ],
            }
        ],
        'texts': [
            {
                'name': f'{prefix}.题目官网链接', 'text': 'https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/',
                'fillColor': '#FFA119', 'Position': [1200, 890],
                # 'start_time': start_time,
                # 'span': {'inPoint': start_time, 'outPoint': end_time},
                'keyframes': {
                            "Transform.Opacity": [
                                [l_times[3], l_times[3]+0.5, l_times[4], l_times[4]+0.5],
                                [0, 100, 100, 0],
                                # {"spatial": [{"type": 'HOLD'}] * 3}
                            ]
                        }
            },
        ],
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf = build_conf(start_time)
    return sn, conf, conf['end_time']
