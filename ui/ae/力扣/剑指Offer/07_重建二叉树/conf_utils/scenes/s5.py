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
                'startTime': start_time+7.5, 'duration': duration-7.5,
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
                'startTime': start_time + 3.5, 'duration': duration-3.5,
            },
        ],
        'vectors': [
            {
                'name': 'Edge Black/Elements.ai', 'layerName': '前序根节点箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [895, 405], 'Rotation': 30,
                'startTime': start_time + 0.5, 'duration': duration - 0.5,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 0.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': 'Edge Black/Elements.ai', 'layerName': '前序左子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [980, 405], 'Rotation': -30,
                'startTime': start_time + 6, 'duration': duration - 6,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 6], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': 'Edge Black/Elements.ai', 'layerName': '前序右子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [1140, 405], 'Rotation': -30,
                'startTime': start_time + 7.5, 'duration': duration - 7.5,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 7.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': 'Edge Black/Elements.ai', 'layerName': '中序根节点箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [980, 844], 'Rotation': -30,
                'startTime': start_time + 0.5, 'duration': duration - 0.5,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 0.5], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': 'Edge Black/Elements.ai', 'layerName': '中序左子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [895, 838], 'Rotation': 30,
                'startTime': start_time + 2, 'duration': duration - 2,
                'keyframes': {
                    "Transform.Scale": [[start_time, start_time + 2], [[0, 0, 0], [40, 40, 40]]]
                }
            },
            {
                'name': 'Edge Black/Elements.ai', 'layerName': '中序右子树箭头', 'Anchor Point': 'TOP',
                'Scale': [40, 40, 40], 'Position': [1140, 844], 'Rotation': -30,
                'startTime': start_time + 3.5, 'duration': duration - 3.5,
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
                                [hex_to_rgb1('#FFFFFF'), hex_to_rgb1('#0573E1')],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 9,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [6, 7.5],
                                [hex_to_rgb1('#FFFFFF'), hex_to_rgb1('#FADED8')],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 20,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [7.5, 8],
                                [hex_to_rgb1('#FFFFFF'), hex_to_rgb1('#CEF2ED')],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 15,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [7.5, 8],
                                [hex_to_rgb1('#FFFFFF'), hex_to_rgb1('#CEF2ED')],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 7,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [7.5, 8],
                                [hex_to_rgb1('#FFFFFF'), hex_to_rgb1('#CEF2ED')],
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
                                [hex_to_rgb1('#FFFFFF'), hex_to_rgb1('#FADED8')],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    },
                    {
                        'key': 3,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [0, 0.5],
                                [hex_to_rgb1('#FFFFFF'), hex_to_rgb1('#0573E1')],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 15,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [3.5, 4],
                                [hex_to_rgb1('#FFFFFF'), hex_to_rgb1('#CEF2ED')],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 20,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [3.5, 4],
                                [hex_to_rgb1('#FFFFFF'), hex_to_rgb1('#CEF2ED')],
                                {"spatial": [{"type": 'HOLD'}]}
                            ]
                        }
                    }, {
                        'key': 7,
                        'keyframes': {
                            'Contents.Group 1.Contents.Fill 1.Color': [
                                [3.5, 4],
                                [hex_to_rgb1('#FFFFFF'), hex_to_rgb1('#CEF2ED')],
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
        ],
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
