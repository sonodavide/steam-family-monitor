import yaml
import requests


from src.services.errors.ErrorNotifierManager import ErrorNotifierManager
class SteamWebApi:
    def __init__(self):
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        
        self.base_url = "https://api.steampowered.com"
        self.api_key = config['Fetchers']['SteamWebApi']['apiKey']

    def getOwnedGames(self, userId):
        endpoint = f"{self.base_url}/IPlayerService/GetOwnedGames/v1/"
        params = {
            'key': self.api_key,
            'steamid': userId,
            'include_appinfo': True,
            'include_played_free_games': False,
            "include_free_sub": False,
            'format': 'json'
        }
        
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            ErrorNotifierManager.notify(f"Error: {response.status_code} - {response.text}")
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
            ErrorNotifierManager.notify(f"Error: {response.status_code} - {response.text}")
            raise Exception(f"Error: {response.status_code} - {response.text}")        
    def getUserUsername(self, userId):
        user_info = self.getUserInfo(userId)
        return user_info.get("response", {}).get("players", [{}])[0].get("personaname", "")
    
    def getUserIdFromVanityLink(self, userLink):
        userLink = userLink.rstrip("/").split("/")[-1]
        endpoint = f"{self.base_url}/ISteamUser/ResolveVanityURL/v1/"
        params = {
            'key': self.api_key,
            'vanityurl': userLink,
            'format': 'json'
        }
        
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.json()["response"].get("steamid", None)
        else:
            ErrorNotifierManager.notify(f"Error: {response.status_code} - {response.text}")
            raise Exception(f"Error: {response.status_code} - {response.text}")
    
    