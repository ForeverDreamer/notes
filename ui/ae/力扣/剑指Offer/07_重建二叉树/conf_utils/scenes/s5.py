import json

from ae.constants.share import *
from .transcript import scenes
from ae.utils.py.color import hex_to_rgb1

name = 's5'


def shot_0(start_time):
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time + i * SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]

    que_elem_width = 80
    que_height = 80
    duration = 20

    with open(BASE_DIR + '力扣/剑指Offer/07_重建二叉树/conf_utils/scenes/s5.json', "r") as f:
        conf_shot_0 = json.loads(f.read())[0]

    conf = {
        'subtitles': subtitles,
        'annotations': [
            {
                'name': '前序遍历注解', 'text': '前序遍历结果按照[根节点|左子树|右子树]排序\n第一个元素就是根节点，但无法确定左子树和右子树',
                'Position': [860, 235], 'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time, 'duration': duration,
            },
            {
                'name': '前序根节点', 'text': '根节点',
                'Position': [800, 485], 'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time+0.5, 'duration': duration-0.5,
            },
            {
                'name': '前序左子树', 'text': '左子树',
                'Position': [965, 485], 'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time+6, 'duration': duration-6,
            },
            {
                'name': '前序右子树', 'text': '右子树',
                'Position': [1124, 485], 'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'span': {'inPoint': start_time + 7.5, 'outPoint': start_time + 20},
            },
            {
                'name': '中序遍历注解', 'text': '中序遍历结果按照[左子树|根节点|右子树]排序\n需要先定位根节点，才能确定左子树和右子树',
                'Position': [860, 685], 'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time, 'duration': duration,
            },
            {
                'name': '中序根节点', 'text': '根节点',
                'Position': [965, 922], 'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time + 0.5, 'duration': duration-0.5,
            },
            {
                'name': '中序左子树', 'text': '左子树',
                'Position': [800, 922], 'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time + 2, 'duration': duration-2,
            },
            {
                'name': '中序右子树', 'text': '右子树',
                'Position': [1124, 922], 'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'span': {'inPoint': start_time + 3.5, 'outPoint': start_time + 20},
            },
        ],
        'vectors': [
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '前序根节点箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [895, 405], 'Rotation': 30,
                'startTime': start_time + 0.5, 'duration': duration - 0.5,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 0.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '前序左子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [980, 405], 'Rotation': -30,
                'startTime': start_time + 6, 'duration': duration - 6,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 6], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '前序右子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [1140, 405], 'Rotation': -30,
                'span': {'inPoint': start_time + 7.5, 'outPoint': start_time + 20},
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 7.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '中序根节点箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [980, 844], 'Rotation': -30,
                'startTime': start_time + 0.5, 'duration': duration - 0.5,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 0.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '中序左子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [895, 838], 'Rotation': 30,
                'startTime': start_time + 2, 'duration': duration - 2,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 2], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '中序右子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [1140, 844], 'Rotation': -30,
                'span': {'inPoint': start_time + 3.5, 'outPoint': start_time + 20},
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 3.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
        ],
        'precomps': [
            {
                'name': '队列.前序数据定位', 'type': 'QUEUE', 'Position': [860, 365], 'Anchor Point': 'LEFT',
                # 'elems': [[3, '#0573E1'], [9, '#FADED8'], [20, '#CEF2ED'], [15, '#CEF2ED'], [7, '#CEF2ED']],
                'elems': [
                    {
                        'key': 3,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [0, 0.5],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['root'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 9,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [6, 7.5],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['left'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 20,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [7.5, 8],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 15,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [7.5, 8],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 7,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [7.5, 8],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }
                ],
                'traverse': 'preorder', 'width': que_elem_width * 5, 'height': que_height,
                'startTime': start_time, 'duration': duration,
                'unit': {
                    'pathGroup': {'type': 'Rect', 'Size': [que_elem_width, que_height]},
                    "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                    "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#000000")},
                },
                # 'effects': {'ADBE Drop Shadow': {}},
            },
            {
                'name': '队列.中序数据定位', 'type': 'QUEUE', 'Position': [860, 805], 'Anchor Point': 'LEFT',
                'elems': [
                    {
                        'key': 9,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [2, 2.5],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['left'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    },
                    {
                        'key': 3,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [0, 0.5],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['root'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 15,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [3.5, 4],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 20,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [3.5, 4],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 7,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [3.5, 4],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }
                ],
                'traverse': 'inorder', 'width': que_elem_width * 5, 'height': que_height,
                'startTime': start_time, 'duration': duration,
                'unit': {
                    'pathGroup': {'type': 'Rect', 'Size': [que_elem_width, que_height]},
                    "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                    "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#000000")},
                },
                # 'effects': {'ADBE Drop Shadow': {}},
            },
            {
                'name': '二叉树.数据定位', 'type': 'BINARY_TREE', 'width': 500, 'height': 500,
                'startTime': start_time, 'duration': duration+5, 'Position': [435, 490],
                'elems': [
                    {'key': 3, 'Color': COLORS['tree']['fillColor']['root']},
                    {'key': 9, 'Color': COLORS['tree']['fillColor']['left']},
                    {'key': 20, 'Color': COLORS['tree']['fillColor']['right']},
                    {'key': None}, {'key': None},
                    {'key': 15, 'Color': COLORS['tree']['fillColor']['right']},
                    {'key': 7, 'Color': COLORS['tree']['fillColor']['right']}],
                'animation': 'false',
                'node': {
                    'shape': {'name': f'Node Shape {VECTORS["node"]["shape"]}/Elements.ai', 'Scale': [80, 80, 80]},
                    'selected': {
                        'pathGroup': {'type': 'Ellipse', 'Size': [100, 100]},
                        "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                    },
                },
                'edge': {
                    'shape': {'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'Anchor Point': 'TOP', 'Scale': [80, 80, 80],
                              'Rotation': 30},
                },
                'Masks': conf_shot_0['precomps']['2']['Masks'],
                'keyframes': {
                    'Masks.Mask 1.Mask Opacity': [[start_time, start_time + 0.5], [0, 100],
                                                  {"spatial": [{"type": 'HOLD'}]}],
                    'Masks.Mask 2.Mask Opacity': [[start_time+1, start_time + 1.5], [0, 100],
                                                  {"spatial": [{"type": 'HOLD'}]}],
                    'Masks.Mask 3.Mask Opacity': [[start_time+2, start_time + 2.5], [0, 100],
                                                  {"spatial": [{"type": 'HOLD'}]}],
                    'Masks.Mask 4.Mask Opacity': [[start_time+3, start_time + 3.5], [0, 100],
                                                  {"spatial": [{"type": 'HOLD'}]}],
                    'Masks.Mask 5.Mask Opacity': [[start_time+4, start_time + 4.5], [0, 100],
                                                  {"spatial": [{"type": 'HOLD'}]}],
                }
                # '3D': 'true'
            }
        ],
        'end_time': end_time,
    }
    return conf


def shot_1(start_time):
    subtitles = []
    for i, text in enumerate(scenes[name][1]):
        subtitles.append([start_time + i * SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]

    que_elem_width = 80
    que_height = 80
    duration = 20
    font_size = 40

    conf = {
        'subtitles': subtitles,
        'annotations': [
            {
                'name': '前序根节点', 'text': '根节点',
                'Position': [1205, 485], 'font': FONTS['cn'], 'fontSize': font_size, 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time + 0.5, 'duration': duration - 0.5,
            },
            {
                'name': '前序左子树', 'text': '左子树',
                'Position': [1330, 490], 'font': FONTS['cn'], 'fontSize': font_size, 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time + 6, 'duration': duration - 6,
            },
            {
                'name': '前序右子树', 'text': '右子树',
                'Position': [1459, 485], 'font': FONTS['cn'], 'fontSize': font_size, 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time + 7.5, 'duration': duration - 10,
            },
            {
                'name': '中序根节点', 'text': '根节点',
                'Position': [1330, 927], 'font': FONTS['cn'], 'fontSize': font_size, 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time + 0.5, 'duration': duration - 0.5,
            },
            {
                'name': '中序左子树', 'text': '左子树',
                'Position': [1205, 922], 'font': FONTS['cn'], 'fontSize': font_size, 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time + 2, 'duration': duration - 2,
            },
            {
                'name': '中序右子树', 'text': '右子树',
                'Position': [1459, 922], 'font': FONTS['cn'], 'fontSize': font_size, 'justification': 'LEFT_JUSTIFY', 'Anchor Point': 'LEFT',
                'startTime': start_time + 3.5, 'duration': duration - 6.5,
            },
        ],
        'vectors': [
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '前序根节点箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [1300, 405], 'Rotation': 30,
                'startTime': start_time + 0.5, 'duration': duration - 0.5,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 0.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '前序左子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [1380, 405],
                'startTime': start_time + 6, 'duration': duration - 6,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 6], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '前序右子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [1460, 405], 'Rotation': -30,
                'startTime': start_time + 7.5, 'duration': duration - 7.5,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 7.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '中序根节点箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [1380, 844],
                'startTime': start_time + 0.5, 'duration': duration - 0.5,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 0.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '中序左子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [1300, 838], 'Rotation': 30,
                'startTime': start_time + 2, 'duration': duration - 2,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 2], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'layerName': '中序右子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [1460, 844], 'Rotation': -30,
                'startTime': start_time + 3.5, 'duration': duration - 3.5,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 3.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
        ],
        'precomps': [
            {
                'name': '队列.前序左边数据定位', 'type': 'QUEUE', 'Position': [860, 365], 'Anchor Point': 'LEFT',
                'elems': [
                    {
                        'key': 3,
                        'Color': COLORS['queue']['fillColor']['left'],
                    }, {
                        'key': 9,
                        'Color': COLORS['queue']['fillColor']['root'],
                    },
                ],
                'traverse': 'preorder', 'width': que_elem_width * 5, 'height': que_height,
                'startTime': start_time, 'duration': duration,
                'unit': {
                    'pathGroup': {'type': 'Rect', 'Size': [que_elem_width, que_height]},
                    "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                    "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#000000")},
                },
            },
            {
                'name': '队列.前序右边数据定位', 'type': 'QUEUE', 'Position': [1020, 365], 'Anchor Point': 'LEFT',
                'elems': [
                    {
                        'key': 20,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [0, 0.5],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 15,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [1, 1.5],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 7,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [2, 2.5],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }
                ],
                'traverse': 'preorder', 'width': que_elem_width * 5, 'height': que_height,
                'startTime': start_time, 'duration': duration,
                'unit': {
                    'pathGroup': {'type': 'Rect', 'Size': [que_elem_width, que_height]},
                    "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                    "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#000000")},
                },
                'keyframes': {
                    'Transform.Position': [[start_time, start_time+0.5], [[1020, 365], [1260, 365]]]
                }
            },
            {
                'name': '队列.中序左边数据定位', 'type': 'QUEUE', 'Position': [860, 805], 'Anchor Point': 'LEFT',
                'elems': [
                    {
                        'key': 9,
                        'Color': COLORS['queue']['fillColor']['left'],
                    },
                    {
                        'key': 3,
                        'Color': COLORS['queue']['fillColor']['root'],
                    },
                ],
                'traverse': 'inorder', 'width': que_elem_width * 5, 'height': que_height,
                'startTime': start_time, 'duration': duration,
                'unit': {
                    'pathGroup': {'type': 'Rect', 'Size': [que_elem_width, que_height]},
                    "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                    "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#000000")},
                },
            },
            {
                'name': '队列.中序右边数据定位', 'type': 'QUEUE', 'Position': [1020, 805], 'Anchor Point': 'LEFT',
                'elems': [
                    {
                        'key': 15,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [1, 1.5],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 20,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [0, 0.5],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 7,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [2, 2.5],
                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']), hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }
                ],
                'traverse': 'inorder', 'width': que_elem_width * 5, 'height': que_height,
                'startTime': start_time, 'duration': duration,
                'unit': {
                    'pathGroup': {'type': 'Rect', 'Size': [que_elem_width, que_height]},
                    "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                    "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#000000")},
                },
                'keyframes': {
                    'Transform.Position': [[start_time, start_time + 0.5], [[1020, 805], [1260, 805]]]
                }
            },
        ],
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    conf_1 = shot_1(conf_0['end_time'] + 1)
    return name, [conf_0, conf_1], conf_1['end_time']
