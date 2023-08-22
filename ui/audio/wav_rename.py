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
i = 0

while i < len(names):
    audio_file = names[i][-1]
    shot = audio_file.split('.')[0].split('#')[0]
    target_name = f'{shot}.{i}.wav'
    print(target_name)
    os.rename(audio_file, os.path.join('audios', target_name))
    i += 1
