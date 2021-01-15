"""kb_handler.py
"""
import os 
import json
from datetime import datetime

class KB:
    def __init__(self,path):
        self.kb=self.load(path)
                  
    def get_kb(self):
        return self.kb

    def load(self,path):
        with open(f"./agent/{path}") as file:
            data=json.load(file)
        return data

    def save(self,d):
         with open(f"./agent/database/{datetime.now().strftime('%Y%m%d-%H%M%S')}_kb.json", 'x') as outfile:
            json.dump(d, outfile)

    def get_region(self,key):
        kb = self.kb["regioni"]
        N=len(kb)

        for i in range(N):
            if kb[i]['regione']==key.capitalize():
                return kb[i]

    def get_dato(self,key):
        return self.kb[key]

    def set_dato(self,color,key,word):
        kb = self.kb["zone"]
        N=len(kb)
        for i in range(N):
            if kb[i]['colore']==color:
                elem =  kb[i]
                if word == "posso":
                    elem[key] = True
                elif word == "non posso":
                    elem[key] = False
        return self.kb

    ## TODO FUNCTIONS
    def get_zone(self, color):
        kb = self.kb['zone']
        for entry in kb:
            if entry['colore'] == color:
                return entry
        return None
            
        







