from ae.constants.share import *
from .transcript import scenes


name = 's7'


def shot_0(start_time):
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]
    colors = {
        'keyword': '#0C007F',
        'number': '#1D22FF',
        'builtin': '#95CCE3',
        'kwargs': '#A2598F',
        'annotation': '#93AB40',
        'breakpoint': '#2154A6'
    }
    conf = {
        'codes': [
            [0, {'text': 'class ', 'Color': colors['keyword']}, {'text': 'Solution:'}],
            [
                1,
                {'text': 'def ', 'Color': colors['keyword']}, {'text': 'buildTree('},
                {'text': 'self ', 'Color': colors['kwargs']}, {'text': ', preorder, inorder):'},
            ],
            [
                2,
                {'text': 'def ', 'Color': colors['keyword']},
                {'text': 'rebuild(idx_preorder_left, idx_preorder_right, idx_inorder_left, idx_inorder_right):'},
            ],
            [
                3,
                {'text': 'if ', 'Color': colors['keyword']}, {'text': 'idx_preorder_left > idx_preorder_right:'},
            ],
            [
                4,
                {'text': 'return None', 'Color': colors['keyword']},
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
                {'text': 'idx_preorder_left + '}, {'text': '1', 'Color': colors['number']},
                {'text': ', idx_preorder_left + size_of_left_subtree,'},
            ],
            [
                4,
                {'text': 'idx_inorder_left, idx_inorder_root - '}, {'text': '1', 'Color': colors['number']},
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
                {'text': 'idx_preorder_left + size_of_left_subtree + '}, {'text': '1', 'Color': colors['number']},
                {'text': ', idx_preorder_right,'},
            ],
            [
                4,
                {'text': 'idx_inorder_root + '}, {'text': '1', 'Color': colors['number']}, {'text': ', idx_inorder_right'},
            ],
            [
                3,
                {'text': ')'},
            ],
            [3, {'text': 'return ', 'Color': colors['keyword']}, {'text': 'root'}],
            [],
            [2, {'text': 'idx_preorder_start = '}], {'text': '0', 'Color': colors['number']},
            [2, {'text': 'idx_preorder_end = '}, {'text': 'len', 'Color': colors['builtin']}, {'text': '(preorder)'}],
            [2, {'text': 'idx_inorder_start = '}], {'text': '0', 'Color': colors['number']},
            [2, {'text': 'idx_inorder_end = '}, {'text': 'len', 'Color': colors['builtin']}, {'text': '(inorder)'}],
            [],
            [
                2,
                {'text': 'idx_dic = {element: i '}, {'text': 'for', 'Color': colors['keyword']}, {'text': ' i, element '},
                {'text': 'in ', 'Color': colors['keyword']}, {'text': 'enumerate', 'Color': colors['builtin']},
                {'text': '(inorder)'}
            ],
            [
                2,
                {'text': 'return ', 'Color': colors['keyword']},
                {'text': 'rebuild(idx_preorder_start, idx_preorder_end, idx_inorder_start, idx_inorder_end)'}
            ],
            [],
            [],
            [
                0,
                {'text': 'print ', 'Color': colors['builtin']}, {'text': '(Solution().buildTree('},
                {'text': 'preorder', 'Color': colors['kwargs']}, {'text': '=['},
                {'text': '3', 'Color': colors['number']}, {'text': ', '}, {'text': '9', 'Color': colors['number']},
                {'text': ', '}, {'text': '20', 'Color': colors['number']}, {'text': ', '},
                {'text': '15', 'Color': colors['number']}, {'text': ', '}, {'text': '7', 'Color': colors['number']},
                {'text': '], '},
                {'text': 'inorder', 'Color': colors['kwargs']}, {'text': '=['},
                {'text': '9', 'Color': colors['number']}, {'text': ', '}, {'text': '3', 'Color': colors['number']},
                {'text': ', '}, {'text': '15', 'Color': colors['number']}, {'text': ', '},
                {'text': '20', 'Color': colors['number']}, {'text': ', '}, {'text': '7', 'Color': colors['number']},
                {'text': ']))'},
            ],
        ],
        'subtitles': subtitles,
        'annotations': [
            {
                'name': 'Linus Torvalds名言', 'text': '"Talk is cheap, show me the code!"',
                'Position': [960, 450],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
        ],
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
