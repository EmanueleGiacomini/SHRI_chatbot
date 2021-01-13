from speaker.speaker import Speaker
from listener.listener import Listener
from agent.agent import Agent





speaker = Speaker()
listener = Listener()
agent0 = Agent(speaker, listener)

agent0.process('phrase3')

exit(0)

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
