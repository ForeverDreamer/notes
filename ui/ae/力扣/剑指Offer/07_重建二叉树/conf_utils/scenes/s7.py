from ae.constants.share import *
from .transcript import scenes
from ae.utils.py.color import hex_to_rgb1

name = 's7'


def shot_0(start_time):
    sn = 0
    prefix = f'{name}.{sn}'
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time + i * SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]+SUBTITLES_INTERVAL
    QUE_ELEM_WIDTH = 40
    QUE_ELEM_HEIGHT = 40
    QUE_UNIT['pathGroup']['Size'] = [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT]
    stroke_add = QUE_UNIT['Stroke']['Stroke Width'] * 4
    duration = end_time - start_time
    temporal = [[[0, 0.1], [0, 0.1], [200, 100]], [[0, 75], [0, 75], [0, 0.1]]]

    # 工作量大或相互关联的配置提到前边统一填写，避免滚轮滚上滚下到处找，头都晕了~
    keyframes = {
        'vars': {
            'idx_pl': {
                'Opacity': [
                    [0, 4, 9],
                    [0, 100, 0],
                    {"spatial": SPATIAL_HOLD * 3}
                ],
            },
            'idx_pr': {
                'Opacity': [
                    [0, 5, 9],
                    [0, 100, 0],
                    {"spatial": SPATIAL_HOLD * 3}
                ],
            },
            'idx_il': {
                'Opacity': [
                    [0, 6, 9],
                    [0, 100, 0],
                    {"spatial": SPATIAL_HOLD * 3}
                ],
            },
            'idx_ir': {
                'Opacity': [
                    [0, 7, 9],
                    [0, 100, 0],
                    {"spatial": SPATIAL_HOLD * 3}
                ],
            },
            'idx_dic': {
                'Opacity': [
                    [0, 8],
                    [0, 100],
                    {"spatial": SPATIAL_HOLD * 2}
                ],
            },
            'idx_pl.idx_pr.idx_il.idx_ir': {
                'Opacity': [
                    [0, 9],
                    [0, 100],
                    {"spatial": SPATIAL_HOLD * 2}
                ],
                'Source Text': [
                    [0, 9, 15],
                    [
                        'idx_pl: 0  idx_pr: 4  idx_il: 0  idx_ir: 4', 'idx_pl: 0  idx_pr: 4  idx_il: 0  idx_ir: 4',
                        'idx_pl: 1  idx_pr: 1  idx_il: 0  idx_ir: 0'
                    ],
                    # {"spatial": SPATIAL_HOLD * 3}
                ]
            },
            'idx_p_root': {
                'Opacity': [
                    [0, 11, 15],
                    [0, 100, 0],
                    {"spatial": SPATIAL_HOLD * 3}
                ],
            },
            'idx_i_root': {
                'Opacity': [
                    [0, 12, 15],
                    [0, 100, 0],
                    {"spatial": SPATIAL_HOLD * 3}
                ],
            },
            'root': {
                'Opacity': [
                    [0, 13, 15],
                    [0, 100, 0],
                    {"spatial": SPATIAL_HOLD * 3}
                ],
            },
            'size_left': {
                'Opacity': [
                    [0, 14, 15],
                    [0, 100, 0],
                    {"spatial": SPATIAL_HOLD * 3}
                ],
            },
        },
        'preorder': {
            'root': {
                'Opacity': [
                    [0, 11, 15, 17, 21, 23],
                    [0, 100, 0, 100, 0, 100],
                    {"spatial": SPATIAL_HOLD * 6}
                ],
                'Position': [
                    [0, 11, 17],
                    [
                        [108, 103.5], [108, 103.5], [148, 103.5]
                    ],
                    {"spatial": SPATIAL_HOLD * 3}
                    # {"spatial": [{"type": 'HOLD'}] * 3 + [{"type": 'LINEAR'}]}
                ],
            },
            'left': {
                'Opacity': [
                    [0, 9],
                    [0, 100],
                    {"spatial": SPATIAL_HOLD * 2}
                ],
                'Position': [
                    [9, 15, 15.3, 21, 21.3, 23, 23.3, 24, 24.5, 26, 26.5],
                    [
                        [108, 52.5], [108, 52.5], [148, 52.5], [148, 52.5], [188, 52.5], [188, 52.5],
                        [148, 52.5], [148, 52.5], [188, 52.5], [188, 52.5], [148, 52.5]
                    ],
                ]
            },
            'right': {
                'Opacity': [
                    [0, 9],
                    [0, 100],
                    {"spatial": SPATIAL_HOLD * 2}
                ],
                'Position': [
                    [8, 15, 15.3],
                    [
                        [265, 52.5], [265, 52.5], [148, 52.5]
                    ]
                ]
            },
        },
        'inorder': {
            'root': {
                'Opacity': [
                    [0, 12],
                    [0, 100],
                    {"spatial": [{"type": 'HOLD'}] * 2}
                ],
                'Position':  [
                    [0, 16, 26, 26.5],
                    [[108, 103.5], [148, 103.5], [148, 103.5], [108, 103.5]],
                    # {"spatial": [{"type": 'HOLD'}] * 3 + [{"type": 'LINEAR'}]}
                ],
            },
            'left': {
                'Opacity': [
                    [0, 9],
                    [0, 100],
                    {"spatial": SPATIAL_HOLD * 2}
                ],
                'Position':[
                    [9, 14, 14.5, 20, 20.5, 22, 22.5, 24, 24.5, 26, 26.5],
                    [
                        [108, 52.5], [108, 52.5], [148, 52.5], [148, 52.5], [188, 52.5], [188, 52.5],
                        [148, 52.5], [148, 52.5], [188, 52.5], [188, 52.5], [148, 52.5]
                    ],
                ]
            },
            'right': {
                'Opacity': [
                    [0, 9],
                    [0, 100],
                    {"spatial": SPATIAL_HOLD * 2}
                ],
                'Position': [[8, 14, 14.5], [[265, 52.5], [265, 52.5], [148, 52.5]]]
            },
        },
        'tree': {

        }
    }

    conf = {
        'subtitles': subtitles,
        # 'annotations': [
        #     {
        #         'name': 'idx_dic', 'text': 'idx_dic = {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}',
        #         'Position': [1610, 110], 'fontSize': 25,
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        # ],
        'precomps': [
            {
                'layerName': f'{prefix}.二叉树', 'type': 'BINARY_TREE', 'width': 500, 'height': 500,
                'startTime': start_time, 'duration': duration, 'Anchor Point': 'LEFT_TOP', 'Position': [50, 250],
                'elems': [
                    {
                        'key': 3,
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, 12, 12.5],
                                [0, 0, 100],
                                # {"temporal": temporal}
                            ]
                        }
                    },
                    {
                        'key': 9,
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, 18, 18.5],
                                [0, 0, 100],
                                # {"temporal": temporal}
                            ]
                        }
                    },
                    {
                        'key': 20,
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, 34, 34.5],
                                [0, 0, 100],
                                # {"temporal": temporal}
                            ]
                        }
                    },
                    {'key': None}, {'key': None},
                    {
                        'key': 15,
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, 40, 40.5],
                                [0, 0, 100],
                                # {"temporal": temporal}
                            ]
                        }
                    },
                    {
                        'key': 7,
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, 56, 56.5],
                                [0, 0, 100],
                                # {"temporal": temporal}
                            ]
                        }
                    }
                ],
                'animation': 'false',
                'node': {
                    'shape': {'name': 'Node Shape Black/Elements.ai', 'Scale': [80, 80, 80]},
                },
                'edge': {
                    'shape': {'name': 'Edge Black/Elements.ai', 'Anchor Point': 'TOP', 'Scale': [80, 80, 80],
                              'Rotation': 30},
                },
                # '3D': 'true'
                'keyframes': {

                }
            }
        ],
        'misc': [
            {
                'layerName': f'{prefix}.队列.前序', 'width': 300, 'height': 150, 'Position': [771.5, 135.5],
                'startTime': start_time, 'duration': duration,
                'keyframes': {
                    'Transform.Opacity': [[0, 1], [0, 100], {"spatial": [{"type": 'HOLD'}]}],
                },
                'texts': [
                    {
                        'name': '名字', 'text': '前序',
                        'Anchor Point': 'LEFT', 'Position': [0, 75], 'font': FONTS['cn'], 'fontSize': 40,
                    },
                ],
                'precomps': [
                    {
                        'layerName': '数据', 'type': 'QUEUE', 'Position': [86.5, 56], 'Anchor Point': 'LEFT_TOP',
                        'elems': [{'key': 3}, {'key': 9}, {'key': 20}, {'key': 15}, {'key': 7}],
                        'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5, 'height': QUE_ELEM_HEIGHT + stroke_add,
                        'unit': QUE_UNIT, 'duration': duration,
                    },
                ],
                'misc': [
                    {
                        'layerName': '根节点.选中框', 'width': 150, 'height': 100, 'Position': [108, 103.5],
                        'duration': duration,
                        'keyframes': keyframes['preorder']['root'],
                        'texts': [
                            {
                                'name': 'idx_p_root', 'text': 'idx_p_root',
                                'fillColor': COLORS['queue']['fillColor']['root'],
                                'Position': [75, 80], 'fontSize': 25,
                            },
                        ],
                        'vectors': [
                            {
                                'name': 'Queue Code Selected Root/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 37],
                            }
                        ],
                    },
                    {
                        'layerName': '左边界.选中框', 'width': 150, 'height': 100, 'Position': [148, 52.5],
                        'duration': duration,
                        'keyframes': keyframes['preorder']['left'],
                        'texts': [
                            {
                                'name': 'idx_pl', 'text': 'idx_pl', 'fillColor': COLORS['queue']['fillColor']['left'],
                                'Position': [75, 15], 'fontSize': 25,
                            },
                        ],
                        'vectors': [
                            {
                                'name': 'Queue Code Selected Left/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 100 - 37],
                            }
                        ],
                    },
                    {
                        'layerName': '右边界.选中框', 'width': 150, 'height': 100, 'Position': [265, 52.5],
                        'duration': duration,
                        'keyframes': keyframes['preorder']['right'],
                        'texts': [
                            {
                                'name': 'idx_pr', 'text': 'idx_pr', 'fillColor': COLORS['queue']['fillColor']['right'],
                                'Position': [75, 15], 'fontSize': 25,
                            },
                        ],
                        'vectors': [
                            {
                                'name': 'Queue Code Selected Right/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 100 - 37],
                            }
                        ],
                    }
                ],
            },
            {
                'layerName': f'{prefix}.队列.中序', 'width': 300, 'height': 150, 'Position': [771.5, 316],
                'startTime': start_time, 'duration': duration,
                'keyframes': {
                    'Transform.Opacity': [[0, 1], [0, 100], {"spatial": [{"type": 'HOLD'}] * 2}],
                },
                'texts': [
                    {
                        'name': '名字', 'text': '中序',
                        'Anchor Point': 'LEFT', 'Position': [0, 75], 'font': FONTS['cn'], 'fontSize': 40,
                    },
                ],
                'precomps': [
                    {
                        'layerName': '数据', 'type': 'QUEUE', 'Position': [86.5, 56], 'Anchor Point': 'LEFT_TOP',
                        'elems': [{'key': 9}, {'key': 3}, {'key': 15}, {'key': 20}, {'key': 7}],
                        'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5, 'height': QUE_ELEM_HEIGHT + stroke_add,
                        'duration': duration,
                        'unit': QUE_UNIT,
                    },
                ],
                'misc': [
                    {
                        'layerName': '根节点.选中框', 'Position': [108, 103.5],
                        'width': 150, 'height': 100, 'duration': duration,
                        'keyframes': {
                            'Transform.Opacity': keyframes['inorder']['root']['Opacity'],
                            'Transform.Position': keyframes['inorder']['root']['Position'],
                        },
                        'texts': [
                            {
                                'name': 'idx_p_root', 'text': 'idx_p_root',
                                'fillColor': COLORS['queue']['fillColor']['root'],
                                'Position': [75, 80], 'fontSize': 25,
                                'span': {'inPoint': start_time, 'outPoint': end_time},
                            },
                        ],
                        'vectors': [
                            {
                                'name': 'Queue Code Selected Root/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 37],
                            }
                        ],
                    },
                    {
                        'layerName': '左边界.选中框', 'Position': [148, 52.5],
                        'width': 150, 'height': 100, 'duration': duration,
                        'keyframes': {
                            'Transform.Opacity': keyframes['inorder']['left']['Opacity'],
                            'Transform.Position': keyframes['inorder']['left']['Position'],
                        },
                        'texts': [
                            {
                                'name': 'idx_pl', 'text': 'idx_pl', 'fillColor': COLORS['queue']['fillColor']['left'],
                                'Position': [75, 15], 'fontSize': 25,
                            },
                        ],
                        'vectors': [
                            {
                                'name': 'Queue Code Selected Left/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 100 - 37],
                                'startTime': start_time,
                            }
                        ],
                    },
                    {
                        'layerName': '右边界.选中框', 'Position': [265, 52.5],
                        'width': 150, 'height': 100, 'duration': duration,
                        'keyframes': {
                            'Transform.Opacity': keyframes['inorder']['right']['Opacity'],
                            'Transform.Position': keyframes['inorder']['right']['Position'],
                        },
                        'texts': [
                            {
                                'name': 'idx_pr', 'text': 'idx_pr', 'fillColor': COLORS['queue']['fillColor']['right'],
                                'Position': [75, 15], 'fontSize': 25,
                            },
                        ],
                        'vectors': [
                            {
                                'name': 'Queue Code Selected Right/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 100 - 37],
                            }
                        ],
                    }
                ],
            },
            {
                'layerName': f'{prefix}.代码', 'width': 1419, 'height': 934,
                'Anchor Point': 'LEFT_TOP', 'Position': [595, 45],
                'startTime': start_time, 'duration': duration,
                'texts': [
                    {
                        'layerName': 'idx_dic', 'text': 'idx_dic = {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}',
                        'Position': [215, 484], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        'keyframes': keyframes['vars']['idx_dic']
                    },
                    {
                        'layerName': 'idx_pl', 'text': 'idx_pl: 0',
                        'Position': [644, 660], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        'keyframes': keyframes['vars']['idx_pl']
                    },
                    {
                        'layerName': 'idx_pr', 'text': 'idx_pr: 4',
                        'Position': [810, 691], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        'keyframes': keyframes['vars']['idx_pr']
                    },
                    {
                        'layerName': 'idx_il', 'text': 'idx_il: 0',
                        'Position': [631, 722], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        'keyframes': keyframes['vars']['idx_il']
                    },
                    {
                        'layerName': 'idx_ir', 'text': 'idx_ir: 4',
                        'Position': [781, 751], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        'keyframes': keyframes['vars']['idx_ir']
                    },
                    {
                        'layerName': 'idx_pl.idx_pr.idx_il.idx_ir',
                        'text': 'idx_pl: 0  idx_pr: 4  idx_il: 0  idx_ir: 4',
                        'Position': [1111, 270], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        'keyframes': keyframes['vars']['idx_pl.idx_pr.idx_il.idx_ir']
                    },
                    {
                        'layerName': 'idx_p_root', 'text': 'idx_p_root: 0',
                        'Position': [818, 390], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        'keyframes': keyframes['vars']['idx_p_root']
                    },
                    {
                        'layerName': 'idx_i_root', 'text': 'idx_i_root: 1',
                        'Position': [1057, 420], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        'keyframes': keyframes['vars']['idx_i_root']
                    },
                    {
                        'layerName': 'root', 'text': 'root: 3',
                        'Position': [995, 447], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        'keyframes': keyframes['vars']['root']
                    },
                    {
                        'layerName': 'size_left', 'text': 'size_left: 1',
                        'Position': [900, 480], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        'keyframes': keyframes['vars']['size_left']
                    },
                ],
                'shapes': [
                    {
                        'layerName': 'idx_dic.选中框',
                        'Position': [196.5, 482.5],
                        # 'startTime': start_time,
                        # 'span': {'inPoint': start_time, 'outPoint': end_time + 3},
                        'pathGroup': {'type': 'Rect', 'Size': [55, 30]},
                        'Stroke': {'Stroke Width': 3, 'Color': hex_to_rgb1('#FF0000')},
                        'keyframes': {
                        }
                    },
                ],
                'precomps': [
                    {
                        'layerName': '函数调用栈', 'type': 'STACK', 'Position': [8, 618], 'Anchor Point': 'LEFT_TOP',
                        'width': STACK_ELEM_WIDTH + stroke_add, 'height': STACK_ELEM_HEIGHT * 6 + stroke_add,
                        'duration': duration,
                        'startTime': start_time,
                        'unit': STACK_UNIT,
                        'elems': [
                            {
                                'key': '<module>',
                                'keyframes': {
                                    "Transform.Opacity": [
                                        [0, 1],
                                        [0, 100],
                                        {'spatial': [{"type": 'HOLD'}] * 2}
                                    ]
                                }
                            },
                            {
                                'key': 'buildTree( )',
                                'keyframes': {
                                    "Transform.Opacity": [
                                        [0, 2],
                                        [0, 100],
                                        {'spatial': [{"type": 'HOLD'}] * 2}
                                    ]
                                }
                            },
                            {
                                'key': 'rebuild( )',
                                'keyframes': {
                                    "Transform.Opacity": [
                                        [0, 9],
                                        [0, 100],
                                        {'spatial': [{"type": 'HOLD'}] * 2}
                                    ]
                                }
                            }, {
                                'key': 'rebuild( )',
                                'keyframes': {
                                    "Transform.Opacity": [
                                        [0, 15],
                                        [0, 100],
                                        {'spatial': [{"type": 'HOLD'}] * 2}
                                    ]
                                }
                            },
                            {
                                'key': 'rebuild( )',
                                'keyframes': {
                                    "Transform.Opacity": [
                                        [0, 21, 23, 23.1, 25, 25.1, 27, 27.1],
                                        [0, 100, 100, 0, 0, 100, 100, 0],
                                        {'spatial': [{"type": 'HOLD'}] * 8}
                                    ]
                                }
                            },
                            {
                                'key': 'rebuild( )',
                                'keyframes': {
                                    "Transform.Opacity": [
                                        [0, 100],
                                        [0, 100],
                                        {'spatial': [{"type": 'HOLD'}] * 2}
                                    ]
                                }
                            }
                        ],
                    },
                ],
                'codes': {
                    'layerName': '代码', 'Position': [370, 0], 'duration': duration, 'width': 1200, 'height': 934,
                    'widthLine': 1200, 'heightLine': 30, 'font': 'MicrosoftSansSerif', 'fontSize': FONT_SIZES['code'],
                    'startTime': start_time, 'Anchor Point': 'LEFT_TOP',
                    'currentLine': {
                        'layerName': 'currentLine',
                        'Anchor Point': 'LEFT',
                        # 'Position': [694, 540],
                        # 'startTime': start_time,
                        # 'span': {'inPoint': start_time, 'outPoint': end_time + 3},
                        'pathGroup': {'type': 'Rect', 'Size': [1200, 30]},
                        'Fill': {'Color': hex_to_rgb1(CODE_COLORS['currentLine'])},
                        'keyframes': {
                            'Transform.Position': [
                                None,
                                [
                                    18, 2, 12, 13, 14, 15, 16, 17, 3, 5, 6, 7, 8, 9, 3, 5, 6, 7, 8, 9, 3, 4, 9, 10, 3,
                                    4, 10, 11,
                                    9, 10, 3, 5, 6, 7, 8, 9, 3, 5, 6, 7, 8, 9, 3, 4, 9, 10, 3, 4, 10, 11, 9, 10, 3, 5,
                                    6, 7, 8,
                                    9, 3, 4, 9, 10, 3, 4, 10, 11, 10, 11, 10, 11, 17, 18
                                ],
                                {'spatial': [{"type": 'HOLD'}] * 72}
                            ],
                            "Transform.Opacity": [
                                [0, 1],
                                [0, 100],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    'lines': [
                        [0, {'text': 'class', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
                         {'text': 'TreeNode:'}],
                        [
                            1,
                            {'text': 'def', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
                            {'text': '__init__', 'fillColor': CODE_COLORS['dunder']}, {'text': '('},
                            {'text': 'self', 'fillColor': CODE_COLORS['self']}, {'text': ', values):'},
                        ],
                        [
                            2,
                            {'text': 'self', 'fillColor': CODE_COLORS['self']}, {'text': '.key = key'},
                        ],
                        [
                            2,
                            {'text': 'self', 'fillColor': CODE_COLORS['self']}, {'text': '.left ='}, {'text': ' '},
                            {'text': 'None', 'fillColor': CODE_COLORS['keyword']},
                        ],
                        [
                            2,
                            {'text': 'self', 'fillColor': CODE_COLORS['self']}, {'text': '.right ='}, {'text': ' '},
                            {'text': 'None', 'fillColor': CODE_COLORS['keyword']},
                        ],
                        [],
                        [0, {'text': 'class', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
                         {'text': 'Solution:'}],
                        [
                            1,
                            {'text': 'def', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
                            {'text': 'buildTree', 'fillColor': CODE_COLORS['func']}, {'text': '('},
                            {'text': 'self', 'fillColor': CODE_COLORS['self']}, {'text': ', preorder, inorder):'},
                        ],
                        [
                            2,
                            {'text': 'def', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
                            {'text': 'rebuild', 'fillColor': CODE_COLORS['func']},
                            {'text': '(idx_pl, idx_pr, idx_il, idx_ir):'},
                        ],
                        [
                            3,
                            {'text': 'if', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
                            {'text': 'idx_pl > idx_pr:'},
                        ],
                        [
                            4,
                            {'text': 'return None', 'fillColor': CODE_COLORS['keyword']},
                        ],
                        [],
                        [
                            3,
                            {'text': 'idx_p_root = idx_pl'},
                        ],
                        [
                            3,
                            {'text': 'idx_i_root = idx_dic[preorder[idx_p_root]]'},
                        ],
                        [
                            3,
                            {'text': 'root = TreeNode(preorder[idx_p_root])'},
                        ],
                        [
                            3,
                            {'text': 'size_left = idx_i_root - idx_il'},
                        ],
                        [],
                        [
                            3,
                            {'text': 'root.left = rebuild(idx_pl +'}, {'text': ' '},
                            {'text': '1', 'fillColor': CODE_COLORS['number']},
                            {'text': ', idx_pl + size_left, idx_il, idx_i_root -'},
                            {'text': ' '}, {'text': '1', 'fillColor': CODE_COLORS['number']}, {'text': ')'},
                        ],
                        [
                            3,
                            {'text': 'root.right = rebuild(idx_pl + size_left +'}, {'text': ' '},
                            {'text': '1', 'fillColor': CODE_COLORS['number']},
                            {'text': ', idx_pr, idx_i_root +'}, {'text': ' '},
                            {'text': '1', 'fillColor': CODE_COLORS['number']},
                            {'text': ', idx_ir)'},
                        ],
                        [3, {'text': 'return', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'root'}],
                        [],
                        [2, {'text': 'idx_pl ='}, {'text': ' '}, {'text': '0', 'fillColor': CODE_COLORS['number']}],
                        [
                            2,
                            {'text': 'idx_pr ='}, {'text': ' '}, {'text': 'len', 'fillColor': CODE_COLORS['builtin']},
                            {'text': '(preorder) -'}, {'text': ' '}, {'text': '1', 'fillColor': CODE_COLORS['number']},
                        ],
                        [2, {'text': 'idx_il ='}, {'text': ' '}, {'text': '0', 'fillColor': CODE_COLORS['number']}],
                        [
                            2,
                            {'text': 'idx_ir ='}, {'text': ' '}, {'text': 'len', 'fillColor': CODE_COLORS['builtin']},
                            {'text': '(inorder) -'}, {'text': ' '}, {'text': '1', 'fillColor': CODE_COLORS['number']},
                        ],
                        [],
                        [
                            2,
                            {'text': 'idx_dic = {element: i'}, {'text': ' '},
                            {'text': 'for', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '}, {'text': ' i, element'}, {'text': ' '},
                            {'text': 'in', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
                            {'text': 'enumerate', 'fillColor': CODE_COLORS['builtin']},
                            {'text': '(inorder)'}
                        ],
                        [
                            2,
                            {'text': 'return', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
                            {'text': 'rebuild(idx_pl, idx_pr, idx_il, idx_ir)'}
                        ],
                        [],
                        [
                            0,
                            {'text': 'print', 'fillColor': CODE_COLORS['builtin']}, {'text': '(Solution().buildTree('},
                            {'text': 'preorder', 'fillColor': CODE_COLORS['kwargs']}, {'text': '=['},
                            {'text': '3', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '},
                            {'text': '9', 'fillColor': CODE_COLORS['number']},
                            {'text': ','}, {'text': ' '}, {'text': '20', 'fillColor': CODE_COLORS['number']},
                            {'text': ','}, {'text': ' '},
                            {'text': '15', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '},
                            {'text': '7', 'fillColor': CODE_COLORS['number']},
                            {'text': '],'}, {'text': ' '},
                            {'text': 'inorder', 'fillColor': CODE_COLORS['kwargs']}, {'text': '=['},
                            {'text': '9', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '},
                            {'text': '3', 'fillColor': CODE_COLORS['number']},
                            {'text': ','}, {'text': ' '}, {'text': '15', 'fillColor': CODE_COLORS['number']},
                            {'text': ','}, {'text': ' '},
                            {'text': '20', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '},
                            {'text': '7', 'fillColor': CODE_COLORS['number']},
                            {'text': ']))'},
                        ],
                    ],
                },
            }
        ],
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
