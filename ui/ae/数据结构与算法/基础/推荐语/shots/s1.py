from .consts import ASSETS_DIR
# from .transcript_cn import subtitles as all_subtitles_cn
# from .transcript_en import subtitles as all_subtitles_en
from utils.py.audio import audios_subtitles

sn = 1
prefix = f's{sn}'


def build_conf(start_time):
    # all_subtitles = list(map(list, zip(all_subtitles_cn[sn], all_subtitles_en[sn])))
    # audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles, start_time)
    # duration = end_time - start_time
    end_time = 30
    duration = 30

    conf = {
        'layerName': prefix, 'startTime': start_time, 'duration': duration,
        # 'subtitles': subtitles,
        # 'files': [
        #     {
        #         'folder': 'audios',
        #         'files': audios,
        #     },
        #     {
        #         'path': f'{ASSETS_DIR}/题目描述.jpg',
        #         'layers': [
        #             {
        #                 'sourceName': '题目描述.jpg',
        #                 'layerName': f'{prefix}.题目描述',
        #                 'Scale': [90, 90, 90],
        #                 'Position': [960, 540],
        #                 'startTime': start_time,
        #                 # 'span': {'inPoint': start_time, 'outPoint': end_time},
        #             }
        #         ],
        #     }
        # ],
        'end_time': end_time,
    }
    return conf


def build(start_time):
    conf = build_conf(start_time)
    return sn, conf, conf['end_time']
