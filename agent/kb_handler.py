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

    def get_region(self,key,data):
        N=len(data["regioni"])

        for i in range(N):
            if data["regioni"][i]['regioni']==key:
                return data["regioni"][i]

    def get_dato(self,key,data):
        return data[key]

    def set_dato(self,color,key,word):
        with open(f"./agent/database/kb_01.json") as json_file:
            data = js.load(json_file)
            N=len(data["zone"])
            for i in range(N):
                if data["zone"][i]['colore']==color:
                    elem =  data["zone"][i]
                    if word == "posso":
                        elem[key] = True
                    elif word == "non posso":
                        elem[key] = False
        with open(f"./agent/database/kb_01.json","w") as js_file:
            js_file.write(js.dumps(data))







