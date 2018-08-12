import time

import speech_recognition as sr




class HOUNDIFY_STT():
    def speak2Text(speech_file):
        client_id = "3are8Pex3Ekut35gCbydXg=="
        client_key = "JnoJc_MzgV3MAUWrCWlcRLz3gyNFnch2_ulmM20r3RoMN4EuI2qvXtpIRdD6m_3iOBbL0S4e2-x5Im623v0jYA=="

        print(sr.__version__)
        r = sr.Recognizer()
        audioSpeak = sr.AudioFile(speech_file)
        with audioSpeak as source:
            audio = r.record(source)
        type(audio)
        text = r.recognize_houndify(audio, client_id, client_key)
        return text

