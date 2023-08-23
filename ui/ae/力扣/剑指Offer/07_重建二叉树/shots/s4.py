from constants.share import FONTS
from .consts import ASSETS_DIR
from .transcript import subtitles as all_subtitles
from utils_v0.py.audio import audios_subtitles

sn = 4
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
                'name': '限制条件', 'box': True, 'rect': [1500, 300],
                'text': '限制条件：0 <= 节点个数 <= 5000\n我们实现算法时需要根据限制条件考虑时间复杂度和空间复杂度问题\n否则即使本地调试通过，提交到力扣依然会因为复杂度太高\n而无法通过全部测试用例',
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
