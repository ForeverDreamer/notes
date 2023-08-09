from constants.share import *
from .transcript import scenes
from utils.py.color import hex_to_rgb1

name = 's3'


def shot_0(start_time):
    sn = 0
    prefix = f'{name}.{sn}'
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time + i * SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]+SUBTITLES_INTERVAL

    QUE_ELEM_WIDTH = 80
    QUE_ELEM_HEIGHT = 80
    QUE_UNIT['pathGroup']['Size'] = [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT]
    QUE_UNIT['fontSize'] = None
    duration = end_time - start_time

    conf = {
        'layerName': prefix, 'duration': duration,
        'subtitles': subtitles,
        'annotations': [
            {
                'name': f'{prefix}注解', 'text': '遍历结果按照[左子树|根节点|右子树]排序\n需要先定位根节点，才能确定左子树和右子树',
                'Anchor Point': 'LEFT_TOP', 'Position': [695, 710],
                'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY',
                'startTime': start_time, 'span': {'inPoint': start_time, 'outPoint': end_time}
            },
        ],
        'precomps': [
            {
                'layerName': f'{prefix}.队列', 'type': 'QUEUE',
                'Anchor Point': 'LEFT_TOP', 'Position': [695, 849],
                'elems': [{'key': 9}, {'key': 3}, {'key': 15}, {'key': 20}, {'key': 7}],
                'traverse': 'inorder', 'width': QUE_ELEM_WIDTH * 5 + STROKE_ADD, 'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                'startTime': start_time, 'duration': duration,
                'unit': QUE_UNIT,
                # 'effects': {'ADBE Drop Shadow': {}},
            },
            {
                'layerName': f'{prefix}.二叉树', 'type': 'BINARY_TREE',
                'width': 500, 'height': 850, 'Anchor Point': 'LEFT_TOP', 'Position': [695, 86],
                'elems': [{'key': 3}, {'key': 9}, {'key': 20}, {'key': None}, {'key': None}, {'key': 15}, {'key': 7}],
                'startTime': start_time,  'duration': duration, 'animation': 'false', 'traverse': 'inorder',
                'node': {
                    'shape': {'name': 'Node Shape Black/Elements.ai', 'Scale': [80, 80, 80]},
                    'selected': {
                        'pathGroup': {'type': 'Ellipse', 'Size': [100, 100]},
                        "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                        "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#000000")},
                        'Opacity': 0,
                    },
                    'drop': {
                        "pathGroup": {
                            "type": "Group",
                            "vertices": [[0, -50], [50, 0], [0, 50], [-50, 0]],
                            "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0],
                                           [0, 27.6142425537109]],
                            "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0],
                                            [0, -27.6142425537109]],
                            "closed": 'true'
                        },
                        "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                        'Opacity': 0,
                    },
                    'path': {
                        "pathGroup": {
                            "type": "Group",
                            'vertices': [[0, -50], [50, 0], [0, 50], [-50, 0]],
                            'inTangents': [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0],
                                           [0, 27.6142425537109]],
                            'outTangents': [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0],
                                            [0, -27.6142425537109]],
                            "closed": 'true'
                        },
                        "Stroke": {
                            'Stroke Width': PATH_STROKE,
                            "Color": hex_to_rgb1(PATH_COLOR)
                        },
                        "Trim Paths": {
                            'Start': 50,
                            'End': 50,
                            'Offset': -135,
                        },
                        'effects': PATH_EFFECTS,
                    },
                },
                'edge': {
                    'shape': {'name': 'Edge Black/Elements.ai', 'Anchor Point': 'TOP', 'Scale': [80, 80, 80], 'Rotation': 30},
                    'path': {
                        "pathGroup": {
                            'vertices': [[153, 95], [88, 211]],
                            'closed': 'false',
                        },
                        "Stroke": {
                            'Stroke Width': PATH_STROKE,
                            "Color": hex_to_rgb1(PATH_COLOR)
                        },
                        "Trim Paths": {
                            'End': 0,
                        },
                        'effects': PATH_EFFECTS,
                    },
                },
                # '3D': 'true'
            }
        ],
        'end_time': end_time+21,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
