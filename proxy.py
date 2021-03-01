import requests
from data import Data

class Proxy:

    def __init__(self, instance):
        self.instance = instance


    def proxy(self):
        object_instance = self.instance
        if object_instance.number % 2 == 0: # países Asia
            data = Data("asia")
            return data.process()
        
        else: # países Europa
            data = Data("europe")
            return data.process()
            
        return False