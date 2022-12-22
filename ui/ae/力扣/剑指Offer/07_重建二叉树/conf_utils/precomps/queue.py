import math


def preorder():
    original_width = 108
    scale = [80, 80]
    elem_width = original_width * scale[0] / 100
    height = math.ceil(elem_width)
    conf = {
        'name': 'preorder', 'type': 'QUEUE', 'Position': [960, 800, 0], 'elems': [3, 9, 20, 15, 7], 'width': math.ceil(elem_width * 5),
        'height': height,
        'duration': 30, 'startTime': 1,
        'unit': {'name': 'Queue Unit Blue/Elements.ai', 'elemWidth': elem_width, 'Size': [elem_width, height]},
        'effects': {'ADBE Drop Shadow': {}},
        'keyframes': {
            # 'Contents.Group 1.Contents.Fill 1.Color': [
            #     ([1, 2, 3], ['#0573E1', '#0573E1', '#FFFFFF']),
            #     ([2, 3, 4], ['#0573E1', '#0573E1', '#FFFFFF']),
            #     ([3, 4, 5], ['#0573E1', '#0573E1', '#FFFFFF']),
            #     ([4, 5, 6], ['#0573E1', '#0573E1', '#FFFFFF']),
            #     ([5, 6, 7], ['#0573E1', '#0573E1', '#FFFFFF'])
            # ],
            # 'Transform.Opacity': [
            #     ([0, 1, 2, 7], [0, 0, 100, 0]),
            #     ([1, 2, 3, 8], [0, 0, 100, 0]),
            #     ([2, 3, 4, 9], [0, 0, 100, 0]),
            #     ([3, 4, 5, 10], [0, 0, 100, 0]),
            #     ([4, 5, 6, 11], [0, 0, 100, 0]),
            # ]
        }
    }
    return conf


def inorder():
    original_width = 108
    scale = [80, 80]
    elem_width = original_width * scale[0] / 100
    height = math.ceil(elem_width)
    conf = {
        'name': 'inorder', 'type': 'QUEUE', 'Position': [960, 900, 0], 'elems': [9, 3, 15, 20, 7],
        'width': math.ceil(elem_width * 5),
        'height': height,
        'duration': 30, 'startTime': 1,
        'unit': {'name': 'Queue Unit Purple/Elements.ai', 'elemWidth': elem_width, 'Size': [elem_width, height]},
        'effects': {'ADBE Drop Shadow': {}},
        'keyframes': {
            # 'Contents.Group 1.Contents.Fill 1.Color': [
            #     ([1, 2, 3], ['#0573E1', '#0573E1', '#FFFFFF']),
            #     ([2, 3, 4], ['#0573E1', '#0573E1', '#FFFFFF']),
            #     ([3, 4, 5], ['#0573E1', '#0573E1', '#FFFFFF']),
            #     ([4, 5, 6], ['#0573E1', '#0573E1', '#FFFFFF']),
            #     ([5, 6, 7], ['#0573E1', '#0573E1', '#FFFFFF'])
            # ],
            # 'Transform.Opacity': [
            #     ([0, 1, 2, 7], [0, 0, 100, 0]),
            #     ([1, 2, 3, 8], [0, 0, 100, 0]),
            #     ([2, 3, 4, 9], [0, 0, 100, 0]),
            #     ([3, 4, 5, 10], [0, 0, 100, 0]),
            #     ([4, 5, 6, 11], [0, 0, 100, 0]),
            # ]
        }
    }
    return conf


def create_all():
    return [preorder(), inorder()]
    # return [inorder()]
    # return []
