from ae.constants.share import *
from .transcript import scenes


name = 's6'


def shot_0(start_time):
    subtitles = []
    for i, text in enumerate(scenes[name][0]):
        subtitles.append([start_time+i*SUBTITLES_INTERVAL, text])
        i += 1
    subtitles = list(map(list, zip(*subtitles)))
    end_time = subtitles[0][-1]+SUBTITLES_INTERVAL
    conf = {
        'images': [
            {
                'name': 'Linus Torvalds.jfif',
                'layerName': 'Linus Torvalds.jfif',
                'Scale': [75, 75, 75],
                'Position': [920, 210],
                'startTime': start_time,
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
            {
                'name': 'linux.png',
                'layerName': 'linux.png',
                'Scale': [50, 50, 50],
                'Position': [390, 730],
                'startTime': start_time,
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
            {
                'name': 'git.bmp',
                'layerName': 'git.bmp',
                'Scale': [50, 50, 50],
                'Position': [1475, 730],
                'startTime': start_time,
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
        ],
        'subtitles': subtitles,
        'annotations': [
            {
                'name': 'Linus Torvalds名言', 'text': '"Talk is cheap, show me the code!"',
                'Position': [960, 450],
                'span': {'inPoint': start_time, 'outPoint': end_time},
            },
        ],
        'end_time': end_time,
    }
    return conf


def create_all(start_time):
    conf_0 = shot_0(start_time)
    return name, [conf_0], conf_0['end_time']
