"""agent.py
"""
from agent.interactions import US_AG_INTERACTION_MAP, US_AG_RESPONSE_MAP
from agent.kb_handler import KB
import re
import random


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
    def __init__(self, speaker, listener, path=None):
        self.speaker = speaker
        self.listener = listener
        self.handle_fn = {
            #'int1': agent_inter1_cb,
            'greet1':agent_greet1_cb,
            'NOT_UNDERSTOOD': agent_not_understood_cb,
            # Default question-answer callbacks
            'int3':agent_autores_cb,
            'int4':agent_autores_cb,
            'int5':agent_autores_cb,
            'int6':agent_autores_cb,
            'int7':agent_autores_cb,
            'int8':agent_autores_cb,
            'int9':agent_autores_cb,
            'int10':agent_autores_cb,
            'int11':agent_autores_cb,
            'int12':agent_autores_cb,
            'int13':agent_autores_cb,
            'int14':agent_autores_cb,
            'int15':agent_autores_cb,
            'int16':agent_autores_cb,
            'int17':agent_autores_cb,
            'int19':agent_autores_cb,
            'int20':agent_autores_cb,
            'int21':agent_autores_cb,
            'int22':None,
            'int23':agent_autores_cb,
            'askzone1':agent_askzone1_cb,
            'setzone1':agent_setzone1_cb,
            'askregion1': agent_askregion1_cb,
            'askregion2': agent_askregion1_cb
        }
        self.kb = KB(path)

    def process(self, in_text: str):
        inter, inter_args = process_text(in_text)
        response = None
        if inter is None:
            response = self.handle_fn['NOT_UNDERSTOOD'](self.speaker)
        else:
            # Inter and inter_args can be used
            response = self.handle_fn[inter](self.speaker, inter,  inter_args, self.kb)
        print(response)
        self.speaker.speak(response)


def agent_inter1_cb(speaker, inter_args):
    speaker.speak("Executing inter 1 callback.")
    return

def agent_not_understood_cb(speaker):
    return "Non ho capito"

def agent_greet1_cb(speaker, inter, inter_args, kb=None) -> str:
    response_lst = US_AG_RESPONSE_MAP['greet1']
    # Sample a response
    response = response_lst[0]
    response = response.format(name=inter_args[0])
    return response

def agent_autores_cb(speaker, inter, inter_args, kb=None) -> str:
    """ 
    Default auto-response callback
    Automatically answer to the user with one of the predefined answers
    """
    response_lst = US_AG_RESPONSE_MAP[inter]
    assert len(response_lst) > 0
    # Sample a response
    response = None
    if len(response_lst) == 1:
        response = response_lst[0]
    else:
        response = random.choice(response_lst)
    return response

def agent_askzone1_cb(speaker, inter, inter_args, kb=None) -> str:
    """
    Query callback. The function uses inter_args to query the KB and extract
    user requested informations.
    """
    #print(inter_args)
    # TODO(Fix KB functions and remake this part)
    color_zone = kb.get_zone(inter_args[0])
    location = color_zone[inter_args[2]]
    if location is None:
        return "Non ti so dire nulla a riguardo"
    response = None
    if location is True:
        response = f'In zona {inter_args[0]} si puo andare {inter_args[1]} {inter_args[2]}'
    else:
        response = f'In zona {inter_args[0]} non si puo andare {inter_args[1]} {inter_args[2]}'
    return response

def agent_setzone1_cb(speaker, inter, inter_args, kb=None) -> str:
    """
    Set query callback. The function uses inter_args to write inside the KB
    """
    color_zone = inter_args[0]
    key = inter_args[2]
    kb.set_dato(color_zone, key, 'posso')
    response = f'Salvo che in zona {color_zone}  si puo andare {inter_args[1]} {key}'
    return response

def agent_askregion1_cb(speaker, inter, inter_args, kb=None) -> str:
    """
    Query callback. The function uses inter_args to query the KB and extract
    user requested informations.
    """
    reg_name = inter_args[2]
    prop = inter_args[1]
    key = inter_args[0]
    region = kb.get_region(reg_name)
    response = None
    
    if region is not None:
        response = f'Il numero di {key} {prop} {reg_name} è {region[key]}'
    else:
        response = f'Non ho informazioni per questa regione'
    return response
    
    


