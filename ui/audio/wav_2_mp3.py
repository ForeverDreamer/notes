from glob import glob
import os
from operator import itemgetter, attrgetter
from pprint import pprint as pp

from moviepy.audio.io.AudioFileClip import AudioFileClip


audio_files = glob('*.wav')
names = []
for af in audio_files:
    elems = []
    for x in af.split('.'):
        try:
            elems.append(int(x))
        except ValueError:
            pass
    elems.append(af)
    elems = tuple(elems)
    names.append(elems)


names = sorted(names, key=itemgetter(0, 1))
print(len(names))
pp(names)
sn_line = 0
sn_snippet = 0
i = 0

while i < len(names):
    audio_file = names[i][-1]
    scene = audio_file.split('.')[0].split('#')[0]
    target_name = f"{sn_line}.{sn_snippet}.mp3" if len(names[i]) == 3 else f"{sn_line}.mp3"
    target_name = f'{scene}.{target_name}'
    print(target_name)
    snd = AudioFileClip(names[i][-1])
    snd.write_audiofile(os.path.join('audios', target_name))
    snd.close()

    try:
        if names[i][0] != names[i+1][0]:
            sn_line += 1
            sn_snippet = 0
        else:
            sn_snippet += 1
    except IndexError:
        pass

    i += 1
