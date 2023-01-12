import json

from ae.constants.share import *
from .transcript import scenes
from ae.utils.py.color import hex_to_rgb1

name = 's5'


def shot_0(start_time):
    sn = 0
    prefix = f'{name}.{sn}'
    subtitles = []
    for i, text in enumerate(scenes[name][sn]):
        subtitles.append([start_time + i * SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]+SUBTITLES_INTERVAL

    duration = 20

    # 工作量大或相互关联的配置提到前边统一填写，避免滚轮滚上滚下到处找，头都晕了~
    times = {
        'que1': {
            'Opacity':  [0, 8],
            'Position': [0, 8, 8.5],
        },
        'que2': {
            'Opacity':  [0, 8],
            'Position': [0, 8, 8.5],
        },
        'preorder': [
            [0, 0.5],
            [4, 4.5],
            [7, 7.5],
            [9, 9.5],
            [13, 13.5],
            [16, 16.5],
        ],
        'inorder': [
            [1, 1.5],
            [3, 3.5],
            [6, 6.5],
            [10, 10.5],
            [12, 12.5],
            [15, 15.5],
        ],
        'tree': [
            [2, 2.5],
            [5, 5.5],
            [11, 11.5],
            [14, 14.5],
            [17, 17.5],
        ]
    }
    opacitys = [0, 100]
    opacitys_inv = [100, 0]
    spatial = [{"type": 'HOLD'}]

    annotation_height = 50

    with open(BASE_DIR + '力扣/剑指Offer/07_重建二叉树/conf_utils/scenes/s5.json', "r") as f:
        conf_shot_0 = json.loads(f.read())

    conf = {
        'subtitles': subtitles,
        'misc': [
            {
                'layerName': f'{prefix}.前序数据分布',
                'width': 1020, 'height': 300,
                'Anchor Point': 'LEFT_TOP', 'Position': [830, 140],
                'startTime': start_time, 'duration': duration,
                'texts': [
                    {
                        'layerName': '前序遍历注解', 'text': '前序遍历结果按照[根节点|左子树|右子树]排序\n第一个元素就是根节点，但无法确定左子树和右子树',
                        'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY',
                        'Anchor Point': 'LEFT_TOP', 'Position': [0, 0],
                        # 'startTime': start_time, 'duration': duration,
                    },
                ],
                'misc': [
                    {
                        'layerName': '数据.All',
                        'width': QUE_ELEM_WIDTH * 5 + STROKE_ADD, 'height': QUE_ELEM_WIDTH + STROKE_ADD + annotation_height,
                        'Anchor Point': 'LEFT_TOP', 'Position': [0, 150],
                        'startTime': start_time, 'duration': duration,
                        'keyframes': {
                            'Transform.Opacity': [
                                times['que1']['Opacity'], opacitys_inv,
                                {"spatial": spatial * len(times['que1']['Opacity'])}
                            ]
                        },
                        'precomps': [
                            {
                                'layerName': '队列', 'type': 'QUEUE', 'traverse': 'preorder',
                                'width': QUE_ELEM_WIDTH * 5 + STROKE_ADD, 'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                                'Position': [0, 0], 'Anchor Point': 'LEFT_TOP',
                                # 'elems': [[3, '#0573E1'], [9, '#FADED8'], [20, '#CEF2ED'], [15, '#CEF2ED'], [7, '#CEF2ED']],
                                'startTime': start_time, 'duration': duration,
                                'unit': QUE_UNIT,
                                'elems': [
                                    {
                                        'key': 3,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['preorder'][0],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['root'])],
                                                {"spatial": spatial * len(times['preorder'][0])}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 9,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['preorder'][1],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['left'])],
                                                {"spatial": spatial * len(times['preorder'][1])}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 20,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['preorder'][2],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                                {"spatial": spatial * len(times['preorder'][2])}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 15,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['preorder'][2],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                                {"spatial": spatial * len(times['preorder'][2])}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 7,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['preorder'][2],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                                {"spatial": spatial * len(times['preorder'][2])}
                                            ]
                                        }
                                    }
                                ],
                                # 'effects': {'ADBE Drop Shadow': {}},
                            },
                        ],
                        'misc': [
                            {
                                'layerName': '根节点注解',
                                'width': QUE_ELEM_WIDTH, 'height': annotation_height,
                                'Anchor Point': 'LEFT_TOP', 'Position': [0, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['preorder'][0], opacitys,
                                        {"spatial": spatial * len(times['preorder'][0])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '根节点', 'text': '根节点',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Root Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                            {
                                'layerName': '左子树注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['preorder'][1], opacitys,
                                        {"spatial": spatial * len(times['preorder'][1])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '左子树', 'text': '左子树',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Left Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                            {
                                'layerName': '右子树注解',
                                'width': QUE_ELEM_WIDTH * 3, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH * 2, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['preorder'][2], opacitys,
                                        {"spatial": spatial * len(times['preorder'][2])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '右子树', 'text': '右子树',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH * 3 / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Right Down 3x/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH * 3 / 2, 0],
                                    }
                                ],
                            },
                        ]
                    },
                    {
                        'layerName': '数据.Left',
                        'width': QUE_ELEM_WIDTH * 2 + STROKE_ADD, 'height': QUE_ELEM_WIDTH + STROKE_ADD + annotation_height,
                        'Anchor Point': 'LEFT_TOP', 'Position': [0, 150],
                        'startTime': start_time, 'duration': duration,
                        'keyframes': {
                            'Transform.Opacity': [
                                times['que1']['Opacity'], opacitys,
                                {"spatial": spatial * len(times['que1']['Opacity'])}
                            ]
                        },
                        'precomps': [
                            {
                                'layerName': '队列.左边', 'type': 'QUEUE', 'traverse': 'inorder',
                                'width': QUE_ELEM_WIDTH * 2 + STROKE_ADD, 'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                                'Anchor Point': 'LEFT_TOP', 'Position': [0, 0],
                                'startTime': start_time, 'duration': duration,
                                'unit': QUE_UNIT,
                                'elems': [
                                    {
                                        'key': 3, 'Color': COLORS['queue']['fillColor']['root'],
                                    },
                                    {
                                        'key': 9, 'Color': COLORS['queue']['fillColor']['left'],
                                    },
                                ],
                            },
                        ],
                        'misc': [
                            {
                                'layerName': '根节点注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [0, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'texts': [
                                    {
                                        'layerName': '根节点', 'text': '根节点',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Root Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                            {
                                'layerName': '左子树注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'texts': [
                                    {
                                        'layerName': '左子树', 'text': '左子树',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Left Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                        ],
                    },
                    {
                        'layerName': '数据.Right',
                        'width': QUE_ELEM_WIDTH * 3 + STROKE_ADD, 'height': QUE_ELEM_WIDTH + STROKE_ADD + annotation_height,
                        'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH * 2, 150],
                        'startTime': start_time, 'duration': duration,
                        'keyframes': {
                            'Transform.Opacity': [
                                times['que1']['Opacity'], opacitys,
                                {"spatial": spatial * len(times['que1']['Opacity'])}
                            ],
                            'Transform.Position': [
                                times['que1']['Position'], [[QUE_ELEM_WIDTH * 2, 150], [QUE_ELEM_WIDTH * 2, 150], [QUE_ELEM_WIDTH * 5, 150]],
                            ],
                        },
                        'precomps': [
                            {
                                'layerName': '队列.右边', 'type': 'QUEUE', 'traverse': 'inorder',
                                'width': QUE_ELEM_WIDTH * 3 + STROKE_ADD, 'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                                'Anchor Point': 'LEFT_TOP', 'Position': [0, 0],
                                'startTime': start_time, 'duration': duration,
                                'unit': QUE_UNIT,
                                'elems': [
                                    {
                                        'key': 20,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['preorder'][3],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['root'])],
                                                {"spatial": spatial * len(times['preorder'][3])}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 15,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['preorder'][4],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['left'])],
                                                {"spatial": spatial * len(times['preorder'][4])}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 7,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['preorder'][5],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                                {"spatial": spatial * len(times['preorder'][5])}
                                            ]
                                        }
                                    }
                                ],
                            },
                        ],
                        'misc': [
                            {
                                'layerName': '根节点注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [0, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['preorder'][3], opacitys,
                                        {"spatial": spatial * len(times['preorder'][3])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '根节点', 'text': '根节点',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Root Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                            {
                                'layerName': '左子树注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['preorder'][4], opacitys,
                                        {"spatial": spatial * len(times['preorder'][4])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '左子树', 'text': '左子树',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Left Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                            {
                                'layerName': '右子树注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH * 2, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['preorder'][5], opacitys,
                                        {"spatial": spatial * len(times['preorder'][5])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '右子树', 'text': '右子树',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH/ 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Right Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                        ],
                    }
                ],
            },
            {
                'layerName': f'{prefix}.中序数据分布',
                'width': 1020, 'height': 300,
                'Anchor Point': 'LEFT_TOP', 'Position': [830, 600],
                'startTime': start_time, 'duration': duration,
                'texts': [
                    {
                        'layerName': '前序遍历注解', 'text': '遍历结果按照[左子树|根节点|右子树]排序\n需要先定位根节点，才能确定左子树和右子树',
                        'font': FONTS['cn'], 'justification': 'LEFT_JUSTIFY',
                        'Anchor Point': 'LEFT_TOP', 'Position': [0, 0],
                        # 'startTime': start_time, 'duration': duration,
                    },
                ],
                'misc': [
                    {
                        'layerName': '数据.All',
                        'width': QUE_ELEM_WIDTH * 5 + STROKE_ADD, 'height': QUE_ELEM_WIDTH + STROKE_ADD + annotation_height,
                        'Anchor Point': 'LEFT_TOP', 'Position': [0, 150],
                        'startTime': start_time, 'duration': duration,
                        'keyframes': {
                            'Transform.Opacity': [
                                times['que2']['Opacity'], opacitys_inv,
                                {"spatial": spatial * len(times['que2']['Opacity'])}
                            ]
                        },
                        'precomps': [
                            {
                                'layerName': '队列', 'type': 'QUEUE', 'traverse': 'preorder',
                                'width': QUE_ELEM_WIDTH * 5 + STROKE_ADD, 'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                                'Position': [0, 0], 'Anchor Point': 'LEFT_TOP',
                                # 'elems': [[3, '#0573E1'], [9, '#FADED8'], [20, '#CEF2ED'], [15, '#CEF2ED'], [7, '#CEF2ED']],
                                'startTime': start_time, 'duration': duration,
                                'unit': QUE_UNIT,
                                'elems': [
                                    {
                                        'key': 9,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['inorder'][1],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['left'])],
                                                {"spatial": spatial * len(times['inorder'][1])}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 3,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['inorder'][0],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['root'])],
                                                {"spatial": spatial * len(times['inorder'][0])}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 15,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['inorder'][2],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                                {"spatial": spatial * len(times['inorder'][2])}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 20,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['inorder'][2],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                                {"spatial": spatial * len(times['inorder'][2])}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 7,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['inorder'][2],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                                {"spatial": spatial * len(times['inorder'][2])}
                                            ]
                                        }
                                    }
                                ],
                                # 'effects': {'ADBE Drop Shadow': {}},
                            },
                        ],
                        'misc': [
                            {
                                'layerName': '根节点注解',
                                'width': QUE_ELEM_WIDTH, 'height': annotation_height,
                                'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['inorder'][0], opacitys,
                                        {"spatial": spatial * len(times['inorder'][0])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '根节点', 'text': '根节点',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Root Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                            {
                                'layerName': '左子树注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [0, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['inorder'][1], opacitys,
                                        {"spatial": spatial * len(times['inorder'][1])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '左子树', 'text': '左子树',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Left Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                            {
                                'layerName': '右子树注解',
                                'width': QUE_ELEM_WIDTH * 3, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH * 2, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['inorder'][2], opacitys,
                                        {"spatial": spatial * len(times['inorder'][2])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '右子树', 'text': '右子树',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH * 3 / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Right Down 3x/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH * 3 / 2, 0],
                                    }
                                ],
                            },
                        ]
                    },
                    {
                        'layerName': '数据.Left',
                        'width': QUE_ELEM_WIDTH * 2 + STROKE_ADD, 'height': QUE_ELEM_WIDTH + STROKE_ADD + annotation_height,
                        'Anchor Point': 'LEFT_TOP', 'Position': [0, 150],
                        'startTime': start_time, 'duration': duration,
                        'keyframes': {
                            'Transform.Opacity': [
                                times['que2']['Opacity'], opacitys,
                                {"spatial": spatial * len(times['que2']['Opacity'])}
                            ],
                        },
                        'precomps': [
                            {
                                'layerName': '队列.左边', 'type': 'QUEUE', 'traverse': 'inorder',
                                'width': QUE_ELEM_WIDTH * 2 + STROKE_ADD, 'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                                'Anchor Point': 'LEFT_TOP', 'Position': [0, 0],
                                'startTime': start_time, 'duration': duration,
                                'unit': QUE_UNIT,
                                'elems': [
                                    {
                                        'key': 9, 'Color': COLORS['queue']['fillColor']['left'],
                                    },
                                    {
                                        'key': 3, 'Color': COLORS['queue']['fillColor']['root'],
                                    },
                                ],
                                # 'effects': {'ADBE Drop Shadow': {}},
                            },
                        ],
                        'misc': [
                            {
                                'layerName': '根节点注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [0, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'texts': [
                                    {
                                        'layerName': '根节点', 'text': '根节点',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Root Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                            {
                                'layerName': '左子树注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'texts': [
                                    {
                                        'layerName': '左子树', 'text': '左子树',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Left Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                        ],
                    },
                    {
                        'layerName': '数据.Right',
                        'width': QUE_ELEM_WIDTH * 3 + STROKE_ADD, 'height': QUE_ELEM_WIDTH + STROKE_ADD + annotation_height,
                        'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH * 2, 150],
                        'startTime': start_time, 'duration': duration,
                        'keyframes': {
                            'Transform.Opacity': [
                                times['que2']['Opacity'], opacitys,
                                {"spatial": spatial * len(times['que2']['Opacity'])}
                            ],
                            'Transform.Position': [
                                times['que2']['Position'], [[QUE_ELEM_WIDTH * 2, 150], [QUE_ELEM_WIDTH * 2, 150], [QUE_ELEM_WIDTH * 5, 150]],
                            ],
                        },
                        'precomps': [
                            {
                                'layerName': '队列.右边', 'type': 'QUEUE', 'traverse': 'inorder',
                                'width': QUE_ELEM_WIDTH * 3 + STROKE_ADD, 'height': QUE_ELEM_HEIGHT + STROKE_ADD,
                                'Anchor Point': 'LEFT_TOP', 'Position': [0, 0],
                                'startTime': start_time, 'duration': duration,
                                'unit': QUE_UNIT,
                                'elems': [
                                    {
                                        'key': 15,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['inorder'][4],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['left'])],
                                                {"spatial": spatial*(len(times['inorder'][3]))}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 20,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['inorder'][3],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['root'])],
                                                {"spatial": spatial*(len(times['inorder'][3]))}
                                            ]
                                        }
                                    },
                                    {
                                        'key': 7,
                                        'keyframes': {
                                            'Contents.Group 1.Contents.Fill 1.Color': [
                                                times['inorder'][5],
                                                [hex_to_rgb1(COLORS['queue']['fillColor']['default']),
                                                 hex_to_rgb1(COLORS['queue']['fillColor']['right'])],
                                                {"spatial": spatial*(len(times['inorder'][5]))}
                                            ]
                                        }
                                    }
                                ],
                                # 'effects': {'ADBE Drop Shadow': {}},
                            },
                        ],
                        'misc': [
                            {
                                'layerName': '根节点注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['inorder'][3], opacitys,
                                        {"spatial": spatial * len(times['inorder'][3])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '根节点', 'text': '根节点',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Root Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                            {
                                'layerName': '左子树注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [0, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['inorder'][4], opacitys,
                                        {"spatial": spatial * len(times['inorder'][4])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '左子树', 'text': '左子树',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Left Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                            {
                                'layerName': '右子树注解',
                                'width': QUE_ELEM_WIDTH, 'height': 50,
                                'Anchor Point': 'LEFT_TOP', 'Position': [QUE_ELEM_WIDTH * 2, QUE_ELEM_HEIGHT],
                                'startTime': start_time, 'duration': duration,
                                'keyframes': {
                                    'Transform.Opacity': [
                                        times['inorder'][5], opacitys,
                                        {"spatial": spatial * len(times['inorder'][5])}
                                    ]
                                },
                                'texts': [
                                    {
                                        'layerName': '右子树', 'text': '右子树',
                                        'fontSize': 15,
                                        'Position': [QUE_ELEM_WIDTH / 2, 35],
                                    }
                                ],
                                'vectors': [
                                    {
                                        'name': 'Tree Length Right Down/Elements.ai',
                                        'Anchor Point': 'TOP', 'Position': [QUE_ELEM_WIDTH / 2, 0],
                                    }
                                ],
                            },
                        ],
                    }
                ],
            },
        ],
        'precomps': [
            {
                'layerName': f'{prefix}.二叉树', 'type': 'BINARY_TREE', 'width': 500, 'height': 500,
                'startTime': start_time, 'duration': duration, 'Position': [435, 490],
                'elems': [
                    # {'key': 3, 'Color': COLORS['tree']['fillColor']['root']},
                    # {'key': 9, 'Color': COLORS['tree']['fillColor']['left']},
                    # {'key': 20, 'Color': COLORS['tree']['fillColor']['right']},
                    # {'key': None}, {'key': None},
                    # {'key': 15, 'Color': COLORS['tree']['fillColor']['right']},
                    # {'key': 7, 'Color': COLORS['tree']['fillColor']['right']}
                    {'key': 3},
                    {'key': 9},
                    {'key': 20},
                    {'key': None}, {'key': None},
                    {'key': 15},
                    {'key': 7}
                ],
                'animation': 'false',
                'node': {
                    'shape': {'name': f'Node Shape {VECTORS["node"]["shape"]}/Elements.ai',
                              'Scale': [80, 80, 80]},
                    'selected': {
                        'pathGroup': {'type': 'Ellipse', 'Size': [100, 100]},
                        "Fill": {"Color": hex_to_rgb1("#FFFFFF")},
                    },
                },
                'edge': {
                    'shape': {'name': f'Edge {VECTORS["edge"]["shape"]}/Elements.ai', 'Anchor Point': 'TOP',
                              'Scale': [80, 80, 80],
                              'Rotation': 30},
                },
                'Masks': conf_shot_0['4'],
                'keyframes': {
                    'Masks.Mask 1.Mask Opacity': [
                        times['tree'][0], opacitys,
                        {"spatial": spatial*len(times['tree'][0])}
                    ],
                    'Masks.Mask 2.Mask Opacity': [
                        times['tree'][1], opacitys,
                        {"spatial": spatial * len(times['tree'][1])}
                    ],
                    'Masks.Mask 3.Mask Opacity': [
                        times['tree'][2], opacitys,
                        {"spatial": spatial * len(times['tree'][2])}
                    ],
                    'Masks.Mask 4.Mask Opacity': [
                        times['tree'][3], opacitys,
                        {"spatial": spatial * len(times['tree'][3])}
                    ],
                    'Masks.Mask 5.Mask Opacity': [
                        times['tree'][4], opacitys,
                        {"spatial": spatial * len(times['tree'][4])}
                    ],
                }
                # '3D': 'true'
            }
        ],
        'end_time': end_time,
    }
    return conf

def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
