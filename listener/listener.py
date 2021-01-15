import speech_recognition as sr

class Listener():

    def __init__(self):
        return

    def listen(self):
        r=sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Bot: Sto ascoltando. . .")
            audio=r.listen(source)

            sentence=""
            taken=True
            try:
                sentence=r.recognize_google(audio, language='it-IT')
                print("User: ", sentence)
            except sr.UnknownValueError:                            # speech is unintelligible
                taken=False


        return sentence,taken


