"""interactions.py
"""

US_AG_INTERACTION_MAP = {
    'int1': ['phrase1', 'phrase2'],
    'int2': ['phrase3', 'phrase4'],
    'greet1': ['i am (.*)', 'hello my name is (.*)']
    # TODO
}

US_AG_RESPONSE_MAP = {
    'int1': ['resp1', 'resp2', 'resp3'],
    'int2': [],
    'greet1': ['Hi {name}, how can i help you ?']
    #TODO
}
