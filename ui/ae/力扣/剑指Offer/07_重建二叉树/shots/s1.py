from constants.share import FONTS
from .consts import ASSETS_DIR
from .transcript_cn import subtitles as all_subtitles_cn
from .transcript_en import subtitles as all_subtitles_en
from utils_v0.py.audio import audios_subtitles

sn = 1
prefix = f's{sn}'


def build_conf(start_time):
    all_subtitles = list(map(list, zip(all_subtitles_cn[sn], all_subtitles_en[sn])))
    audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles, start_time)
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
                'name': f'{prefix}.题目描述', 'box': True, 'rect': [1500, 300],
                'text': '输入某二叉树的前序遍历和中序遍历结果\n请构建该二叉树并返回其根节点\n假设输入的前序遍历和中序遍历的结果中\n都不含重复的数字',
                'Position': [960, 200, 0], 'font': FONTS["cn"],
                'presets': [
                    {
                        'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Text/Multi-Line/Word Processor.ffx',
                        'keyframes': {'Type_on.Slider': [[0, duration], [0, 90], None, True]}
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
