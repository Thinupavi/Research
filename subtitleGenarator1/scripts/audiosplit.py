from pydub import AudioSegment
import os
import wave
import contextlib
from math import ceil


class AudioSplit():
    def split(fname,captionTitle):
        if not os.path.exists('../Datas/Splits/'+captionTitle+'/'):
            os.mkdir('../Datas/Splits/'+captionTitle+'/')

        with contextlib.closing(wave.open(fname, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            duration *= 1000
            duration = int(ceil(duration))
            print(duration)
        YOUR_AUDIO_FILE = fname
        t1 = 0  # Works in milliseconds
        t2 = 5000
        newAudio = AudioSegment.from_wav(YOUR_AUDIO_FILE)
        i = 1
        while (1):
            if (t1 > duration):
                break
            newAudio2 = newAudio[t1:t2]
            newAudio2.export('../Datas/Splits/'+captionTitle+'/' + str(i) + '.wav', format="wav")
            t1 += 5000
            t2 += 5000
            i += 1

if __name__ == '__main__':
    AudioSplit.split('https://www.youtube.com/watch?v=9No-FiEInLA','dsadsadsdasdasssdsa')
