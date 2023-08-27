import copy

from constants.share import (
    FONTS, QUE_UNIT, COLORS, SPATIAL_HOLD, STROKE_ADD, PATH_STROKE, PATH_COLOR, PATH_EFFECTS, SUBTITLES_INTERVAL
)
from .consts import ASSETS_DIR
from .transcript import subtitles as all_subtitles
from utils_v0.py.audio import audios_subtitles
from utils_v0.py.color import hex_to_rgb1

sn = 6
prefix = f's{sn}'


def build_conf(start_time):
    audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles[sn], start_time)
    BINARY_TREE_TIME = 6.5
    START_IDX = 2
    for i in range(START_IDX, len(subtitles[0])):
        subtitles[0][i] += BINARY_TREE_TIME
    for i in range(START_IDX, len(audios)):
        audios[i]['layers'][0]['startTime'] += BINARY_TREE_TIME
    for i in range(START_IDX, len(l_times)):
        l_times[i] += BINARY_TREE_TIME
    end_time += BINARY_TREE_TIME
    duration = end_time - start_time

    QUE_ELEM_WIDTH = 80
    QUE_ELEM_HEIGHT = 80
    _QUE_UNIT = copy.deepcopy(QUE_UNIT)
    _QUE_UNIT['pathGroup']['Size'] = [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT]
    _QUE_UNIT['fontSize'] = None

    conf = {
        'layerName': prefix, 'startTime': start_time, 'duration': duration,
        'subtitles': subtitles,
        'files': [
            {
                'folder': 'audios',
                'files': audios,
            },
        ],
        'texts': [
            {
                'layerName': f'{prefix}.注解', 'text': '遍历结果按照[左子树|根节点|右子树]排序\n需要先定位根节点，才能确定左子树和右子树',
                'Anchor Point': 'LEFT_TOP', 'Position': [450, 157],
                'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY',
            },
            {
                'layerName': f'{prefix}.左', 'text': '左',
                'Anchor Point': 'LEFT_DOWN', 'Position': [1065, 680.5],
                'font': FONTS['cn'],
                'keyframes': {
                    "Transform.Opacity": [
                        [14.5, 15],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.根', 'text': '根',
                'Anchor Point': 'LEFT_DOWN', 'Position': [1146, 677.8],
                'font': FONTS['cn'],
                'keyframes': {
                    "Transform.Opacity": [
                        [15.5, 16],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.右', 'text': '右',
                'Anchor Point': 'LEFT_DOWN', 'Position': [1303, 679.1],
                'font': FONTS['cn'],
                'keyframes': {
                    "Transform.Opacity": [
                        [16.5, 17],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
        ],
        'layers': [
            {
                'sourceName': 'Tree Length Left Down/Elements.ai',
                'Scale': [75, 75], 'Position': [1090.6, 619.3],
                'keyframes': {
                    "Transform.Opacity": [
                        [14.5, 15],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'sourceName': 'Tree Length Root Down/Elements.ai',
                'Scale': [75, 75], 'Position': [1172, 619.3],
                'keyframes': {
                    "Transform.Opacity": [
                        [15.5, 16],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'sourceName': 'Tree Length Right Down 3x/Elements.ai',
                'Scale': [75, 75], 'Position': [1328.6, 619.3],
                'keyframes': {
                    "Transform.Opacity": [
                        [16.5, 17],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
        ],
        'shapes': [
            {
                'layerName': '[左子树|根节点|右子树].选中框',
                'Position': [1023, 182], 'Opacity': 50,
                # 'startTime': start_time,
                # 'span': {'inPoint': start_time, 'outPoint': end_time + 3},
                'pathGroup': {'type': 'Rect', 'Size': [522, 55]},
                'Fill': {'Color': hex_to_rgb1(COLORS['markBox'])},
                'Stroke': {'Stroke Width': 3, 'Color': hex_to_rgb1(COLORS['markBox'])},
                # 'keyframes': {
                #     "Transform.Opacity": [
                #         [0, l_times[2], l_times[3]-SUBTITLES_INTERVAL],
                #         [0, 50, 0],
                #         {"spatial": [{"type": 'HOLD'}] * 3}
                #     ]
                # },
                'effects': {
                    "ADBE Glo2": {}
                }
            },
        ],
        'dsa': [
            {
                'layerName': f'{prefix}.队列', 'type': 'QUEUE', 'duration': duration,
                'Anchor Point': 'LEFT_TOP', 'Position': [1050, 512],
                # 'elems': [[3, '#0573E1'], [9, '#FADED8'], [20, '#CEF2ED'], [15, '#CEF2ED'], [7, '#CEF2ED']],
                'elems': [
                    {'key': 9}, {'key': 3}, {'key': 15}, {'key': 20}, {'key': 7}
                ],
                'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5 + STROKE_ADD, 'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                'unit': _QUE_UNIT,
                # 'effects': {'ADBE Drop Shadow': {}},
            },
            {
                'layerName': f'{prefix}.二叉树', 'type': 'BINARY_TREE', 'rootNodePos': [186, 60],
                'width': 500, 'height': 520, 'Anchor Point': 'LEFT_TOP', 'Position': [472, 356],
                # 'duration': 20, 'Position': [960, 600], 'elems': [[3, '#0573E1'], [9, '#FADED8'], [20, '#CEF2ED'], ['null'], ['null'], [15, '#CEF2ED'], [7, '#CEF2ED']],
                'elems': [
                    {'key': 3}, {'key': 9}, {'key': 20}, {'key': None}, {'key': None}, {'key': 15}, {'key': 7}
                ],
                'duration': duration, 'animation': False, 'traverse': 'preorder',
                'node': {
                    'shape': {'sourceName': 'Node Shape Black/Elements.ai', 'Scale': [80, 80, 80]},
                    # 可以用AtomX或其它插件的precomp,preset,effets替换
                    'selected': {
                        'pathGroup': {'type': 'Ellipse', 'Size': [100, 100]},
                        "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                        "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#000000")},
                    },
                    # 'drop': {
                    #     "pathGroup": {
                    #         "type": "Group",
                    #         "vertices": [[0, -50], [50, 0], [0, 50], [-50, 0]],
                    #         "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0],
                    #                        [0, 27.6142425537109]],
                    #         "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0],
                    #                         [0, -27.6142425537109]],
                    #         "closed": 'true'
                    #     },
                    #     "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                    #     'Opacity': 0,
                    # },
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
                        # 'effects': PATH_EFFECTS,
                    },
                },
                'edge': {
                    'shape': {'sourceName': 'Edge Black/Elements.ai', 'Anchor Point': 'TOP', 'Scale': [80, 80, 80], 'Rotation': 30},
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
                        # 'effects': PATH_EFFECTS,
                    },
                },
                # '3D': 'true'
            }
        ],
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf = build_conf(start_time)
    return sn, conf, conf['end_time']
