from speaker.speaker import Speaker
from listener.listener import Listener
from agent.agent import Agent





speaker = Speaker()
listener = Listener()
agent0 = Agent(speaker, listener)

print('Ciao il mio nome è Emanuele')
agent0.process('Ciao il mio nome è Emanuele')

exit(0)

speaker.speak('Ciao come posso aiutarti?')

a=False
while a==False:
    command,taken=listener.listen()

    if command=='arrivederci':
        speaker.speak("Grazie e arrivederci")
        break

    if taken==False:
        print("Non ho capito, puoi ripetere?")
        a=False

