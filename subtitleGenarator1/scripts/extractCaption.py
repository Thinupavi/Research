import base64
import codecs

from pytube import YouTube

import webvtt


class Extract_Caption():
    def extractCap(url):
        yt = YouTube(url)
        try:
            caption = yt.captions.get_by_language_code('en')
            if caption is None:
                print("NO caption available")
                return None
            else:
                captionTxt = yt.title
                # print(caption.generate_srt_captions())
                # print(captionTxt)
                return str(caption.generate_srt_captions()), captionTxt
        except Exception as e:
            print(e)

    def extractTitle(url):
        yt = YouTube(url)
        captionTxt = yt.title

        return captionTxt.replace(" ", "").replace("'", "").replace('"', '')

    def getEmbedURL(url):
        yt = YouTube(url)
        embedURL = yt.embed_html
        return embedURL

    def download_video(url):
        vidDownloadPath = 'C:/xampp/htdocs/SubtitleGenaretor/Videos/'
        yt = YouTube(url)
        title = yt.title.replace(" ", "").replace("'", "").replace('"', '')
        audioMP4 = yt.streams.filter(file_extension='mp4').all()
        # print(audioMP4)
        audioMP4[0].download(vidDownloadPath, filename=title)
        return title


if __name__ == '__main__':
    Extract_Caption.download_video('https://www.youtube.com/watch?v=9No-FiEInLA')
