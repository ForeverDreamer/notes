from ae.constants.share import *
from ae.utils.py.color import hex_to_rgb1
from .transcript import scenes

name = 's4'


def shot_0(start_time):
    sn = 0
    prefix = f'{name}.{sn}'
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]+SUBTITLES_INTERVAL
    duration = end_time - start_time

    conf = {
        'images': [
            {
                'name': '题目描述.jpg',
                'layerName': f'{prefix}.题目描述',
                'Scale': [90, 90, 90],
                'Position': [960, 540],
                'startTime': start_time,
                'span': {'inPoint': start_time, 'outPoint': end_time},
                '3D': 'true',
            }
        ],
        'subtitles': subtitles,
        'shapes': [
            {
                'layerName': f'{prefix}.选中框',
                'Position': [694, 540],
                'startTime': start_time,
                'span': {'inPoint': start_time, 'outPoint': end_time},
                'pathGroup': {'type': 'Rect', 'Size': [525, 33]},
                'Stroke': {'Stroke Width': 3, 'Color': hex_to_rgb1('#FF0000')},
                "Trim Paths": {
                    'Offset': -85,
                },
                'keyframes': {
                    'Contents.Group 1.Contents.Trim Paths 1.Start': [
                        [0.5, 1], [50, 0]
                    ],
                    'Contents.Group 1.Contents.Trim Paths 1.End': [
                        [0.5, 1], [50, 100]
                    ],
                    'Transform.Opacity': [[2.9, 3], [100, 0], {'spatial': SPATIAL_HOLD*2}]
                }
            },
        ],
        'camera': {
            'Transform.Point of Interest': [[0, 0.5, 3, 3.5], [[960, 540, 0], [600, 311, 0], [600, 311, 0], [960, 540, 0]]],
            'Transform.Position': [[0, 0.5, 3, 3.5], [[960, 540, -800], [600, 311, -475], [600, 311, -475], [960, 540, -800]]],
        },
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
