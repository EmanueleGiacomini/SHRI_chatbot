from speaker.speaker import Speaker
from listener.listener import Listener

speaker = Speaker()
listener = Listener()

speaker.speak('Hello, how can I help you?') 

a=False
while a==False:
    command,taken=listener.listen()

    if command=='goodbye':
        speaker.speak("Thank you, bye")
        break

    if taken==False:
        print("I don't understand, could you repeat?")
        a=False

