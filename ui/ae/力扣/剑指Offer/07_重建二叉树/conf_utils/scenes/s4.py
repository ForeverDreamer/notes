from ae.constants.share import *
from ae.utils.py.color import hex_to_rgb1
from .transcript import scenes

name = 's4'


def shot_0(start_time):
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]
    conf = {
        'images': [
            {
                'name': '题目描述.jpg',
                'layerName': '题目描述2',
                'Scale': [90, 90, 90],
                'Position': [960, 540],
                'startTime': start_time,
                'span': {'inPoint': start_time, 'outPoint': end_time+4},
                '3D': 'true',
            }
        ],
        'subtitles': subtitles,
        'shapes': [
            {
                'layerName': '结果中都不含重复的数字.选中框',
                'Position': [694, 540],
                'startTime': start_time,
                'span': {'inPoint': start_time, 'outPoint': end_time+3},
                'pathGroup': {'type': 'Rect', 'Size': [525, 33]},
                'Stroke': {'Stroke Width': 3, 'Color': hex_to_rgb1('#FF0000')},
                "Trim Paths": {
                    'Offset': -85,
                },
                'keyframes': {
                    'Contents.Group 1.Contents.Trim Paths 1.Start': [[start_time+0.5, start_time+1], [50, 0]],
                    'Contents.Group 1.Contents.Trim Paths 1.End': [[start_time+0.5, start_time+1], [50, 100]],
                }
            },
        ],
        'camera': {
            'Transform.Point of Interest': [[start_time, start_time+0.5, start_time+3, start_time+3.5], [[960, 540, 0], [600, 311, 0], [600, 311, 0], [960, 540, 0]]],
            'Transform.Position': [[start_time, start_time+0.5, start_time+3, start_time+3.5], [[960, 540, -800], [600, 311, -475], [600, 311, -475], [960, 540, -800]]],
        },
        'end_time': end_time+3,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
