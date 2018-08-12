from pytube import YouTube
import glob, os
import subprocess


def extractWAV(url):
    yt = YouTube(url)
    # listing Available files in audio url
    audioMP4 = yt.streams.filter(only_audio=True).all()

    try:
        audiDownloadPath = '../Datas/ExtractAudio/'
        print('Extracting Audio..................')
        print('Please wait ......................')
        title = yt.title.replace(" ", "").replace("'", "").replace('"','')
        mp4Title = audiDownloadPath + title + '.mp4'
        wavTitle = audiDownloadPath + title + '.wav'
        print('Downloading Audio..................')

        audioMP4[0].download(audiDownloadPath, filename=title)
        # os.rename(audiDownloadPath + yt.title + '.mp4', mp4Title)

        print('Audio mp4 downloaded Successfully')
        print('Start converting mp4 to wave')

        subprocess.call('ffmpeg -i ' + mp4Title + ' ' + wavTitle + '', shell=True)
        print('Done')
        os.remove(mp4Title)
    except Exception as e:
        print(e)
    return str(wavTitle)



def extract_wav_fromFile(filePath,filename):
    audiDownloadPath = '../Datas/ExtractAudio/'
    title = filename.replace(" ", "").replace("'", "").replace('"', '')
    wavTitle = audiDownloadPath + title + '.wav'
    subprocess.call('ffmpeg -i ' + filePath + ' ' + wavTitle + '', shell=True)
    return str(wavTitle)


if __name__ == '__main__':
    extract_wav_fromFile('C:/xampp/htdocs/SubtitleGenaretor/Videos//IntroducingGoogleGnome.mp4','IntroducingGoogleGnome')
