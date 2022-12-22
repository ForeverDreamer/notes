from ae.utils.py.color import hex_to_rgb1


def preorder():
    basic = {
        'name': 'preorder', 'type': 'BINARY_TREE', 'width': 500, 'height': 500, 'duration': 30,
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
            'Color': hex_to_rgb1('#B5FF6A'),
            'Stroke Width': 5,
            'Offset': -180,
            'effects': ['ADBE Glo2'],
            'keyframes': [
                {
                    'Contents.Group 1.Contents.Trim Paths 1.Start': [[i * 1, i * 1 + 0.5], [50, 0]],
                    'Contents.Group 1.Contents.Trim Paths 1.End': [[i * 1, i * 1 + 0.5], [50, 100]],
                }
                for i in range(len_elems)
            ],
            'sound': {
                'name': 'SFX - Magic 25.wav',
                'startTimes': [i * 1 for i in range(len_elems)]
            }
        },
    }
    conf = {
        # 可以用AtomX或其它插件的precomp,preset,effets替换
        'selected': {
            'name': 'Node Green/Elements.ai', 'scale': [80, 80, 80],
        },
        'node': node,
        'edge': {
            'name': 'Edge/Elements.ai', 'anchor': 'TOP', 'scale': [80, 80, 80], 'rotation': 30,
            'Path': {
                'vertices': [[153, 95], [88, 211]],
                'closed': 'false',
                'Color': hex_to_rgb1('#B5FF6A'),
                'Stroke Width': 5,
                'effects': ['ADBE Glo2'],
                'sound': {
                    'name': 'SFX - Fast Swoosh 15.wav',
                    'startTimes': [i * 1 + 0.5 for i in range(len_elems - 1)]
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
        'name': 'inorder', 'type': 'BINARY_TREE', 'width': 500, 'height': 800, 'duration': 30,
        'Position': [390, 500, 0], 'elems': [3, 9, 20, 'null', 'null', 15, 7], 'startTime': 1,
        # 'pos': [1420, 500, 0], 'elems': [3, 9, 20, 'null', 'null', 15, 7], 'startTime': 1,
    }
    # len_elems = len(basic['elems']) - basic['elems'].count('null')
    conf = {
        'node': {
            'shape': {'name': 'Node White/Elements.ai', 'Scale': [80, 80, 80]},
            # 可以用AtomX或其它插件的precomp,preset,effets替换
            'selected': {
                'name': 'Node Green/Elements.ai', 'Scale': [80, 80, 80], 'Opacity': 0,
            },
            'drop': {
                "pathGroup": {
                    "type": "Group",
                    "vertices": [[0, -50], [50, 0], [0, 50], [-50, 0]],
                    "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0],
                                   [0, 27.6142425537109]],
                    "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0],
                                    [0, -27.6142425537109]],
                    "closed": 'true'
                },
                "Fill": {"Color": hex_to_rgb1("#7EE787")},
                'Opacity': 0,
            },
            'path': {
                "pathGroup": {
                    "type": "Group",
                    'vertices': [[0, -50], [50, 0], [0, 50], [-50, 0]],
                    'inTangents': [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0],
                                   [0, 27.6142425537109]],
                    'outTangents': [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0],
                                    [0, -27.6142425537109]],
                    "closed": 'true'
                },
                "Stroke": {
                    'Stroke Width': 5,
                    "Color": hex_to_rgb1("#F8F9FB")
                },
                "Trim Paths": {
                    'Start': 50,
                    'End': 50,
                    'Offset': -135,
                },
                'effects': {'ADBE Glo2': {}},
            },
        },
        'edge': {
            'shape': {'name': 'Edge/Elements.ai', 'Anchor Point': 'TOP', 'Scale': [80, 80, 80], 'Rotation': 30},
            'path': {
                "pathGroup": {
                    'vertices': [[153, 95], [88, 211]],
                    'closed': 'false',
                },
                "Stroke": {
                    'Stroke Width': 5,
                    "Color": hex_to_rgb1("#F8F9FB")
                },
                "Trim Paths": {
                    'End': 0,
                },
                'effects': {'ADBE Glo2': {}},
            },
        },
        'effects': {},
        # 'keyframes': [{'Opacity': [[0, 1, 2], [0, 0, 100]]}],
        # '3D': 'true'
    }
    return {**basic, **conf}


def create_all():
    # confs = [preorder(), inorder()]
    confs = [inorder()]
    return confs
