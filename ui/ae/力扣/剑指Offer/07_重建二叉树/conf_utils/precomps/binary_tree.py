
def preorder():
    basic = {
        'name': '前序', 'type': 'BINARY_TREE', 'width': 500, 'height': 500, 'duration': 30,
        'pos': [390, 540, 0], 'elems': [3, 9, 20, 'null', 'null', 15, 7], 'startTime': 1,
    }
    len_elems = len(basic['elems']) - basic['elems'].count('null')

    node = {
                   'name': 'Node White/Elements.ai', 'scale': [80, 80, 80],
                   'Path': {
                       'vertices': [[0, -50], [50, 0], [0, 50], [-50, 0]],
                       'inTangents': [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0],
                                      [0, 27.6142425537109]],
                       'outTangents': [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0],
                                       [0, -27.6142425537109]],
                       'closed': 'true',
                       'Color': '#B5FF6A',
                       'Stroke Width': 5,
                       'Offset': -180,
                       'effects': ['ADBE Glo2'],
                       'keyframes': [
                           {
                               'Contents.Group 1.Contents.Trim Paths 1.Start': [[i*1, i*1+0.5], [50, 0]],
                               'Contents.Group 1.Contents.Trim Paths 1.End': [[i*1, i*1+0.5], [50, 100]],
                           }
                           for i in range(len_elems)
                       ],
                       'sound': {
                           'name': 'SFX - Magic 25.wav',
                           'startTimes': [i*1 for i in range(len_elems)]
                       }
                   },
               }
    conf = {
                # 可以用AtomX或其它插件的precomp,preset,effets替换
               'selected': {
                   'name': 'Node Green/Elements.ai', 'scale': [80, 80, 80],
                   'keyframes': {
                       'Transform.Position': [
                           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [
                               [188, 60], [188, 60], [60, 252], [60, 252], [316, 252],
                               [316, 252], [188, 444], [188, 444], [444, 444], [444, 444]
                           ]
                       ],
                       # 'Transform.Opacity': [
                       #     [0, 1, 1.1, 1.9, 2, 3, 3.1, 3.9, 4, 5, 5.1, 5.9, 6, 7, 7.1, 7.9, 8, 9],
                       #     [100, 100, 0, 0, 100, 100, 0, 0, 100, 100, 0, 0, 100, 100, 0, 0, 100, 100],
                       # ]
                   },
               },
               'tracker': {
                   'name': 'Node Tracker/Elements.ai', 'scale': [80, 80, 80],
                   'keyframes': {
                       'Transform.Position': [
                           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [
                               [188, 60], [188, 60], [60, 252], [60, 252], [316, 252],
                               [316, 252], [188, 444], [188, 444], [444, 444], [444, 444]
                           ]
                       ],
                       # 'Transform.Opacity': [
                       #     [0, 1, 1.1, 1.9, 2, 3, 3.1, 3.9, 4, 5, 5.1, 5.9, 6, 7, 7.1, 7.9, 8, 9],
                       #     [100, 100, 0, 0, 100, 100, 0, 0, 100, 100, 0, 0, 100, 100, 0, 0, 100, 100],
                       # ]
                   },
               },
               'node': node,
               'edge': {
                   'name': 'Edge/Elements.ai', 'anchor': 'TOP', 'scale': [80, 80, 80], 'rotation': 30,
                   'Path': {
                       'vertices': [[153, 95], [88, 211]],
                       'closed': 'false',
                       'Color': '#B5FF6A',
                       'Stroke Width': 5,
                       'effects': ['ADBE Glo2'],
                       'keyframes': [
                           {
                               'Contents.Group 1.Contents.Trim Paths 1.End': [[i*1+0.5, i*1+1], [0, 100]],
                           }
                           for i in range(len_elems-1)
                       ],
                       'sound': {
                           'name': 'SFX - Fast Swoosh 15.wav',
                           'startTimes': [i*1+0.5 for i in range(len_elems-1)]
                       }
                   },
               },
               'effects': [{'name': 'ADBE Drop Shadow'}],
               'keyframes': [{'Opacity': [[0, 1, 2], [0, 0, 100]]}],
               # '3D': 'true'
           }
    return {**basic, **conf}


def inorder():
    basic = {
        'name': '中序', 'type': 'BINARY_TREE', 'width': 500, 'height': 500, 'duration': 30,
        'pos': [1420, 500, 0], 'elems': [3, 9, 20, 'null', 'null', 15, 7], 'startTime': 1,
    }
    len_elems = len(basic['elems']) - basic['elems'].count('null')
    # selected_keyframes = [
    #                 {
    #                     'Transform.Opacity': [times, [0, 100]]
    #                 }
    #                 for times in [[], [1.5, 2], [], [3, 3.5]]
    #             ]
    conf = {
            # 可以用AtomX或其它插件的precomp,preset,effets替换
            'selected': {
                'name': 'Node Green/Elements.ai', 'scale': [80, 80, 80],
                'Opacity': 0,
            },
            # 'tracker': {
            #     'name': 'Node Tracker/Elements.ai', 'scale': [80, 80, 80],
            #     'keyframes': {
            #         'Transform.Position': [
            #             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            #             [
            #                 [188, 60], [188, 60], [60, 252], [60, 252], [316, 252],
            #                 [316, 252], [188, 444], [188, 444], [444, 444], [444, 444]
            #             ]
            #         ],
            #         'Transform.Opacity': [
            #             [0, 1, 1.1, 1.9, 2, 3, 3.1, 3.9, 4, 5, 5.1, 5.9, 6, 7, 7.1, 7.9, 8, 9],
            #             [100, 100, 0, 0, 100, 100, 0, 0, 100, 100, 0, 0, 100, 100, 0, 0, 100, 100],
            #         ]
            #     },
            # },
            'node': {
                'name': 'Node White/Elements.ai', 'scale': [80, 80, 80],
                'Path': {
                    'vertices': [[0, -50], [50, 0], [0, 50], [-50, 0]],
                    'inTangents': [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0], [0, 27.6142425537109]],
                    'outTangents': [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0], [0, -27.6142425537109]],
                    'closed': 'true',
                    'Color': '#B5FF6A',
                    'Stroke Width': 5,
                    'Start': 50,
                    'End': 50,
                    'Offset': -135,
                    'effects': ['ADBE Glo2'],
                    # 'keyframes': [
                    #     {
                    #         'Contents.Group 1.Contents.Trim Paths 1.Start': [[i * 1, i * 1 + 0.5], [50, 0]],
                    #         'Contents.Group 1.Contents.Trim Paths 1.End': [[i * 1, i * 1 + 0.5], [50, 100]],
                    #     }
                    #     for i in range(len_elems)
                    # ],
                },
            },
            'edge': {
                'name': 'Edge/Elements.ai', 'anchor': 'TOP', 'scale': [80, 80, 80], 'rotation': 30,
                'Path': {
                    'vertices': [[153, 95], [88, 211]],
                    'closed': 'false',
                    'Color': '#B5FF6A',
                    'Stroke Width': 5,
                    'End': 0,
                    'effects': ['ADBE Glo2'],
                    # 'keyframes': [
                    #     {
                    #         'Contents.Group 1.Contents.Trim Paths 1.End': [[i * 1 + 0.5, i * 1 + 1], [0, 100]],
                    #     }
                    #     for i in range(len_elems - 1)
                    # ],
                },
            },
            'effects': [],
            'keyframes': [{'Opacity': [[0, 1, 2], [0, 0, 100]]}],
            # '3D': 'true'
        }
    return {**basic, **conf}


def create_all():
    # confs = [preorder(), inorder()]
    confs = [inorder()]
    return confs
