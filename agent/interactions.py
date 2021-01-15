"""interactions.py
"""

US_AG_INTERACTION_MAP = {
    'int1': ['phrase1', 'phrase2'],
    'int2': ['phrase3', 'phrase4'],
    'int3': ['Sto male', 'Non mi sento bene', 'Mi sento poco bene'],
    'int4': ['Non sento gli odori','Ho la febbre','Non sento i sapori','Ho la tosse','Febbre','Tosse','Non sento odori e sapori'],
    'int5': ['Si ho fatto il tampone','Tampone fatto'],
    'int6': ['Tampone positivo','Positivo','Sono positivo'],
    'int7': ['Tampone negativo','Negativo','Sono negativo'],
    'int8': ['Ho avuto un contatto con un positivo','Ho frequentato un positivo','Sono entrato a contatto con un positivo'],
    'int9': ['Sono positivo da (1|2|3|4|5|6|7) giorni', 'Il (covid|coronavirus) da (1|2|3|4|5|6|7) giorni'],
    'int10': ['Sono positivo ma da (1|2|3) giorni non ho sintomi'],
    'int11': ['Sono positivo da (18|19|20) giorno senza sintomi'],
    'int12': ['Sono in isolamento da 15 giorni senza sintomi'],
    'int13': ['Sono positivo ma asintomatico'],
    'int14': ['Quali sono alcuni sintomi del (covid|coronavirus)','Dimmi alcuni sintomi del (covid|coronavirus)'],
    'int15': ['Quali sono i sintomi lievi del (covid|coronavirus)','Dimmi i sintomi lievi del (covid|coronavirus)'],
    'int16': ['Quali sono i sintomi gravi del (covid|coronavirus)','Dimmi i sintomi gravi del (covid|coronavirus)'],
    'int17': ['Quali sono i paesi più colpiti dal (covid|coronavirus)','Dimmi i paesi più colpiti dal (covid|coronavirus)','Quali sono i paesi più colpiti','Dimmi i paesi più colpiti'],
    'int18': ['I paesi più colpiti sono gli (USA|Stati Uniti)'],
    'int19': ['Farai il vaccino'],
    'int20': ['Posso fare un aperitivo','Posso fare aperitivo'],
    'int21': ['I cinema sono aperti','Dimmi se i cinema sono aperti'],
    'int22': ['No, non l\'ho fatto', 'No', 'Ancora no'],
    'int23': ['Posso cenare fuori'],
    #'int24': ['Dimmi la popolazione di (.*)', 'Qual è la popolazione di (.*)', 'Quanti abitanti ci sono in (.*)'],
    'greet1': ['Ciao sono (.*)', 'Ciao il mio nome è (.*)'],
    'askzone1': ['Dimmi se in zona (?P<zona>[a-z]+) si puo andare (al|nei) (?P<luogo>[a-z]+)'],
    'setzone1': ['In zona (?P<zona>[a-z]+) si puo andare (al|nei) (?P<luogo>[a-z]+)']
    

    # TODO
}

US_AG_RESPONSE_MAP = {
    'int1': ['resp1','resp2','resp3'],
    'int2': [],
    'int3': ['Che ti senti?','Cosa hai?'],
    'int4': ['Hai fatto il tampone?'],
    'int5': ['Qual è l\'esito del tampone?' ],
    'int6': ['Buona guarigione, ricordati di non avere contatti.'],
    'int7': ['Ok, sei libero','Se stai bene puoi uscire'],
    'int8': ['Fai il tampone','Resta a casa in isolamento','Hai sviluppato sintomi?'],
    'int9': ['Aspetta il giorno 8 per vedere cosa fare'],
    'int10': ['Dovresti fare il tampone'],
    'int11': ['Dal giorno 21 puoi uscire'],
    'int12': ['Sei libero','Puoi uscire'],
    'int13':['Al primo tampone negativo puoi uscire'],
    'int14':['Mal di testa, febbre e tosse','Tosse secca, febbre e spossatezza'],
    'int15':['Tosse secca, febbre e spossatezza, perdita di gusto e olfatto'],
    'int16':['Difficoltà respiratoria', 'Fiato corto','Difficoltà respiratoria, fiato corto'],
    'int17': ['Stati uniti, India, Brasile, Russia'],
    'int18' : ['Grazie per l\'informazione'],
    'int19': ['Certo'],
    'int20': ['Solo a casa','Prima delle 18 in zona gialla'],
    'int21': ['No sono chiusi'],
    'int22': ['Allora dovresti farlo','Forse è il caso di farlo'],
    'int23': ['No, solo asporto'],
    #'int24': ['(.*) ha ... abitanti', 'La popolazione è ...'],
    'greet1': ['Ciao {name}, come posso aiutarti?'],
    'askzone1': [],
    'setzone1': []
    #TODO
}
