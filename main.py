from speaker.speaker import Speaker
from listener.listener import Listener
from agent.agent import Agent





speaker = Speaker()
listener = Listener()
agent0 = Agent(speaker, listener, './database/kb_01.json')

#print('Ciao il mio nome è Emanuele')
#agent0.process('Dimmi se in zona rossa si puo andare al cinema')
agent0.process('In zona rossa si puo andare al cinema')

exit(0)

speaker.speak('Ciao come posso aiutarti?')

a=False
while a==False:
    command,taken=listener.listen()
    command = command.capitalize()

    if command=='Arrivederci':
        speaker.speak("Grazie e arrivederci")
        break

    if taken==False:
        print("Non ho capito, puoi ripetere?")
        a=False

    agent0.process(command)

    

