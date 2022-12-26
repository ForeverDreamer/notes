from ae.utils.py.color import hex_to_rgb1
from .transcript import scenes


def shot_1():
    subtitles = []
    for i, text in enumerate(scenes['s1'][0]):
        subtitles.append([i, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))

    conf = {
        'images': [
            {
                'name': '题目描述.jpg',
                'layerName': '题目描述',
                'Scale': [90, 90, 90],
                'Position': [960, 540],
                'startTime': 0,
                'span': {'inPoint': 0, 'outPoint': 5}
            }
        ],
        'subtitles': subtitles,
        'annotations': [
            {
                'name': '题目官网链接', 'text': 'https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/',
                'fillColor': '#FFA119', 'Position': [1200, 890],
                'span': {'inPoint': 0, 'outPoint': 9}, 'keyframes': {'Opacity': [[0, 0.5, 5, 9], [0, 100, 100, 0]]}
            },
        ]
    }
    return conf


def create_all():
    return 's1', [shot_1()]
