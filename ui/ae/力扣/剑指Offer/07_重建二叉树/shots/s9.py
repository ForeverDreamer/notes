from constants.share import FONTS
from .consts import ASSETS_DIR
from .transcript_cn import subtitles as all_subtitles_cn
from .transcript_en import subtitles as all_subtitles_en
from utils_v0.py.audio import audios_subtitles
from utils_v0.py.color import hex_to_rgb1

sn = 9
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
            {
                'path': f'{ASSETS_DIR}/Linus Torvalds.jfif',
                'layers': [
                    {
                        'sourceName': 'Linus Torvalds.jfif',
                        'layerName': f'{prefix}.Linus Torvalds',
                        'Scale': [75, 75, 75],
                        'Position': [920, 210],
                    }
                ],
            },
            {
                'path': f'{ASSETS_DIR}/linux.png',
                'layers': [
                    {
                        'sourceName': 'linux.png',
                        'layerName': f'{prefix}.linux',
                        'Scale': [50, 50, 50],
                        'Position': [390, 730],
                    }
                ],
            },
            {
                'path': f'{ASSETS_DIR}/git.bmp',
                'layers': [
                    {
                        'sourceName': 'git.bmp',
                        'layerName': f'{prefix}.git',
                        'Scale': [50, 50, 50],
                        'Position': [1475, 730],
                    }
                ],
            },
        ],
        # 'images': [
        #     {
        #         'name': 'Linus Torvalds.jfif',
        #         'layerName': f'{prefix}.Linus Torvalds.jfif',
        #         'Scale': [75, 75, 75],
        #         'Position': [920, 210],
        #         'startTime': start_time,
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        #     {
        #         'name': 'linux.png',
        #         'layerName': f'{prefix}.linux.png',
        #         'Scale': [50, 50, 50],
        #         'Position': [390, 730],
        #         'startTime': start_time,
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        #     {
        #         'name': 'git.bmp',
        #         'layerName': f'{prefix}.git.bmp',
        #         'Scale': [50, 50, 50],
        #         'Position': [1475, 730],
        #         'startTime': start_time,
        #         'span': {'inPoint': start_time, 'outPoint': end_time},
        #     },
        # ],
        'texts': [
            {
                'name': 'Linus Torvalds名言', 'text': '"Talk is cheap, show me the code!"',
                'Position': [960, 450],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
        ],
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf = build_conf(start_time)
    return sn, conf, conf['end_time']
