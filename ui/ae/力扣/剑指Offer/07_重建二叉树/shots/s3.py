from constants.share import FONTS
from .consts import ASSETS_DIR
from .transcript import subtitles as all_subtitles
from utils_v0.py.audio import audios_subtitles

sn = 3
prefix = f's{sn}'


def build_conf(start_time):
    audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles[sn], start_time)
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
                'name': f'{prefix}.示例2', 'box': True, 'rect': [1500, 300],
                'text': '示例 2\n如果前序遍历的结果是[-1]，中序遍历的结果是[-1]\n重建出来的二叉树为[-1]\n此种为空树情况',
                'Position': [960, 200], 'font': FONTS["cn"],
                'presets': [
                    {
                        'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Text/Multi-Line/Word Processor.ffx',
                        'keyframes': {'Type_on.Slider': [[0, l_times[-1]], [0, 100], None, True]}
                    }
                ]
            },
        ],
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf = build_conf(start_time)
    return sn, conf, conf['end_time']
