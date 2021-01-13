"""agent.py
"""
from agent.interactions import US_AG_INTERACTION_MAP, US_AG_RESPONSE_MAP
import re


def process_text(in_text: str):
    """
    Applies RE to find the interaction type and interaction arguments given an input text in_text
    :param in_text: str
    :return:
    """
    for k in US_AG_INTERACTION_MAP:
        for i, interaction in enumerate(US_AG_INTERACTION_MAP[k]):
            match = re.search(interaction, in_text)
            if match:
                # Found a match, analyze the match object
                return k, match.groups() #TODO: return interaction args (ie: Subjects and so on)
    return None, None


class Agent:
    def __init__(self, speaker, listener):
        self.speaker = speaker
        self.listener = listener
        self.handle_fn = {
            'int1': agent_inter1_cb,
            'greet1':agent_greet1_cb,
            'NOT_UNDERSTOOD': agent_not_understood_cb
        }
        ...

    def process(self, in_text: str):
        inter, inter_args = process_text(in_text)
        if inter is None:
            self.handle_fn['NOT_UNDERSTOOD'](self.speaker)
            return
        # Inter and inter_args can be used
        #print(f'matched signal: {inter}')
        self.handle_fn[inter](self.speaker, inter_args)


def agent_inter1_cb(speaker, inter_args):
    speaker.speak("Executing inter 1 callback.")
    return

def agent_not_understood_cb(speaker):
    speaker.speak('I did not understand.')

def agent_greet1_cb(speaker, inter_args):
    response_lst = US_AG_RESPONSE_MAP['greet1']
    # Sample a response
    response = response_lst[0]
    print(response.format(name=inter_args[0]))
    speaker.speak(response.format(name=inter_args[0]))
    


