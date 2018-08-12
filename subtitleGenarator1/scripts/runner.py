import os
from audio2text_cog import Microsoft_ASR
from translate import TRANSLATR_TO_TEXT
from houndify_STT import HOUNDIFY_STT
from extractCaption import Extract_Caption
import extractWavAudio
from audiosplit import AudioSplit
import glob

ext_cap = Extract_Caption()
ms_asr = Microsoft_ASR()
ms_asr.get_speech_token()
TTT = TRANSLATR_TO_TEXT()

url = "https://www.youtube.com/watch?v=vNOllWX-2aE"
language = "si"
# fine If any english captions available in the yputube url video
captionTitle = Extract_Caption.extractTitle(url)
# if captionTXT is not None:
#     translate_caption_text = TRANSLATR_TO_TEXT.translateFromTXT(captionTXT, language)
#     file_str = open("../Datas/SubtitleFile/" + captionTitle + ".srt", "w", encoding="utf-16")
#     file_str.write(translate_caption_text)
#     file_str.close()
#
# else:
wavFilePath = extractWavAudio.extractWAV(url);
#spliting the audio file in to multiple audio
AudioSplit.split(wavFilePath)

#initiate the subtitle file path
file_str = open("../Datas/SubtitleFile/" + captionTitle + ".srt", "w", encoding="utf-16")

#initiate slite wav file
num_files = len(os.listdir('../Datas/Splits/'))

cnt = 0
start = 0
end = 5
for i in range(1, num_files + 1):
    flag = 0
    text, confidence = ms_asr.transcribe('../Datas/Splits/' + str(i) + '.wav')
    print("Text: ", text)
    print("Confidence: ", confidence)
    if text == " ":
        translated_text = " "
    else:
        translated_text = TRANSLATR_TO_TEXT.translateFromTXT(text, language)
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

        file_str.write(str(cnt) + "\n")
        file_str.write(
            start_hours + ':' + start_min + ':' + start_sec + ',001 --> ' + end_hours + ':' + end_min + ':' + end_sec + ',000\n')
        file_str.write(str(translated_text) + '\n')
        file_str.write('\n')
    start += 5
    end += 5

file_str.close()
files = glob.glob('../Datas/Splits/*')
for f in files:
    os.remove(f)
os.rmdir('../Datas/Splits/')

