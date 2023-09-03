from .consts import ASSETS_DIR
# from .transcript_cn import subtitles as all_subtitles_cn
# from .transcript_en import subtitles as all_subtitles_en
from utils.py.audio import audios_subtitles

sn = 0
s_name = f's{sn}'


def build_conf(start_time):
    # all_subtitles = list(map(list, zip(all_subtitles_cn[sn], all_subtitles_en[sn])))
    # audios, subtitles, end_time, l_times = audios_subtitles(f'{ASSETS_DIR}/audios/{prefix}/*.wav', all_subtitles, start_time)
    end_time = 30
    duration = end_time - start_time

    shot = [
        {
            'layerName': 's0.主标题', 'sourceName': s_name, 'parentFolderName': s_name,
            'startTime': start_time, 'duration': duration, 'Position': [400, 542.8]
        }
    ]
    return sn, shot, end_time


def build(start_time):
    return build_conf(start_time)
