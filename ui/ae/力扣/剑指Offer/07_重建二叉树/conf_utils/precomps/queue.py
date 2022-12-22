import math

from ae.utils.py.color import hex_to_rgb1


def preorder():
    elem_width = 80
    height = 80
    conf = {
        'name': 'preorder', 'type': 'QUEUE', 'Position': [960, 800, 0], 'elems': [3, 9, 20, 15, 7],
        'width': elem_width * 5,
        'height': height,
        'duration': 30, 'startTime': 1,
        'unit': {
            'pathGroup': {'type': 'Rect', 'Size': [elem_width, height]},
            "Fill": {"Color": hex_to_rgb1("#7EE787")},
            "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#F8F9FB")},
        },
        'effects': {'ADBE Drop Shadow': {}},
    }
    return conf


def inorder():
    elem_width = 80
    height = 80
    conf = {
        'name': 'inorder', 'type': 'QUEUE', 'Position': [353, 848, 0], 'elems': [9, 3, 15, 20, 7],
        'width': elem_width * 5,
        'height': height,
        'duration': 30, 'startTime': 1,
        'unit': {
            'pathGroup': {'type': 'Rect', 'Size': [elem_width, height]},
            "Fill": {"Color": hex_to_rgb1("#7EE787")},
            "Stroke": {'Stroke Width': 5, "Color": hex_to_rgb1("#F8F9FB")},
        },
        'effects': {'ADBE Drop Shadow': {}},
    }
    return conf


def create_all():
    # return [preorder(), inorder()]
    return [inorder()]
    # return []
