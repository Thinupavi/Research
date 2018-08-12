from pytube import YouTube
import glob, os
import subprocess


def extractWAV(url):
    yt = YouTube(url)
    #listing Available files in audio url
    audioMP4 = yt.streams.filter(only_audio=True).all()

    try:
        audiDownloadPath = '../Datas/ExtractAudio/'

        print('Extracting Audio..................')
        print('Please wait ......................')
        audioMP4[0].download(audiDownloadPath)

        mp4Title = audiDownloadPath + yt.title.replace(" ", "") + '.mp4'
        wavTitle = audiDownloadPath + yt.title.replace(" ", "") + '.wav'

        os.rename(audiDownloadPath + yt.title + '.mp4', mp4Title)

        print('Audio mp4 downloaded Successfully')
        print('Start converting mp4 to wave')

        subprocess.call('ffmpeg -i ' + mp4Title + ' ' + wavTitle + '', shell=True)
        print('Done')
        os.remove('../Datas/ExtractAudio/' + mp4Title)
    except Exception as e:
        print(e)
    return str(wavTitle)


if __name__ == '__main__':
    extractWAV('https://www.youtube.com/watch?v=vNOllWX-2aE')
