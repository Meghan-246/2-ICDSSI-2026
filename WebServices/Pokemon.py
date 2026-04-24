import requests
import shutil 
import json

class Pokemon():

    def get_image(self, url, file_name):
        res = requests.get(url,stream = True)
        if 200==res.status_code:
            with open(file_name, 'wb')as f:
                shutil.copyfileobj(res.raw, f)
            print('imagen descargada corectamente')
        else:
            print('No se encontro la imagen')
       
    def get_pokemon(self,pokemon):
        url = 'https://pokeapi.co/api/v2/pokemon/'
        r = requests.get(url+pokemon)
        print(r)
        obj = json.loads(r.content)
        return obj['sprites']['front_default']
    
    
png_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/"


