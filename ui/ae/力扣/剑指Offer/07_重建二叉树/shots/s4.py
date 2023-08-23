from .consts import ASSETS_DIR
from .transcript import subtitles as all_subtitles
from utils_v0.py.audio import audios_subtitles

sn = 0
prefix = f's{sn}'


def shot_3(start_time):
    sn = 3
    prefix = f'{name}.{sn}'
    subtitles = []
    for i, text in enumerate(scene[3]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1] + SUBTITLES_INTERVAL
    duration = end_time - start_time

    conf = {
        'layerName': prefix, 'startTime': start_time, 'duration': duration,
        'subtitles': subtitles,
        'texts': [
            {
                'name': '限制条件', 'box': 'true', 'rect': [1500, 300],
                'text': '限制条件：0 <= 节点个数 <= 5000\n我们实现算法时需要根据限制条件考虑时间复杂度和空间复杂度问题\n否则即使本地调试通过，提交到力扣依然会因为复杂度太高而无法通过全部测试用例',
                'Position': [960, 200], 'font': FONTS["cn"],
                'presets': [
                    {
                        'path': 'D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/Text/Multi-Line/Word Processor.ffx',
                        'keyframes': {'Type_on.Slider': [[0, duration], [0, 100], None, True]}
                    }
                ]
            },
        ],
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf_0 = shot_0(start_time)
    conf_1 = shot_1(conf_0['end_time'])
    conf_2 = shot_2(conf_1['end_time'])
    conf_3 = shot_3(conf_2['end_time'])
    return name, [conf_0, conf_1, conf_2, conf_3], conf_3['end_time']
