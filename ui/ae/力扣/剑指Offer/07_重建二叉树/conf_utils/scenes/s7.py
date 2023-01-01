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
    colors = {
        'keyword': '#0C007F',
        'number': '#1D22FF',
        'builtin': '#95CCE3',
        'kwargs': '#A2598F',
        'annotation': '#01CD2A',
        'currentLine': '#008AFF'
    }
    conf = {
        'codes': {
            'layerName': '代码', 'Position': [950, 500], 'duration': 60, 'width': 1200, 'height': 1000,
            'widthLine': 1200, 'heightLine': 35, 'fontSize': 25,
            'currentLine': {
                'layerName': 'currentLine',
                'Anchor Point': 'LEFT',
                # 'Position': [694, 540],
                # 'startTime': start_time,
                # 'span': {'inPoint': start_time, 'outPoint': end_time + 3},
                'pathGroup': {'type': 'Rect', 'Size': [1200, 30]},
                'Fill': {'Color': hex_to_rgb1(colors['currentLine'])}
            },
            'lines': [
                [0, {'text': 'class ', 'fillColor': colors['keyword']}, {'text': 'Solution:'}],
                [
                    1,
                    {'text': 'def ', 'fillColor': colors['keyword']}, {'text': 'buildTree('},
                    {'text': 'self ', 'fillColor': colors['kwargs']}, {'text': ', preorder, inorder):'},
                ],
                [
                    2,
                    {'text': 'def ', 'fillColor': colors['keyword']},
                    {'text': 'rebuild(idx_preorder_left, idx_preorder_right, idx_inorder_left, idx_inorder_right):'},
                ],
                [
                    3,
                    {'text': 'if ', 'fillColor': colors['keyword']}, {'text': 'idx_preorder_left > idx_preorder_right:'},
                ],
                [
                    4,
                    {'text': 'return None', 'fillColor': colors['keyword']},
                ],
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
                [
                    3,
                    {'text': 'root.left = rebuild('},
                ],
                [
                    4,
                    {'text': 'idx_preorder_left + '}, {'text': '1', 'fillColor': colors['number']},
                    {'text': ', idx_preorder_left + size_of_left_subtree,'},
                ],
                [
                    4,
                    {'text': 'idx_inorder_left, idx_inorder_root - '}, {'text': '1', 'fillColor': colors['number']},
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
                    {'text': 'idx_preorder_left + size_of_left_subtree + '}, {'text': '1', 'fillColor': colors['number']},
                    {'text': ', idx_preorder_right,'},
                ],
                [
                    4,
                    {'text': 'idx_inorder_root + '}, {'text': '1', 'fillColor': colors['number']},
                    {'text': ', idx_inorder_right'},
                ],
                [
                    3,
                    {'text': ')'},
                ],
                [3, {'text': 'return ', 'fillColor': colors['keyword']}, {'text': 'root'}],
                [],
                [2, {'text': 'idx_preorder_start = '}, {'text': '0', 'fillColor': colors['number']}],
                [2, {'text': 'idx_preorder_end = '}, {'text': 'len', 'fillColor': colors['builtin']}, {'text': '(preorder)'}],
                [2, {'text': 'idx_inorder_start = '}, {'text': '0', 'fillColor': colors['number']}],
                [2, {'text': 'idx_inorder_end = '}, {'text': 'len', 'fillColor': colors['builtin']}, {'text': '(inorder)'}],
                [],
                [
                    2,
                    {'text': 'idx_dic = {element: i '}, {'text': 'for', 'fillColor': colors['keyword']},
                    {'text': ' i, element '},
                    {'text': 'in ', 'fillColor': colors['keyword']}, {'text': 'enumerate', 'fillColor': colors['builtin']},
                    {'text': '(inorder)'}
                ],
                [
                    2,
                    {'text': 'return ', 'fillColor': colors['keyword']},
                    {'text': 'rebuild(idx_preorder_start, idx_preorder_end, idx_inorder_start, idx_inorder_end)'}
                ],
                [],
                [
                    0,
                    {'text': 'print ', 'fillColor': colors['builtin']}, {'text': '(Solution().buildTree('},
                    {'text': 'preorder', 'fillColor': colors['kwargs']}, {'text': '=['},
                    {'text': '3', 'fillColor': colors['number']}, {'text': ', '}, {'text': '9', 'fillColor': colors['number']},
                    {'text': ', '}, {'text': '20', 'Color': colors['number']}, {'text': ', '},
                    {'text': '15', 'fillColor': colors['number']}, {'text': ', '}, {'text': '7', 'fillColor': colors['number']},
                    {'text': '], '},
                    {'text': 'inorder', 'fillColor': colors['kwargs']}, {'text': '=['},
                    {'text': '9', 'fillColor': colors['number']}, {'text': ', '}, {'text': '3', 'fillColor': colors['number']},
                    {'text': ', '}, {'text': '15', 'Color': colors['number']}, {'text': ', '},
                    {'text': '20', 'fillColor': colors['number']}, {'text': ', '}, {'text': '7', 'fillColor': colors['number']},
                    {'text': ']))'},
                ],
            ],
        },
        'subtitles': subtitles,
        'annotations': [
            {
                'name': '注释0', 'text': 'left和right均包含首尾元素', 'fillColor': colors['annotation'],
                'Position': [960, 350],
                'span': {'inPoint': start_time, 'outPoint': end_time}, 'fillColor': colors['annotation'],
            },
            {
                'name': '注释1', 'text': '构造哈希映射，帮助我们快速定位根节点', 'fillColor': colors['annotation'],
                'Position': [960, 400],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
            {
                'name': '注释2', 'text': '前序遍历中的第一个节点就是根节点', 'fillColor': colors['annotation'],
                'Position': [960, 450],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
            {
                'name': '注释3', 'text': '在中序遍历中定位根节点', 'fillColor': colors['annotation'],
                'Position': [960, 500],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
            {
                'name': '注释4', 'text': '先把根节点建立出来', 'fillColor': colors['annotation'],
                'Position': [960, 550],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
            {
                'name': '注释5', 'text': '得到左子树中的节点数目', 'fillColor': colors['annotation'],
                'Position': [960, 600],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
            {
                'name': '注释6', 'text': '递归地构造左子树，并连接到根节点', 'fillColor': colors['annotation'],
                'Position': [960, 650],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
            {
                'name': '注释7', 'text': '左子树数据：前序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素',
                'fillColor': colors['annotation'], 'Position': [960, 700],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
            {
                'name': '注释8', 'text': '递归地构造右子树，并连接到根节点', 'fillColor': colors['annotation'],
                'Position': [960, 850],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
            {
                'name': '注释9', 'text': '右子树数据：前序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素',
                'fillColor': colors['annotation'], 'Position': [960, 900],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
        ],
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
