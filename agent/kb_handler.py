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
         with open(f"./agent/kb/{datetime.now().strftime('%Y%m%d-%H%M%S')}_kb.json", 'x') as outfile:
            json.dump(d, outfile)

    def get_region(self,key,data):
        N=len(data["regioni"])

        for i in range(N):
            if data["regioni"][i]['regioni']==key:
                return data["regioni"][i]

    def get_dato(self,key,data):
        return data[key]



