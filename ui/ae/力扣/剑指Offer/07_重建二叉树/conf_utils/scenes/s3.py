from ae.constants.share import *
from .transcript import scenes
from ae.utils.py.color import hex_to_rgb1

name = 's3'


def shot_0(start_time):
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time + i * SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]

    que_elem_width = 80
    que_height = 80
    conf = {
        'subtitles': subtitles,
        'annotations': [
            {
                'name': '中序遍历注解', 'text': '遍历结果按照[左子树|根节点|右子树]排序\n需要先定位根节点，才能确定左子树和右子树', 'Position': [1000, 770],
                'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY', 'span': {'inPoint': end_time+10, 'outPoint': end_time+21}
            },
        ],
        'precomps': [
            {
                'name': '队列.中序遍历演示', 'type': 'QUEUE', 'Position': [914, 890],
                'elems': [[9], [3], [15], [20], [7]],
                'traverse': 'inorder', 'width': que_elem_width * 5, 'height': que_height, 'duration': 20,
                'startTime': end_time + 1,
                'unit': {
                    'pathGroup': {'type': 'Rect', 'Size': [que_elem_width, que_height]},
                    "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                    "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#000000")},
                },
                # 'effects': {'ADBE Drop Shadow': {}},
            },
            {
                'name': '二叉树.中序遍历演示', 'type': 'BINARY_TREE', 'width': 500, 'height': 850,
                'duration': 17.5, 'Position': [960, 500], 'elems': [[3], [9], [20], ['null'], ['null'], [15], [7]],
                'startTime': end_time + 1, 'animation': 'false', 'traverse': 'inorder',
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
                            'Stroke Width': 5,
                            "Color": hex_to_rgb1("#FF0000")
                        },
                        "Trim Paths": {
                            'Start': 50,
                            'End': 50,
                            'Offset': -135,
                        },
                        'effects': {'ADBE Glo2': {}},
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
                            'Stroke Width': 5,
                            "Color": hex_to_rgb1("#FF0000")
                        },
                        "Trim Paths": {
                            'End': 0,
                        },
                        'effects': {'ADBE Glo2': {}},
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
