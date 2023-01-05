from ae.constants.share import *
from .transcript import scenes
from ae.utils.py.color import hex_to_rgb1

name = 's7'


def shot_0(start_time):
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time + i * SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]
    QUE_ELEM_WIDTH = 40
    QUE_ELEM_HEIGHT = 40
    QUE_UNIT['pathGroup']['Size'] = [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT]
    stroke_add = QUE_UNIT['Stroke']['Stroke Width'] * 4
    duration = 60
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
                'name': '代码.二叉树重建', 'type': 'BINARY_TREE', 'width': 500, 'height': 500,
                'startTime': start_time, 'duration': 8, 'Anchor Point': 'LEFT_TOP', 'Position': [50, 250],
                'elems': [{'key': 3}, {'key': 9}, {'key': 20}, {'key': None}, {'key': None}, {'key': 15}, {'key': 7}],
                'animation': 'true',
                'node': {
                    'shape': {'name': 'Node Shape Black/Elements.ai', 'Scale': [80, 80, 80]},
                },
                'edge': {
                    'shape': {'name': 'Edge Black/Elements.ai', 'Anchor Point': 'TOP', 'Scale': [80, 80, 80],
                              'Rotation': 30},
                },
                # '3D': 'true'
            }
        ],
        'misc': [
            {
                'layerName': '代码.队列.前序', 'Position': [771.5, 135.5],
                'width': 300, 'height': 150, 'duration': duration,
                'texts': [
                    {
                        'name': '名字', 'text': '前序',
                        'Anchor Point': 'LEFT', 'Position': [0, 75], 'font': FONTS['cn'], 'fontSize': 40,
                        'span': {'inPoint': start_time, 'outPoint': end_time},
                    },
                ],
                'precomps': [
                    {
                        'name': '数据', 'type': 'QUEUE', 'Position': [86.5, 56], 'Anchor Point': 'LEFT_TOP',
                        'elems': [{'key': 3}, {'key': 9}, {'key': 20}, {'key': 15}, {'key': 7}],
                        'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5, 'height': QUE_ELEM_HEIGHT + stroke_add,
                        'duration': 20,
                        'startTime': start_time,
                        'unit': QUE_UNIT,
                    },
                ],
                'misc': [
                    {
                        'layerName': '根节点.选中框', 'Position': [108, 103.5],
                        'width': 150, 'height': 100, 'duration': duration,
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
                                'startTime': start_time,
                            }
                        ],
                    },
                    {
                        'layerName': '左边界.选中框', 'Position': [148, 52.5],
                        'width': 150, 'height': 100, 'duration': duration,
                        'texts': [
                            {
                                'name': 'idx_pl', 'text': 'idx_pl', 'fillColor': COLORS['queue']['fillColor']['left'],
                                'Position': [75, 15], 'fontSize': 25,
                                'span': {'inPoint': start_time, 'outPoint': end_time},
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
                        'texts': [
                            {
                                'name': 'idx_pr', 'text': 'idx_pr', 'fillColor': COLORS['queue']['fillColor']['right'],
                                'Position': [75, 15], 'fontSize': 25,
                                'span': {'inPoint': start_time, 'outPoint': end_time},
                            },
                        ],
                        'vectors': [
                            {
                                'name': 'Queue Code Selected Right/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 100 - 37],
                                'startTime': start_time,
                            }
                        ],
                    }
                ],
            },
            {
                'layerName': '代码.队列.中序', 'Position': [771.5, 316],
                'width': 300, 'height': 150, 'duration': duration,
                'texts': [
                    {
                        'name': '名字', 'text': '中序',
                        'Anchor Point': 'LEFT', 'Position': [0, 75], 'font': FONTS['cn'], 'fontSize': 40,
                        'span': {'inPoint': start_time, 'outPoint': end_time},
                    },
                ],
                'precomps': [
                    {
                        'name': '数据', 'type': 'QUEUE', 'Position': [86.5, 56], 'Anchor Point': 'LEFT_TOP',
                        'elems': [{'key': 3}, {'key': 9}, {'key': 20}, {'key': 15}, {'key': 7}],
                        'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5, 'height': QUE_ELEM_HEIGHT + stroke_add,
                        'duration': 20,
                        'startTime': start_time,
                        'unit': QUE_UNIT,
                    },
                ],
                'misc': [
                    {
                        'layerName': '根节点.选中框', 'Position': [108, 103.5],
                        'width': 150, 'height': 100, 'duration': duration,
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
                                'startTime': start_time,
                            }
                        ],
                    },
                    {
                        'layerName': '左边界.选中框', 'Position': [148, 52.5],
                        'width': 150, 'height': 100, 'duration': duration,
                        'texts': [
                            {
                                'name': 'idx_pl', 'text': 'idx_pl', 'fillColor': COLORS['queue']['fillColor']['left'],
                                'Position': [75, 15], 'fontSize': 25,
                                'span': {'inPoint': start_time, 'outPoint': end_time},
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
                        'texts': [
                            {
                                'name': 'idx_pr', 'text': 'idx_pr', 'fillColor': COLORS['queue']['fillColor']['right'],
                                'Position': [75, 15], 'fontSize': 25,
                                'span': {'inPoint': start_time, 'outPoint': end_time},
                            },
                        ],
                        'vectors': [
                            {
                                'name': 'Queue Code Selected Right/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 100 - 37],
                                'startTime': start_time,
                            }
                        ],
                    }
                ],
            },
            {
                'layerName': '代码.合成', 'duration': duration, 'width': 1419, 'height': 934,
                'startTime': start_time, 'Anchor Point': 'LEFT_TOP', 'Position': [620, 45],
                'texts': [
                    {
                        'layerName': 'idx_dic', 'text': 'idx_dic = {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}',
                        'Position': [215, 484], 'fontSize': 25,
                        'span': {'inPoint': start_time, 'outPoint': end_time},
                    },
                ],
                'precomps': [
                    {
                        'layerName': '函数调用栈', 'type': 'STACK', 'Position': [8, 618], 'Anchor Point': 'LEFT_TOP',
                        'elems': [
                            {'key': '<module>'}, {'key': 'buildTree( )'}, {'key': 'rebuild( )'}, {'key': 'rebuild( )'},
                            {'key': 'rebuild( )'}, {'key': 'rebuild( )'}
                        ],
                        'width': STACK_ELEM_WIDTH + stroke_add, 'height': STACK_ELEM_HEIGHT*6 + stroke_add,
                        'duration': 20,
                        'startTime': start_time,
                        'unit': STACK_UNIT,
                    },
                ],
                'codes': {
                    'layerName': '代码', 'Position': [370, 0], 'duration': duration, 'width': 1200, 'height': 934,
                    'widthLine': 1200, 'heightLine': 30, 'font': 'MicrosoftSansSerif', 'fontSize': 25,
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
                                    18, 2, 12, 13, 14, 15, 16, 17, 3, 5, 6, 7, 8, 9, 3, 5, 6, 7, 8, 9, 3, 4, 9, 10, 3, 4, 10, 11,
                                    9, 10, 3, 5, 6, 7, 8, 9, 3, 5, 6, 7, 8, 9, 3, 4, 9, 10, 3, 4, 10, 11, 9, 10, 3, 5, 6, 7, 8,
                                    9, 3, 4, 9, 10, 3, 4, 10, 11, 10, 11, 10, 11, 17, 18
                                ],
                                {'spatial': [{"type": 'HOLD'}]*72}
                            ]
                        }
                    },
                    'lines': [
                        [0, {'text': 'class', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'TreeNode:'}],
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
                        [0, {'text': 'class', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'Solution:'}],
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
                            {'text': 'if', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'idx_pl > idx_pr:'},
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
                            {'text': 'idx_dic = {element: i'}, {'text': ' '}, {'text': 'for', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},  {'text': ' i, element'}, {'text': ' '},
                            {'text': 'in', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'enumerate', 'fillColor': CODE_COLORS['builtin']},
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
                            {'text': '3', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '}, {'text': '9', 'fillColor': CODE_COLORS['number']},
                            {'text': ','}, {'text': ' '}, {'text': '20', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '},
                            {'text': '15', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '}, {'text': '7', 'fillColor': CODE_COLORS['number']},
                            {'text': '],'}, {'text': ' '},
                            {'text': 'inorder', 'fillColor': CODE_COLORS['kwargs']}, {'text': '=['},
                            {'text': '9', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '}, {'text': '3', 'fillColor': CODE_COLORS['number']},
                            {'text': ','}, {'text': ' '}, {'text': '15', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '},
                            {'text': '20', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '}, {'text': '7', 'fillColor': CODE_COLORS['number']},
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
