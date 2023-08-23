from glob import glob
from operator import itemgetter

from mutagen.wave import WAVE

from constants.share import SHOTS_INTERVAL


def audios_subtitles(path, raw_subtitles):
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
    start_time = 0
    for i, af in enumerate(names):
        audio = WAVE(af[-1])
        audios.append(
            {
                'path': af[-1],
                'layers': [
                    {
                        'sourceName': af[-1].split('\\')[-1],
                        'startTime': start_time,
                        'Anchor Point': None,
                    }
                ],
            }
        )
        subtitles.append([start_time, raw_subtitles[i]])
        start_time += audio.info.length + 0.5

    subtitles = list(zip(*subtitles))
    end_time = start_time + SHOTS_INTERVAL
    return audios, subtitles, end_time
