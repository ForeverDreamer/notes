from constants.share import COLORS
from .consts import ASSETS_DIR
from .transcript import subtitles as all_subtitles
from utils_v0.py.audio import audios_subtitles
from utils_v0.py.color import hex_to_rgb1

sn = 11
prefix = f's{sn}'


def build_conf(start_time):
    audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles[sn], start_time)
    LEETCODE_TIME = 18
    START_IDX = 0
    for i in range(START_IDX, len(subtitles[0])):
        subtitles[0][i] += LEETCODE_TIME
    for i in range(START_IDX, len(audios)):
        audios[i]['layers'][0]['startTime'] += LEETCODE_TIME
    for i in range(START_IDX, len(l_times)):
        l_times[i] += LEETCODE_TIME
    end_time += LEETCODE_TIME
    duration = end_time - start_time

    conf = {
        'layerName': prefix, 'startTime': start_time, 'duration': duration,
        'subtitles': subtitles,
        'files': [
            {
                'folder': 'audios',
                'files': audios,
            },
            {
                'path': f'{ASSETS_DIR}/代码提交力扣执行过程.mp4',
                'layers': [
                    {
                        'sourceName': '代码提交力扣执行过程.mp4',
                        'layerName': f'{prefix}.代码提交力扣执行过程',
                        # 'Scale': [90, 90, 90],
                        'Position': [960, 540],
                    }
                ],
            }
        ],
        'shapes': [
            {
                'layerName': f'{prefix}.任务栏.遮罩',
                'Position': [960, 1061.5],
                'adjustmentLayer': True,
                'pathGroup': {'type': 'Rect', 'Size': [1920, 40]},
                'Fill': {'Color': hex_to_rgb1(COLORS['bg'])},
                'effects': {
                    "ADBE Box Blur2": {'props': {'Blur Radius': 10}}
                }
            },
            {
                'layerName': f'{prefix}.浏览器.遮罩',
                'Position': [960, 52.7],
                'adjustmentLayer': True,
                'pathGroup': {'type': 'Rect', 'Size': [1920, 106]},
                'Fill': {'Color': hex_to_rgb1(COLORS['bg'])},
                'effects': {
                    "ADBE Box Blur2": {'props': {'Blur Radius': 10}}
                },
                'keyframes': {
                    "Opacity": [
                        [0, 6.17],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            },
            {
                'layerName': f'{prefix}.运行结果.遮罩',
                'Position': [284.2, 821],
                'adjustmentLayer': True,
                'pathGroup': {'type': 'Rect', 'Size': [500, 65]},
                'Fill': {'Color': hex_to_rgb1(COLORS['bg'])},
                'effects': {
                    "ADBE Box Blur2": {'props': {'Blur Radius': 10}}
                },
                'keyframes': {
                    "Opacity": [
                        [0, 17.33],
                        [0, 100],
                        {"spatial": [{"type": 'HOLD'}] * 2}
                    ]
                },
            }
        ],
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf = build_conf(start_time)
    return sn, conf, conf['end_time']
