import pyttsx3



class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('volume',10.0) 

        self.engine.setProperty('rate', 115)  

        voices = self.engine.getProperty('voices') 
        self.engine.setProperty('voice', voices[1].id) 

    def speak(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()


