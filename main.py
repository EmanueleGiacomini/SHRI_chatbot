from speaker.speaker import Speaker
from listener.listener import Listener
from agent.agent import Agent





speaker = Speaker()
listener = Listener()
agent0 = Agent(speaker, listener, './database/kb_01.json')

speaker.speak('Ciao come posso aiutarti?')

a=False
while a==False:
    command,taken=listener.listen()
    #command, taken = input(), True # ASR cut-off (use console instead)
    command = command.capitalize()

    if command=='Arrivederci':
        speaker.speak("Grazie e arrivederci")
        break

    if taken==False:
        print("Bot: Non ho capito, puoi ripetere?")
        a=False

    agent0.process(command)
agent0.kb.save(agent0.kb.kb)

