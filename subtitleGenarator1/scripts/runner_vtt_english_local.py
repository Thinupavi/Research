import os
import time

from docutils.nodes import target
from webvtt import WebVTT, Caption

from scripts.audio2text_cog import Microsoft_ASR
from scripts.translate import TRANSLATR_TO_TEXT
from scripts.extractCaption import Extract_Caption
import scripts.extractWavAudio as extractWavAudio
from scripts.audiosplit import AudioSplit
import glob
from threading import Thread

ext_cap = Extract_Caption()
ms_asr = Microsoft_ASR()
ms_asr.get_speech_token()
TTT = TRANSLATR_TO_TEXT()


def genarateSUB(filePath, fileName, lang):
    captionTitle = fileName
    language = lang
    # fine If any english captions available in the yputube url video

    wavFilePath = extractWavAudio.extract_wav_fromFile(filePath, fileName)

    # spliting the audio file in to multiple audio
    AudioSplit.split(wavFilePath, captionTitle)

    # initiate the subtitle file path
    vtt = WebVTT()

    # initiate slite wav file
    num_files = len(os.listdir('../Datas/Splits/' + captionTitle + '/'))

    cnt = 0
    start = 0
    end = 5
    for i in range(1, num_files + 1):

        flag = 0
        text, confidence = ms_asr.transcribe('../Datas/Splits/' + captionTitle + '/' + str(i) + '.wav')
        print("Text: ", text)
        print("Confidence: ", confidence)
        if text == " ":
            translated_text = " "
        else:
            # translated_text = TRANSLATR_TO_TEXT.translateFromTXT(text, language)
            translated_text = text
            flag = 1
            cnt += 1
        print("Translated Text: ", translated_text)
        if flag == 1:
            start_hours = start // 3600
            temp = start % 3600
            start_min = temp // 60
            start_sec = temp % 60
            end_hours = end // 3600
            temp = end % 3600
            end_min = temp // 60
            end_sec = temp % 60

            if (start_hours <= 9):
                start_hours = '0' + str(start_hours)
            else:
                start_hours = str(start_hours)
            if (start_min <= 9):
                start_min = '0' + str(start_min)
            else:
                start_min = str(start_min)
            if (start_sec <= 9):
                start_sec = '0' + str(start_sec)
            else:
                start_sec = str(start_sec)

            if (end_hours <= 9):
                end_hours = '0' + str(end_hours)
            else:
                end_hours = str(end_hours)
            if (end_min <= 9):
                end_min = '0' + str(end_min)
            else:
                end_min = str(end_min)
            if (end_sec <= 9):
                end_sec = '0' + str(end_sec)
            else:
                end_sec = str(end_sec)

            caption = Caption(start_hours + ':' + start_min + ':' + start_sec + '.001 ',
                              end_hours + ':' + end_min + ':' + end_sec + '.000\n', str(translated_text) + '\n')

            vtt.captions.append(caption)
        start += 5
        end += 5

    vttFilePath = "../webApp/static/SubtitleFile/" + captionTitle + "_" + language + ".vtt"
    vtt.save(vttFilePath)
    vttName = captionTitle + "_" + language + ".vtt"
    files = glob.glob('../Datas/Splits/' + captionTitle + '/*')
    for f in files:
        os.remove(f)
    os.rmdir('../Datas/Splits/' + captionTitle)
    os.remove(wavFilePath)

    return vttName

