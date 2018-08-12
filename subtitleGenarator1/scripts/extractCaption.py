from pytube import YouTube


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
        return  captionTxt

if __name__ == '__main__':
    Extract_Caption.extractCap('https://www.youtube.com/watch?v=vNOllWX-2aE')