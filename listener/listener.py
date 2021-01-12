import speech_recognition as sr

class Listener():

    def __init__(self):
        return

    def listen(self):
        r=sr.Recognizer()

        with sr.Microphone() as source:
            print("I'm listening. . .")
            audio=r.listen(source)

            sentence=""
            taken=True
            try:
                sentence=r.recognize_google(audio)
                print("You have said", sentence)
            except sr.UnknownValueError:                            # speech is unintelligible
                taken=False


        return sentence,taken


