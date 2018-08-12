from googletrans import Translator
import extractCaption


class TRANSLATR_TO_TEXT():
    # def translatFromUrl():
    # translator = Translator()
    # text = extractCap('https://www.youtube.com/watch?v=oKUHfIlKhRI')
    # trans = translator.translate(text, src='en', dest='si')
    # print(trans.__getattribute__('text'))
    #
    # with open("Output.txt","w") as f:
    #     f.write(str(trans.__getattribute__('text')))

    def translatFromURL(url, language):
        translator = Translator()
        text = extractCaption.extractCap(url)
        trans = translator.translate(text, src='en', dest=language)
        print(trans.__getattribute__('text'))

    def translateFromTXT(text, language):
        translator = Translator()
        trans = translator.translate(text, src='en', dest=language)
        return str(trans.__getattribute__('text'))
