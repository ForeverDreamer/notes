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
    UNIT['pathGroup']['Size'] = [QUE_ELEM_WIDTH, QUE_ELEM_HEIGHT]
    stroke_add = UNIT['Stroke']['Stroke Width'] * 4
    duration = 60
    conf = {
        'subtitles': subtitles,
        'annotations': [
            # {
            #     'name': 'idx_p_root', 'text': 'idx_p_root', 'fillColor': COLORS['queue']['fillColor']['root'],
            #     'Position': [750, 50], 'fontSize': 25,
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': 'idx_pl', 'text': 'idx_pl', 'fillColor': COLORS['queue']['fillColor']['left'],
            #     'Position': [750, 100], 'fontSize': 25,
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': 'idx_pr', 'text': 'idx_pr', 'fillColor': COLORS['queue']['fillColor']['right'],
            #     'Position': [960, 50], 'fontSize': 25,
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': 'idx_i_root', 'text': 'idx_p_root', 'fillColor': COLORS['queue']['fillColor']['root'],
            #     'Position': [790, 150], 'fontSize': 25,
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': 'idx_il', 'text': 'idx_il', 'fillColor': COLORS['queue']['fillColor']['left'],
            #     'Position': [750, 200], 'fontSize': 25,
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': 'idx_ir', 'text': 'idx_ir', 'fillColor': COLORS['queue']['fillColor']['right'],
            #     'Position': [960, 150], 'fontSize': 25,
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': '注释4', 'text': '先把根节点建立出来', 'fillColor': colors['annotation'],
            #     'Position': [960, 550],
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': '注释5', 'text': '得到左子树中的节点数目', 'fillColor': colors['annotation'],
            #     'Position': [960, 600],
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': '注释6', 'text': '递归地构造左子树，并连接到根节点', 'fillColor': colors['annotation'],
            #     'Position': [960, 650],
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': '注释7', 'text': '左子树数据：前序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素',
            #     'fillColor': colors['annotation'], 'Position': [960, 700],
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': '注释8', 'text': '递归地构造右子树，并连接到根节点', 'fillColor': colors['annotation'],
            #     'Position': [960, 850],
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
            # {
            #     'name': '注释9', 'text': '右子树数据：前序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素',
            #     'fillColor': colors['annotation'], 'Position': [960, 900],
            #     'span': {'inPoint': start_time, 'outPoint': end_time},
            # },
        ],
        'misc': [
            {
                'layerName': '代码.队列.前序.根节点.选中框', 'Position': [771.5, 114.5],
                'width': 150, 'height': 100, 'duration': duration,
                'texts': [
                    {
                        'name': 'idx_p_root', 'text': 'idx_p_root', 'fillColor': COLORS['queue']['fillColor']['root'],
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
                'layerName': '代码.队列.前序.左边界.选中框', 'Position': [811.5, 63.5],
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
                        'Scale': [100, 100, 100], 'Position': [75, 100-37],
                        'startTime': start_time,
                    }
                ],
            },
            {
                'layerName': '代码.队列.前序.右边界.选中框', 'Position': [928.5, 63.5],
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
                        'Scale': [100, 100, 100], 'Position': [75, 100-37],
                        'startTime': start_time,
                    }
                ],
            }
        ],
        'precomps': [
            {
                'name': '代码.队列.前序', 'type': 'QUEUE', 'Position': [750, 67], 'Anchor Point': 'LEFT_TOP',
                'elems': [{'key': 3}, {'key': 9}, {'key': 20}, {'key': 15}, {'key': 7}],
                'traverse': 'preorder', 'width': QUE_ELEM_WIDTH * 5, 'height': QUE_ELEM_HEIGHT + stroke_add, 'duration': 20,
                'startTime': start_time,
                'unit': UNIT,
            },
            {
                'name': '代码.队列.中序', 'type': 'QUEUE', 'Position': [750, 167], 'Anchor Point': 'LEFT_TOP',
                'elems': [{'key': 9}, {'key': 3}, {'key': 15}, {'key': 20}, {'key': 7}],
                'traverse': 'inorder', 'width': QUE_ELEM_WIDTH * 5, 'height': QUE_ELEM_HEIGHT + stroke_add, 'duration': 20,
                'startTime': start_time,
                'unit': UNIT,
            },
        ],
        # 'codes': {
        #     'layerName': '代码', 'Position': [990, 45], 'duration': 60, 'width': 1200, 'height': 1000,
        #     'widthLine': 1200, 'heightLine': 30, 'font': 'MicrosoftSansSerif', 'fontSize': 25,
        #     'startTime': start_time, 'Anchor Point': 'LEFT_TOP',
        #     'currentLine': {
        #         'layerName': 'currentLine',
        #         'Anchor Point': 'LEFT',
        #         # 'Position': [694, 540],
        #         # 'startTime': start_time,
        #         # 'span': {'inPoint': start_time, 'outPoint': end_time + 3},
        #         'pathGroup': {'type': 'Rect', 'Size': [1200, 30]},
        #         'Fill': {'Color': hex_to_rgb1(CODE_COLORS['currentLine'])},
        #         'keyframes': {
        #             'Transform.Position': [
        #                 None,
        #                 [
        #                     18, 2, 12, 13, 14, 15, 16, 17, 3, 5, 6, 7, 8, 9, 3, 5, 6, 7, 8, 9, 3, 4, 9, 10, 3, 4, 10, 11,
        #                     9, 10, 3, 5, 6, 7, 8, 9, 3, 5, 6, 7, 8, 9, 3, 4, 9, 10, 3, 4, 10, 11, 9, 10, 3, 5, 6, 7, 8,
        #                     9, 3, 4, 9, 10, 3, 4, 10, 11, 10, 11, 10, 11, 17, 18
        #                 ],
        #                 {'spatial': [{"type": 'HOLD'}]*72}
        #             ]
        #         }
        #     },
        #     'lines': [
        #         [0, {'text': 'class', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'TreeNode:'}],
        #         [
        #             1,
        #             {'text': 'def', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
        #             {'text': '__init__', 'fillColor': CODE_COLORS['dunder']}, {'text': '('},
        #             {'text': 'self', 'fillColor': CODE_COLORS['self']}, {'text': ', values):'},
        #         ],
        #         [
        #             2,
        #             {'text': 'self', 'fillColor': CODE_COLORS['self']}, {'text': '.key = key'},
        #         ],
        #         [
        #             2,
        #             {'text': 'self', 'fillColor': CODE_COLORS['self']}, {'text': '.left ='}, {'text': ' '},
        #             {'text': 'None', 'fillColor': CODE_COLORS['keyword']},
        #         ],
        #         [
        #             2,
        #             {'text': 'self', 'fillColor': CODE_COLORS['self']}, {'text': '.right ='}, {'text': ' '},
        #             {'text': 'None', 'fillColor': CODE_COLORS['keyword']},
        #         ],
        #         [],
        #         [0, {'text': 'class', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'Solution:'}],
        #         [
        #             1,
        #             {'text': 'def', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
        #             {'text': 'buildTree', 'fillColor': CODE_COLORS['func']}, {'text': '('},
        #             {'text': 'self', 'fillColor': CODE_COLORS['self']}, {'text': ', preorder, inorder):'},
        #         ],
        #         [
        #             2,
        #             {'text': 'def', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
        #             {'text': 'rebuild', 'fillColor': CODE_COLORS['func']},
        #             {'text': '(idx_pl, idx_pr, idx_il, idx_ir):'},
        #         ],
        #         [
        #             3,
        #             {'text': 'if', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'idx_pl > idx_pr:'},
        #         ],
        #         [
        #             4,
        #             {'text': 'return None', 'fillColor': CODE_COLORS['keyword']},
        #         ],
        #         [],
        #         [
        #             3,
        #             {'text': 'idx_p_root = idx_pl'},
        #         ],
        #         [
        #             3,
        #             {'text': 'idx_i_root = idx_dic[preorder[idx_p_root]]'},
        #         ],
        #         [
        #             3,
        #             {'text': 'root = TreeNode(preorder[idx_p_root])'},
        #         ],
        #         [
        #             3,
        #             {'text': 'size_left = idx_i_root - idx_il'},
        #         ],
        #         [],
        #         [
        #             3,
        #             {'text': 'root.left = rebuild(idx_pl +'}, {'text': ' '},
        #             {'text': '1', 'fillColor': CODE_COLORS['number']},
        #             {'text': ', idx_pl + size_left, idx_il, idx_i_root -'},
        #         ],
        #         [
        #             3,
        #             {'text': 'root.right = rebuild(idx_pl + size_left +'}, {'text': ' '},
        #             {'text': '1', 'fillColor': CODE_COLORS['number']},
        #             {'text': ', idx_pr, idx_i_root +'}, {'text': ' '},
        #             {'text': '1', 'fillColor': CODE_COLORS['number']},
        #             {'text': ', idx_ir)'},
        #         ],
        #         [3, {'text': 'return', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'root'}],
        #         [],
        #         [2, {'text': 'idx_pl ='}, {'text': ' '}, {'text': '0', 'fillColor': CODE_COLORS['number']}],
        #         [
        #             2,
        #             {'text': 'idx_pr ='}, {'text': ' '}, {'text': 'len', 'fillColor': CODE_COLORS['builtin']},
        #             {'text': '(preorder) -'}, {'text': ' '}, {'text': '1', 'fillColor': CODE_COLORS['number']},
        #         ],
        #         [2, {'text': 'idx_il ='}, {'text': ' '}, {'text': '0', 'fillColor': CODE_COLORS['number']}],
        #         [
        #             2,
        #             {'text': 'idx_ir ='}, {'text': ' '}, {'text': 'len', 'fillColor': CODE_COLORS['builtin']},
        #             {'text': '(inorder) -'}, {'text': ' '}, {'text': '1', 'fillColor': CODE_COLORS['number']},
        #         ],
        #         [],
        #         [
        #             2,
        #             {'text': 'idx_dic = {element: i'}, {'text': ' '}, {'text': 'for', 'fillColor': CODE_COLORS['keyword']},
        #             {'text': ' '},  {'text': ' i, element'}, {'text': ' '},
        #             {'text': 'in', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'enumerate', 'fillColor': CODE_COLORS['builtin']},
        #             {'text': '(inorder)'}
        #         ],
        #         [
        #             2,
        #             {'text': 'return', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
        #             {'text': 'rebuild(idx_pl, idx_pr, idx_il, idx_ir)'}
        #         ],
        #         [],
        #         [
        #             0,
        #             {'text': 'print', 'fillColor': CODE_COLORS['builtin']}, {'text': '(Solution().buildTree('},
        #             {'text': 'preorder', 'fillColor': CODE_COLORS['kwargs']}, {'text': '=['},
        #             {'text': '3', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '}, {'text': '9', 'fillColor': CODE_COLORS['number']},
        #             {'text': ','}, {'text': ' '}, {'text': '20', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '},
        #             {'text': '15', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '}, {'text': '7', 'fillColor': CODE_COLORS['number']},
        #             {'text': '],'}, {'text': ' '},
        #             {'text': 'inorder', 'fillColor': CODE_COLORS['kwargs']}, {'text': '=['},
        #             {'text': '9', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '}, {'text': '3', 'fillColor': CODE_COLORS['number']},
        #             {'text': ','}, {'text': ' '}, {'text': '15', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '},
        #             {'text': '20', 'fillColor': CODE_COLORS['number']}, {'text': ','}, {'text': ' '}, {'text': '7', 'fillColor': CODE_COLORS['number']},
        #             {'text': ']))'},
        #         ],
        #     ],
        # },
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
