from hashlib import md5
from requests import get
from datetime import datetime

class SuperHero:
    """
    Information about the service:
    https://superheroapi.com/index.html
    """

    token = ''

    def get_heroes(self):
        result = get('https://www.superheroapi.com/api.php/dfa70ad56d67606d27ce79c68abdcfad/search/ironman')
        data = result.json()
        print(data)
        print(data["status"])


