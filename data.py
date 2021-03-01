import requests as req

class Data:

    def __init__(self, continente):
        self.continente = continente

    def process(self):
        response = req.get(f"https://restcountries.eu/rest/v2/region/{self.continente}")
        if response.status_code == 200:
            return response.content
        elif response.status_code == 404:
            return "Ese continente no existe"
        else:
            return "Hubo un error :("
            