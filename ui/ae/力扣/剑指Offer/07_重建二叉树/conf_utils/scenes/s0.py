from ae.constants.share import *
from .transcript import scenes


name = 's0'


def shot_0(start_time):
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]+SUBTITLES_INTERVAL
    conf = {
        'images': [
            {
                'name': '题目描述.jpg',
                'layerName': '题目描述1',
                'Scale': [90, 90, 90],
                'Position': [960, 540],
                'startTime': start_time,
                'span': {'inPoint': start_time, 'outPoint': end_time},
            }
        ],
        'subtitles': subtitles,
        'annotations': [
            {
                'name': '题目官网链接', 'text': 'https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/',
                'fillColor': '#FFA119', 'Position': [1200, 890],
                'span': {'inPoint': start_time+1, 'outPoint': end_time-5}, 'keyframes': {'Opacity': [[0, 0.5, 5, 9], [0, 100, 100, 0]]}
            },
        ],
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
