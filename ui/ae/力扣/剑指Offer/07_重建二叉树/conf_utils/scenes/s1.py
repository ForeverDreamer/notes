from .transcript import scenes
from ae.constants.share import *
from ae.utils.py.color import hex_to_rgb1

name = 's1'
scene = scenes[name]

def shot_0(start_time):
    subtitles = []
    for i, text in enumerate(scene[0]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]
    conf = {
        'subtitles': subtitles,
        'annotations': [
            {
                'name': '题目描述', 'box': 'true', 'rect': [1500, 300],
                'text': '输入某二叉树的前序遍历和中序遍历的结果\n请构建该二叉树并返回其根节点\n假设输入的前序遍历和中序遍历的结果中都不含重复的数字',
                'Position': [960, 200, 0], 'span': {'inPoint': start_time, 'outPoint': end_time}, 'font': FONTS["cn"],
                'presets': [
                    {
                        'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Text/Multi-Line/Word Processor.ffx',
                        'keyframes': {'Type_on.Slider': {'times': [start_time, end_time], 'values': [0, 90]}}
                    }
                ]
            },
        ],
        'end_time': end_time,
    }
    return conf


def shot_1(start_time):
    subtitles = []
    for i, text in enumerate(scene[1]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]
    conf = {
        'subtitles': subtitles,
        'annotations': [
            {
                'name': '示例1', 'box': 'true', 'rect': [1000, 300],
                'text': 'Input: preorder = [3,9,20,15,7]\nInput: inorder = [9,3,15,20,7]\nOutput: [3,9,20,null,null,15,7]',
                'Position': [960, 200], 'span': {'inPoint': start_time, 'outPoint': end_time+9}, 'font': FONTS["cn"],
                'presets': [
                    {
                        'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Text/Multi-Line/Word Processor.ffx',
                        'keyframes': {'Type_on.Slider': {'times': [start_time, end_time], 'values': [0, 100]}}
                    }
                ]
            },
        ],
        'precomps': [
            {
                'name': '示例1.二叉树', 'type': 'BINARY_TREE', 'width': 500, 'height': 500,
                'duration': 8, 'Position': [960, 600], 'elems': [[3], [9], [20], ['null'], ['null'], [15], [7]], 'startTime': end_time+1,
                'animation': 'true',
                'node': {
                    'shape': {'name': 'Node Shape Black/Elements.ai', 'Scale': [80, 80, 80]},
                },
                'edge': {
                    'shape': {'name': 'Edge Black/Elements.ai', 'Anchor Point': 'TOP', 'Scale': [80, 80, 80], 'Rotation': 30},
                },
                # '3D': 'true'
            }
        ],
        'end_time': end_time+9,
    }
    return conf


def shot_2(start_time):
    subtitles = []
    for i, text in enumerate(scene[2]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]
    conf = {
        'subtitles': subtitles,
        'annotations': [
            {
                'name': '示例 2', 'box': 'true', 'rect': [1500, 300],
                'text': '示例 2\n如果前序遍历的结果是[-1]，中序遍历的结果是[-1]\n重建出来的二叉树为[-1]\n此种为空树情况',
                'Position': [960, 200], 'span': {'inPoint': start_time, 'outPoint': end_time}, 'font': FONTS["cn"],
                'presets': [
                    {
                        'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Text/Multi-Line/Word Processor.ffx',
                        'keyframes': {'Type_on.Slider': {'times': [start_time, end_time], 'values': [0, 90]}}
                    }
                ]
            },
        ],
        'end_time': end_time,
    }
    return conf


def shot_3(start_time):
    subtitles = []
    for i, text in enumerate(scene[3]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]
    conf = {
        'subtitles': subtitles,
        'annotations': [
            {
                'name': '限制条件', 'box': 'true', 'rect': [1500, 300],
                'text': '限制条件：0 <= 节点个数 <= 5000\n我们实现算法时需要根据限制条件考虑时间复杂度和空间复杂度问题\n否则即使本地调试通过，提交到力扣依然会因为复杂度太高而无法通过全部测试用例',
                'Position': [960, 200], 'span': {'inPoint': start_time, 'outPoint': end_time}, 'font': FONTS["cn"],
                'presets': [
                    {
                        'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Text/Multi-Line/Word Processor.ffx',
                        'keyframes': {'Type_on.Slider': {'times': [start_time, end_time], 'values': [0, 90]}}
                    }
                ]
            },
        ],
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    conf_1 = shot_1(conf_0['end_time'] + 1)
    conf_2 = shot_2(conf_1['end_time'] + 1)
    return name, [conf_0, conf_1, conf_2], conf_2['end_time']
