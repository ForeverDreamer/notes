from ae.constants.share import *
from .transcript import scenes
from ae.utils.py.color import hex_to_rgb1

name = 's2'


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
    duration = 20

    conf = {
        'subtitles': subtitles,
        'annotations': [
            {
                'name': f'{prefix}注解', 'text': '遍历结果按照[根节点|左子树|右子树]排序\n第一个元素就是根节点，但无法确定左子树和右子树',
                'Anchor Point': 'LEFT_TOP', 'Position': [695, 710],
                'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY',
                'startTime': start_time, 'span': {'inPoint': start_time, 'outPoint': end_time}
            },
        ],
        'precomps': [
            {
                'layerName': f'{prefix}.队列', 'type': 'QUEUE',
                'Anchor Point': 'LEFT_TOP', 'Position': [695, 849],
                # 'elems': [[3, '#0573E1'], [9, '#FADED8'], [20, '#CEF2ED'], [15, '#CEF2ED'], [7, '#CEF2ED']],
                'elems': [
                    {
                        'key': 3,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [start_time, duration - 1],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["root"])
                                ],
                                {"spatial": SPATIAL_HOLD * 2},
                            ]
                        }
                    },
                    {'key': 9}, {'key': 20}, {'key': 15}, {'key': 7}
                ],
                'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5 + STROKE_ADD, 'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                'startTime': start_time, 'duration': duration,
                'unit': QUE_UNIT,
                # 'effects': {'ADBE Drop Shadow': {}},
            },
            {
                'layerName': f'{prefix}.二叉树', 'type': 'BINARY_TREE',
                'width': 500, 'height': 850, 'Anchor Point': 'LEFT_TOP', 'Position': [695, 86],
                # 'duration': 20, 'Position': [960, 600], 'elems': [[3, '#0573E1'], [9, '#FADED8'], [20, '#CEF2ED'], ['null'], ['null'], [15, '#CEF2ED'], [7, '#CEF2ED']],
                'elems': [
                    {
                        'key': 3,
                        'selectedKeyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [start_time, duration - 1],
                                [
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["default"]),
                                    hex_to_rgb1(COLORS["tree"]["fillColor"]["root"])
                                ],
                                {"spatial": SPATIAL_HOLD * 2},
                            ]
                        }
                    },
                    {'key': 9}, {'key': 20}, {'key': None}, {'key': None}, {'key': 15}, {'key': 7}
                ],
                'startTime': start_time,  'duration': duration, 'animation': 'false', 'traverse': 'preorder',
                'node': {
                    'shape': {'name': 'Node Shape Black/Elements.ai', 'Scale': [80, 80, 80]},
                    # 可以用AtomX或其它插件的precomp,preset,effets替换
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
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
