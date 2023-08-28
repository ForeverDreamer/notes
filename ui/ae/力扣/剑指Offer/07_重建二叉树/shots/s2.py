from constants.share import FONTS
from .consts import ASSETS_DIR
from .transcript_cn import subtitles as all_subtitles_cn
from .transcript_en import subtitles as all_subtitles_en
from utils_v0.py.audio import audios_subtitles

sn = 2
prefix = f's{sn}'


def build_conf(start_time):
    all_subtitles = list(map(list, zip(all_subtitles_cn[sn], all_subtitles_en[sn])))
    audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles, start_time)
    end_time += 5
    duration = end_time - start_time

    conf = {
        'layerName': prefix, 'startTime': start_time, 'duration': duration,
        'subtitles': subtitles,
        'files': [
            {
                'folder': 'audios',
                'files': audios,
            },
        ],
        'texts': [
            {
                'name': f'{prefix}.示例1', 'box': True, 'rect': [1000, 300],
                'text': 'Input: preorder = [3,9,20,15,7]\nInput: inorder = [9,3,15,20,7]\nOutput: [3,9,20,null,null,15,7]',
                'Position': [960, 200], 'font': FONTS["cn"],
                'presets': [
                    {
                        'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Text/Multi-Line/Word Processor.ffx',
                        'keyframes': {'Type_on.Slider': [[0, l_times[-1]], [0, 100], None, True]}
                    }
                ]
            },
        ],
        'dsa': [
            {
                'layerName': f'{prefix}.示例1.二叉树', 'type': 'BINARY_TREE', 'width': 500, 'height': 500,
                'startTime': l_times[-1], 'duration': 5, 'Position': [960, 600], 'rootNodePos': [186, 60],
                'elems': [{'key': 3}, {'key': 9}, {'key': 20}, {'key': None}, {'key': None}, {'key': 15}, {'key': 7}],
                'animation': True,
                'node': {
                    'shape': {'sourceName': 'Node Shape Black/Elements.ai', 'Scale': [80, 80, 80]},
                },
                'edge': {
                    'shape': {'sourceName': 'Edge Black/Elements.ai', 'Anchor Point': 'TOP', 'Scale': [80, 80, 80], 'Rotation': 30},
                },
                # '3D': 'true'
            }
        ],
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf = build_conf(start_time)
    return sn, conf, conf['end_time']
