# filepath: /c:/Users/Dav/Documents/GitHub/steam-family-monitor/src/SteamWebApi.py
import yaml

class SteamWebApi:
    def __init__(self):
        # Carica la configurazione dal file config.yaml
        with open('../config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        
        self.base_url = "https://api.steampowered.com"
        self.api_key = config['SteamWebApi']['apiKey']

    def cerca(self, userId):
        # Implementa la logica di ricerca qui
        print(f"Cercando per userId: {userId} con apiKey: {self.api_key}")

    