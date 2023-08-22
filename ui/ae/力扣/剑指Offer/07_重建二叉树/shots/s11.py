from glob import glob
from operator import itemgetter

from mutagen.mp3 import MP3

from constants.share import *
from .consts import ASSETS_DIR
from .transcript import subtitles as all_subtitles
from utils.py.color import hex_to_rgb1

sn = 11
prefix = f's{sn}'

def audios_subtitles():
    files = glob(f'{ASSETS_DIR}/audios/{prefix}/*.mp3')
    names = []
    for f in files:
        elems = []
        for x in f.split('\\')[-1].split('.'):
            try:
                elems.append(int(x))
            except ValueError:
                pass
        elems.append(f)
        elems = tuple(elems)
        names.append(elems)

    names = sorted(names, key=itemgetter(0, 1))
    audios = []
    subtitles = []
    start_time = 0
    for i, af in enumerate(names):
        audio = MP3(af[-1])
        audios.append(
            {
                'path': af[-1],
                'layers': [
                    {
                        'name': af[-1].split('\\')[-1],
                        'startTime': start_time,
                        'Anchor Point': 'null',
                    }
                ],
            }
        )
        subtitles.append([start_time, all_subtitles[sn][i]])
        start_time += audio.info.length + 0.5

    subtitles = list(zip(*subtitles))
    end_time = subtitles[0][-1] + SHOTS_INTERVAL
    return audios, subtitles, end_time


def currentline_times(subtitles, steps):
    times = []
    intervals = subtitles[2]
    i = 0
    while i < len(subtitles[2]):
        if intervals[i] == 0:
            i += 1
            continue
        elif intervals[i] == 1:
            times.append(subtitles[0][i])
        else:
            times.append(subtitles[0][i])
            interval = (subtitles[0][i+1] - subtitles[0][i])/intervals[i]
            times += [times[-1]+interval*j for j in range(1, intervals[i])]
        i += 1

    i = len(times) - 1
    while len(times) < steps:
        times.append(times[i]+1)
        i += 1

    return times


def build_conf(start_time):
    audios, subtitles, end_time = audios_subtitles()
    subtitles.append([1, 1, 4, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1])
    _CURRENTLINE_STEPS = 72
    _currentline_times = currentline_times(subtitles, _CURRENTLINE_STEPS)
    QUE_ELEM_WIDTH = 40
    QUE_ELEM_HEIGHT = 40
    QUE_UNIT['pathGroup']['Size'] = [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT]
    stroke_add = QUE_UNIT['Stroke']['Stroke Width'] * 4
    duration = _currentline_times[-1] + SHOTS_INTERVAL
    temporal = [[[0, 0.1], [0, 0.1], [200, 100]], [[0, 75], [0, 75], [0, 0.1]]]

    # 工作量大或相互关联的配置提到前边统一填写，避免滚轮滚上滚下到处找，头都晕了~，
    # 代码每断点调试一次只核对一个变量，多了容易出错
    conf = {
        'layerName': prefix, 'duration': duration,
        'files': [
            {
                'folder': 'audios',
                'files': audios,
            },
        ],
        'subtitles': subtitles,
        'dsa': [
            {
                'layerName': f'{prefix}.二叉树', 'type': 'BINARY_TREE', 'width': 760, 'height': 700,
                'startTime': start_time, 'duration': duration, 'Anchor Point': 'LEFT_TOP', 'Position': [0, 160],
                'elems': [
                    {
                        'key': 3,
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[12]],
                                [0, 100],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 9,
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[18]],
                                [0, 100],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 20,
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[34]],
                                [0, 100],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': '空',
                        'layerName': '9.空.left',
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[23], _currentline_times[23] + 1],
                                [0, 100, 0],
                                {"spatial": [{"type": 'HOLD'}] * 3}
                            ]
                        }
                    },
                    {
                        'key': '空',
                        'layerName': '9.空.right',
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[27], _currentline_times[27] + 1],
                                [0, 100, 0],
                                {"spatial": [{"type": 'HOLD'}] * 3}
                            ]
                        }
                    },
                    {
                        'key': 15,
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[40]],
                                [0, 100],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {
                        'key': 7,
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[56]],
                                [0, 100],
                                {"spatial": [{"type": 'HOLD'}] * 2}
                            ]
                        }
                    },
                    {'key': None}, {'key': None}, {'key': None}, {'key': None},
                    {
                        'key': '空',
                        'layerName': '15.空.left',
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[45], _currentline_times[45] + 1],
                                [0, 100, 0],
                                {"spatial": [{"type": 'HOLD'}] * 3}
                            ]
                        }
                    },
                    {
                        'key': '空',
                        'layerName': '15.空.right',
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[49], _currentline_times[49] + 1],
                                [0, 100, 0],
                                {"spatial": [{"type": 'HOLD'}] * 3}
                            ]
                        }
                    },
                    {
                        'key': '空',
                        'layerName': '7.空.left',
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[61], _currentline_times[61] + 1],
                                [0, 100, 0],
                                {"spatial": [{"type": 'HOLD'}] * 3}
                            ]
                        }
                    },
                    {
                        'key': '空',
                        'layerName': '7.空.right',
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[65], _currentline_times[65] + 1],
                                [0, 100, 0],
                                {"spatial": [{"type": 'HOLD'}] * 3}
                            ]
                        }
                    },
                    {'key': None}, {'key': None}, {'key': None}, {'key': None},
                    {'key': None}, {'key': None}, {'key': None}, {'key': None},
                ],
                'animation': 'false',
                'node': {
                    'shape': {'sourceName': 'Node Shape Black/Elements.ai', 'Scale': [80, 80, 80]},
                },
                'edge': {
                    'shape': {'sourceName': 'Edge Black/Elements.ai', 'Anchor Point': 'TOP', 'Scale': [80, 80, 80],
                              'Rotation': 30},
                },
                # '3D': 'true'
                'keyframes': {

                }
            }
        ],
        'comps': [
            {
                'layerName': f'{prefix}.前序遍历结果', 'width': 330, 'height': 150, 'Position': [771.5, 135.5],
                'startTime': start_time, 'duration': duration,
                'keyframes': {
                    'Transform.Opacity': [[0, 1], [0, 100], {"spatial": [{"type": 'HOLD'}]}],
                },
                'texts': [
                    {
                        'text': '前序',
                        'Anchor Point': 'LEFT', 'Position': [0, 75], 'font': FONTS['cn'], 'fontSize': 40,
                    },
                ],
                'dsa': [
                    {
                        'layerName': '数据', 'type': 'QUEUE', 'Position': [86.5, 56], 'Anchor Point': 'LEFT_TOP',
                        'elems': [{'key': 3}, {'key': 9}, {'key': 20}, {'key': 15}, {'key': 7}],
                        'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5, 'height': QUE_ELEM_HEIGHT + stroke_add,
                        'unit': QUE_UNIT, 'duration': duration,
                    },
                ],
                'comps': [
                    {
                        'layerName': '根选中框', 'width': 44, 'height': 44, 'Position': [108, 78.5],
                        'duration': duration,
                        # 'keyframes': keyframes['preorder']['root'],
                        'vectors': [
                            {
                                'sourceName': 'Queue Code Selected Root/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [22, 22],
                            }
                        ],
                        'texts': [
                            {
                                'text': 'root',
                                'fillColor': COLORS['text'],
                                'Position': [22, 19.2], 'fontSize': 20,
                            },
                        ],
                    },
                    {
                        'layerName': '左选中框', 'width': 150, 'height': 100, 'Position': [148, 52.5],
                        'duration': duration,
                        # 'keyframes': keyframes['preorder']['left'],
                        'texts': [
                            {
                                'text': 'idx_pl', 'fillColor': COLORS['queue']['fillColor']['left'],
                                'Position': [75, 15], 'fontSize': 25,
                            },
                        ],
                        'vectors': [
                            {
                                'sourceName': 'Queue Code Selected Left/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 100 - 37],
                            }
                        ],
                    },
                    {
                        'layerName': '右选中框', 'width': 150, 'height': 100, 'Position': [265, 104.5],
                        'duration': duration,
                        # 'keyframes': keyframes['preorder']['right'],
                        'texts': [
                            {
                                'text': 'idx_pr', 'fillColor': COLORS['queue']['fillColor']['right'],
                                'Position': [75, 83], 'fontSize': 25,
                            },
                        ],
                        'vectors': [
                            {
                                'sourceName': 'Queue Code Selected Right/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 36],
                            }
                        ],
                    }
                ],
            },
            {
                'layerName': f'{prefix}.中序遍历结果', 'width': 330, 'height': 150, 'Position': [771.5, 316],
                'startTime': start_time, 'duration': duration,
                'keyframes': {
                    'Transform.Opacity': [[0, 1], [0, 100], {"spatial": [{"type": 'HOLD'}] * 2}],
                },
                'texts': [
                    {
                        'text': '中序',
                        'Anchor Point': 'LEFT', 'Position': [0, 75], 'font': FONTS['cn'], 'fontSize': 40,
                    },
                ],
                'dsa': [
                    {
                        'layerName': '数据', 'type': 'QUEUE', 'Position': [86.5, 56], 'Anchor Point': 'LEFT_TOP',
                        'elems': [{'key': 9}, {'key': 3}, {'key': 15}, {'key': 20}, {'key': 7}],
                        'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5, 'height': QUE_ELEM_HEIGHT + stroke_add,
                        'duration': duration,
                        'unit': QUE_UNIT,
                    },
                ],
                'comps': [
                    {
                        'layerName': '根选中框', 'Position': [108, 78.5],
                        'width': 44, 'height': 44, 'duration': duration,
                        # 'keyframes': {
                        #     'Transform.Opacity': keyframes['inorder']['root']['Opacity'],
                        #     'Transform.Position': keyframes['inorder']['root']['Position'],
                        # },
                        'vectors': [
                            {
                                'sourceName': 'Queue Code Selected Root/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [22, 22],
                            }
                        ],
                        'texts': [
                            {
                                'text': 'root',
                                'fillColor': COLORS['text'],
                                'Position': [22, 19.2], 'fontSize': 20,
                                # 'span': {'inPoint': start_time, 'outPoint': end_time},
                            },
                        ],
                    },
                    {
                        'layerName': '左选中框', 'Position': [148, 52.5],
                        'width': 150, 'height': 100, 'duration': duration,
                        # 'keyframes': {
                        #     'Transform.Opacity': keyframes['inorder']['left']['Opacity'],
                        #     'Transform.Position': keyframes['inorder']['left']['Position'],
                        # },
                        'texts': [
                            {
                                'text': 'idx_il', 'fillColor': COLORS['queue']['fillColor']['left'],
                                'Position': [75, 15], 'fontSize': 25,
                            },
                        ],
                        'vectors': [
                            {
                                'sourceName': 'Queue Code Selected Left/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 100 - 37],
                                'startTime': start_time,
                            }
                        ],
                    },
                    {
                        'layerName': '右选中框', 'Position': [265, 104.5],
                        'width': 150, 'height': 100, 'duration': duration,
                        # 'keyframes': {
                        #     'Transform.Opacity': keyframes['inorder']['right']['Opacity'],
                        #     'Transform.Position': keyframes['inorder']['right']['Position'],
                        # },
                        'texts': [
                            {
                                'text': 'idx_ir', 'fillColor': COLORS['queue']['fillColor']['right'],
                                'Position': [75, 83], 'fontSize': 25,
                            },
                        ],
                        'vectors': [
                            {
                                'sourceName': 'Queue Code Selected Right/Elements.ai',
                                'Scale': [100, 100, 100], 'Position': [75, 36],
                            }
                        ],
                    }
                ],
            },
            {
                'layerName': f'{prefix}.代码调试', 'width': 1419, 'height': 934,
                'Anchor Point': 'LEFT_TOP', 'Position': [595, 45],
                'startTime': start_time, 'duration': duration,
                'texts': [
                    {
                        'layerName': 'idx_pl', 'text': 'idx_pl: 0',
                        'Position': [644, 660], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        # 'keyframes': keyframes['vars']['idx_pl']
                    },
                    {
                        'layerName': 'idx_pr', 'text': 'idx_pr: 4',
                        'Position': [810, 691], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        # 'keyframes': keyframes['vars']['idx_pr']
                    },
                    {
                        'layerName': 'idx_il', 'text': 'idx_il: 0',
                        'Position': [631, 722], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        # 'keyframes': keyframes['vars']['idx_il']
                    },
                    {
                        'layerName': 'idx_ir', 'text': 'idx_ir: 4',
                        'Position': [781, 751], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        # 'keyframes': keyframes['vars']['idx_ir']
                    },
                    {
                        'layerName': 'idx_dic', 'text': 'idx_dic = {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}',
                        'Position': [215, 484], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        # 'keyframes': keyframes['vars']['idx_dic']
                    },
                    {
                        'layerName': 'idx_pl.idx_pr.idx_il.idx_ir',
                        'text': 'idx_pl: 0  idx_pr: 4  idx_il: 0  idx_ir: 4',
                        'Position': [1111, 270], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        # 'keyframes': keyframes['vars']['idx_pl.idx_pr.idx_il.idx_ir']
                    },
                    {
                        'layerName': 'idx_p_root', 'text': 'idx_p_root: 0',
                        'Position': [818, 390], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        # 'keyframes': keyframes['vars']['idx_p_root']
                    },
                    {
                        'layerName': 'idx_i_root', 'text': 'idx_i_root: 1',
                        'Position': [1057, 420], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        # 'keyframes': keyframes['vars']['idx_i_root']
                    },
                    {
                        'layerName': 'root', 'text': 'root: 3',
                        'Position': [995, 447], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        # 'keyframes': keyframes['vars']['root']
                    },
                    {
                        'layerName': 'size_left', 'text': 'size_left: 1',
                        'Position': [900, 480], 'fontSize': FONT_SIZES['code'], 'fillColor': CODE_COLORS['annotation'],
                        # 'keyframes': keyframes['vars']['size_left']
                    },
                ],
                'shapes': [
                    {
                        'layerName': '主函数选中框',
                        'Position': [791, 898],
                        # 'startTime': start_time,
                        # 'span': {'inPoint': start_time, 'outPoint': end_time + 3},
                        'pathGroup': {'type': 'Rect', 'Size': [858, 43]},
                        'Stroke': {'Stroke Width': 3, 'Color': hex_to_rgb1('#FF0000')},
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, 1, _currentline_times[1]],
                                [0, 100, 0],
                                {"spatial": [{"type": 'HOLD'}] * 3}
                            ]
                        }
                    },
                    {
                        'layerName': '递归重建函数选中框',
                        'Position': [868, 434],
                        # 'startTime': start_time,
                        # 'span': {'inPoint': start_time, 'outPoint': end_time + 3},
                        'pathGroup': {'type': 'Rect', 'Size': [810, 358]},
                        'Stroke': {'Stroke Width': 3, 'Color': hex_to_rgb1('#FF0000')},
                        'keyframes': {
                            "Transform.Opacity": [
                                [0, _currentline_times[1], _currentline_times[2]],
                                [0, 100, 0],
                                {"spatial": [{"type": 'HOLD'}] * 3}
                            ]
                        }
                    },
                ],
                'dsa': [
                    {
                        'layerName': '函数调用栈', 'type': 'STACK', 'Position': [185, 618], 'Anchor Point': 'LEFT_TOP',
                        'width': STACK_ELEM_WIDTH + stroke_add, 'height': STACK_ELEM_HEIGHT * 6 + stroke_add,
                        'duration': duration,
                        'startTime': start_time,
                        'unit': STACK_UNIT,
                        'elems': [
                            {
                                'key': '<module>',
                            },
                            {
                                'key': 'buildTree( )',
                            },
                            {
                                'key': 'rebuild( )',
                                'layerName': 'rebuild( ).0',
                            }, {
                                'key': 'rebuild( )',
                                'layerName': 'rebuild( ).1',
                            },
                            {
                                'key': 'rebuild( )',
                                'layerName': 'rebuild( ).2',
                            },
                            {
                                'key': 'rebuild( )',
                                'layerName': 'rebuild( ).3',
                            }
                        ],
                    },
                ],
                'codes': {
                    'layerName': f'{prefix}.代码', 'Position': [370, 0], 'duration': duration, 'width': 1200, 'height': 934,
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
                        'steps': _CURRENTLINE_STEPS,
                        'keyframes': {
                            'Transform.Position': [
                                _currentline_times,
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
                        [
                            0,
                            {'text': 'class', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},
                            {'text': 'TreeNode:'}
                        ],
                        [
                            1,
                            {'text': 'def', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},
                            {'text': '__init__', 'fillColor': CODE_COLORS['dunder']},
                            {'text': '('},
                            {'text': 'self', 'fillColor': CODE_COLORS['self']},
                            {'text': ', key):'},
                        ],
                        [
                            2,
                            {'text': 'self', 'fillColor': CODE_COLORS['self']},
                            {'text': '.key = key'},
                        ],
                        [
                            2,
                            {'text': 'self', 'fillColor': CODE_COLORS['self']},
                            {'text': '.left ='},
                            {'text': ' '},
                            {'text': 'None', 'fillColor': CODE_COLORS['keyword']},
                        ],
                        [
                            2,
                            {'text': 'self', 'fillColor': CODE_COLORS['self']},
                            {'text': '.right ='},
                            {'text': ' '},
                            {'text': 'None', 'fillColor': CODE_COLORS['keyword']},
                        ],
                        [],
                        [
                            0,
                            {'text': 'class', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},
                            {'text': 'Solution:'}
                        ],
                        [
                            1,
                            {'text': 'def', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},
                            {'text': 'buildTree', 'fillColor': CODE_COLORS['func']},
                            {'text': '('},
                            {'text': 'self', 'fillColor': CODE_COLORS['self']},
                            {'text': ', preorder, inorder):'},
                        ],
                        [
                            2,
                            {'text': 'def', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},
                            {'text': 'rebuild', 'fillColor': CODE_COLORS['func']},
                            {'text': '(idx_pl, idx_pr, idx_il, idx_ir):'},
                        ],
                        [
                            3,
                            {'text': 'if', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},
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
                            {'text': 'root.left = rebuild(idx_pl +'},
                            {'text': ' '},
                            {'text': '1', 'fillColor': CODE_COLORS['number']},
                            {'text': ', idx_pl + size_left, idx_il, idx_i_root -'},
                            {'text': ' '}, {'text': '1', 'fillColor': CODE_COLORS['number']},
                            {'text': ')'},
                        ],
                        [
                            3,
                            {'text': 'root.right = rebuild(idx_pl + size_left +'},
                            {'text': ' '},
                            {'text': '1', 'fillColor': CODE_COLORS['number']},
                            {'text': ', idx_pr, idx_i_root +'},
                            {'text': ' '},
                            {'text': '1', 'fillColor': CODE_COLORS['number']},
                            {'text': ', idx_ir)'},
                        ],
                        [
                            3,
                            {'text': 'return', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},
                            {'text': 'root'}
                        ],
                        [],
                        [
                            2,
                            {'text': 'idx_pl ='},
                            {'text': ' '},
                            {'text': '0', 'fillColor': CODE_COLORS['number']}
                        ],
                        [
                            2,
                            {'text': 'idx_pr ='},
                            {'text': ' '},
                            {'text': 'len', 'fillColor': CODE_COLORS['builtin']},
                            {'text': '(preorder) -'},
                            {'text': ' '},
                            {'text': '1', 'fillColor': CODE_COLORS['number']},
                        ],
                        [
                            2,
                            {'text': 'idx_il ='},
                            {'text': ' '},
                            {'text': '0', 'fillColor': CODE_COLORS['number']}
                        ],
                        [
                            2,
                            {'text': 'idx_ir ='},
                            {'text': ' '},
                            {'text': 'len', 'fillColor': CODE_COLORS['builtin']},
                            {'text': '(inorder) -'},
                            {'text': ' '},
                            {'text': '1', 'fillColor': CODE_COLORS['number']},
                        ],
                        [],
                        [
                            2,
                            {'text': 'idx_dic = {element: i'},
                            {'text': ' '},
                            {'text': 'for', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},
                            {'text': ' i, element'},
                            {'text': ' '},
                            {'text': 'in', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},
                            {'text': 'enumerate', 'fillColor': CODE_COLORS['builtin']},
                            {'text': '(inorder)'}
                        ],
                        [
                            2,
                            {'text': 'return', 'fillColor': CODE_COLORS['keyword']},
                            {'text': ' '},
                            {'text': 'rebuild(idx_pl, idx_pr, idx_il, idx_ir)'}
                        ],
                        [],
                        [
                            0,
                            {'text': 'print', 'fillColor': CODE_COLORS['builtin']},
                            {'text': '(Solution().buildTree('},
                            {'text': 'preorder', 'fillColor': CODE_COLORS['kwargs']},
                            {'text': '=['},
                            {'text': '3', 'fillColor': CODE_COLORS['number']},
                            {'text': ','},
                            {'text': ' '},
                            {'text': '9', 'fillColor': CODE_COLORS['number']},
                            {'text': ','},
                            {'text': ' '},
                            {'text': '20', 'fillColor': CODE_COLORS['number']},
                            {'text': ','},
                            {'text': ' '},
                            {'text': '15', 'fillColor': CODE_COLORS['number']},
                            {'text': ','},
                            {'text': ' '},
                            {'text': '7', 'fillColor': CODE_COLORS['number']},
                            {'text': '],'},
                            {'text': ' '},
                            {'text': 'inorder', 'fillColor': CODE_COLORS['kwargs']},
                            {'text': '=['},
                            {'text': '9', 'fillColor': CODE_COLORS['number']},
                            {'text': ','}, {'text': ' '},
                            {'text': '3', 'fillColor': CODE_COLORS['number']},
                            {'text': ','},
                            {'text': ' '},
                            {'text': '15', 'fillColor': CODE_COLORS['number']},
                            {'text': ','},
                            {'text': ' '},
                            {'text': '20', 'fillColor': CODE_COLORS['number']},
                            {'text': ','},
                            {'text': ' '},
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


def build(start_time):
    conf = build_conf(start_time)
    return sn, build_conf(start_time), conf['end_time']


if __name__ == '__main__':
    build(0)
