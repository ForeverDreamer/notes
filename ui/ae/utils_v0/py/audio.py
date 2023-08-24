from glob import glob
from operator import itemgetter

from mutagen.wave import WAVE

from constants.share import SUBTITLES_INTERVAL


def audios_subtitles(path, raw_subtitles, start_time):
    files = glob(path)
    names = []
    for f in files:
        elems = []
        for x in f.split('\\')[-1].split('.'):
            try:
                elems.append(int(x))
            except ValueError:
                pass
        elems.append(f)
        elems = tuple(elems)
        names.append(elems)

    names = sorted(names, key=itemgetter(0, 1))
    audios = []
    subtitles = []
    l_start_time = 0
    l_times = [l_start_time]
    for i, af in enumerate(names):
        audio = WAVE(af[-1])
        audios.append(
            {
                'path': af[-1],
                'layers': [
                    {
                        'sourceName': af[-1].split('\\')[-1],
                        'startTime': l_start_time,
                        'Anchor Point': None,
                    }
                ],
            }
        )
        subtitles.append([start_time, raw_subtitles[i]])
        length = audio.info.length
        start_time += length + SUBTITLES_INTERVAL
        l_start_time += length + SUBTITLES_INTERVAL
        l_times.append(l_start_time)

    subtitles = list(map(list, zip(*subtitles)))
    end_time = start_time
    return audios, subtitles, end_time, l_times
