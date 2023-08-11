from glob import glob
import os

from moviepy.audio.io.AudioFileClip import AudioFileClip


audio_files = glob('*.wav')
print(audio_files)
for af in audio_files:
    snd = AudioFileClip(af)
    snd.write_audiofile(os.path.join('audios', f"{''.join(af.split('.')[:-1])}.mp3"))
    snd.close()
