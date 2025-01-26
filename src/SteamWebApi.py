# filepath: /c:/Users/Dav/Documents/GitHub/steam-family-monitor/src/SteamWebApi.py
import yaml
import requests
from pprint import pprint
class SteamWebApi:
    def __init__(self):
        # Carica la configurazione dal file config.yaml
        with open('../config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        
        self.base_url = "https://api.steampowered.com"
        self.api_key = config['SteamWebApi']['apiKey']

    def cerca(self, userId):
        endpoint = f"{self.base_url}/IPlayerService/GetOwnedGames/v1/"
        params = {
            'key': self.api_key,
            'steamid': userId,
            'include_appinfo': True,
            'format': 'json'
        }
        
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
    
    def getUserInfo(self, userId):
        endpoint = f"{self.base_url}/ISteamUser/GetPlayerSummaries/v0002/"
        params = {
            'key': self.api_key,
            'steamids': userId,
            'include_appinfo': True,
            'format': 'json'
        }
        
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")        
