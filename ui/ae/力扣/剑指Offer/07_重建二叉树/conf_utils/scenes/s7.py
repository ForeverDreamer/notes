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
    conf = {
        'codes': {
            'layerName': '代码', 'Position': [1420, 550], 'duration': 60, 'width': 1200, 'height': 1000,
            'widthLine': 1200, 'heightLine': 30, 'font': 'MicrosoftSansSerif', 'fontSize': 25,
            'startTime': start_time,
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
                            24, 2, 18, 19, 20, 21, 22, 23, 3, 5, 6, 7, 8, 9, 10, 11, 9, 3, 5, 6, 7, 8, 9, 10, 11, 9, 3,
                            4, 9, 13, 14, 15, 13, 3, 4, 13, 17, 9, 13, 14, 15, 13, 3, 5, 6, 7, 8, 9, 10, 11, 9, 3, 5, 6,
                            7, 8, 9, 10, 11, 9, 3, 4, 9, 13, 14, 15, 13, 3, 4, 13, 17, 9, 13, 14, 15, 13, 3, 5, 6, 7, 8,
                            9, 10, 11, 9, 3, 4, 9, 13, 14, 15, 13, 3, 4, 13, 17, 13, 17, 13, 17, 23
                        ],
                        {'spatial': [{"type": 'HOLD'}]*101}
                    ]
                }
            },
            'lines': [
                [0, {'text': 'class', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'Solution:'}],
                [
                    1,
                    {'text': 'def', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'buildTree('},
                    {'text': 'self', 'fillColor': CODE_COLORS['kwargs']}, {'text': ', preorder, inorder):'},
                ],
                [
                    2,
                    {'text': 'def', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '},
                    {'text': 'rebuild(idx_preorder_left, idx_preorder_right, idx_inorder_left, idx_inorder_right):'},
                ],
                [
                    3,
                    {'text': 'if', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'idx_preorder_left > idx_preorder_right:'},
                ],
                [
                    4,
                    {'text': 'return None', 'fillColor': CODE_COLORS['keyword']},
                ],
                [],
                [
                    3,
                    {'text': 'idx_preorder_root = idx_preorder_left'},
                ],
                [
                    3,
                    {'text': 'idx_inorder_root = idx_dic[preorder[idx_preorder_root]]'},
                ],
                [
                    3,
                    {'text': 'root = TreeNode(preorder[idx_preorder_root])'},
                ],
                [
                    3,
                    {'text': 'size_of_left_subtree = idx_inorder_root - idx_inorder_left'},
                ],
                [],
                [
                    3,
                    {'text': 'root.left = rebuild('},
                ],
                [
                    4,
                    {'text': 'idx_preorder_left +'}, {'text': ' '}, {'text': '1', 'fillColor': CODE_COLORS['number']},
                    {'text': ', idx_preorder_left + size_of_left_subtree,'},
                ],
                [
                    4,
                    {'text': 'idx_inorder_left, idx_inorder_root -'}, {'text': ' '}, {'text': '1', 'fillColor': CODE_COLORS['number']},
                ],
                [
                    3,
                    {'text': ')'},
                ],
                [
                    3,
                    {'text': 'root.right = rebuild('},
                ],
                [
                    4,
                    {'text': 'idx_preorder_left + size_of_left_subtree +'}, {'text': ' '}, {'text': '1', 'fillColor': CODE_COLORS['number']},
                    {'text': ', idx_preorder_right,'},
                ],
                [
                    4,
                    {'text': 'idx_inorder_root +'}, {'text': ' '}, {'text': '1', 'fillColor': CODE_COLORS['number']},
                    {'text': ', idx_inorder_right'},
                ],
                [
                    3,
                    {'text': ')'},
                ],
                [3, {'text': 'return', 'fillColor': CODE_COLORS['keyword']}, {'text': ' '}, {'text': 'root'}],
                [],
                [2, {'text': 'idx_preorder_start ='}, {'text': ' '}, {'text': '0', 'fillColor': CODE_COLORS['number']}],
                [2, {'text': 'idx_preorder_end ='}, {'text': ' '}, {'text': 'len', 'fillColor': CODE_COLORS['builtin']}, {'text': '(preorder)'}],
                [2, {'text': 'idx_inorder_start ='}, {'text': ' '}, {'text': '0', 'fillColor': CODE_COLORS['number']}],
                [2, {'text': 'idx_inorder_end ='}, {'text': ' '}, {'text': 'len', 'fillColor': CODE_COLORS['builtin']}, {'text': '(inorder)'}],
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
                    {'text': 'rebuild(idx_preorder_start, idx_preorder_end, idx_inorder_start, idx_inorder_end)'}
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
        'subtitles': subtitles,
        # 'annotations': [
        #     {
        #         'name': '注释0', 'text': 'left和right均包含首尾元素', 'fillColor': colors['annotation'],
        #         'Position': [960, 350],
        #         'span': {'inPoint': start_time, 'outPoint': end_time}, 'fillColor': colors['annotation'],
        #     },
        #     {
        #         'name': '注释1', 'text': '构造哈希映射，帮助我们快速定位根节点', 'fillColor': colors['annotation'],
        #         'Position': [960, 400],
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        #     {
        #         'name': '注释2', 'text': '前序遍历中的第一个节点就是根节点', 'fillColor': colors['annotation'],
        #         'Position': [960, 450],
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        #     {
        #         'name': '注释3', 'text': '在中序遍历中定位根节点', 'fillColor': colors['annotation'],
        #         'Position': [960, 500],
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        #     {
        #         'name': '注释4', 'text': '先把根节点建立出来', 'fillColor': colors['annotation'],
        #         'Position': [960, 550],
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        #     {
        #         'name': '注释5', 'text': '得到左子树中的节点数目', 'fillColor': colors['annotation'],
        #         'Position': [960, 600],
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        #     {
        #         'name': '注释6', 'text': '递归地构造左子树，并连接到根节点', 'fillColor': colors['annotation'],
        #         'Position': [960, 650],
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        #     {
        #         'name': '注释7', 'text': '左子树数据：前序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素',
        #         'fillColor': colors['annotation'], 'Position': [960, 700],
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        #     {
        #         'name': '注释8', 'text': '递归地构造右子树，并连接到根节点', 'fillColor': colors['annotation'],
        #         'Position': [960, 850],
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        #     {
        #         'name': '注释9', 'text': '右子树数据：前序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素',
        #         'fillColor': colors['annotation'], 'Position': [960, 900],
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        # ],
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
