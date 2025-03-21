import yaml

from src.models.ParsedUserResult import ParsedUserResult
from src.services.fetchers.SteamWebApiFetcher import SteamWebApiFetcher

class FetcherManager:
    def __init__(self, dbHelper):
        self.fetchers = []
        self.dbHelper = dbHelper
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        for platform, settings in config["Fetchers"].items():
            match platform:
                case "SteamWebApi":
                    if settings.get("enabled"):
                        self.fetchers.append(SteamWebApiFetcher(self.dbHelper))
                
    def fetch(self):
        parsedUsersResults = []
        for fetcher in self.fetchers:
            temp = fetcher.fetch()
            for parsedUserResult in temp:
                found = False
                for user in parsedUsersResults:
                    if user.user_id == parsedUserResult.user_id:
                        found = True
                        user.games = user.games.union(parsedUserResult.games)
                        break
                if not found:
                    parsedUsersResults.append(parsedUserResult)
        return parsedUsersResults
        