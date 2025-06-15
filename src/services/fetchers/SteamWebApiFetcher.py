from src.services.database.DbHelper import DbHelper
from src.services.fetchers.SteamWebApi import SteamWebApi
from src.services.fetchers.UpdateFetcher import UpdateFetcher
from src.models.ParsedUserResult import ParsedUserResult
from src.models.Game import Game
import yaml
class SteamWebApiFetcher(UpdateFetcher):
    def __init__(self, db: DbHelper):
        super().__init__()
        self.steamWebApi = SteamWebApi()
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        self.user_ids = config['SteamProfilesLinks']
        self.user_ids = self._parseUserIds(self.user_ids)
        self.dbHelper = db
        self._usersInitializer(self.user_ids)
        
    def _usersInitializer(self, userIds : list[str]):
        for userId in userIds:
            if not self.dbHelper.user_exists(userId):
                jsonResponse = self.steamWebApi.getOwnedGames(userId)["response"]["games"]
                fetchedGames = list()
                for game in jsonResponse:
                    fetchedGames.append(Game(str(game['appid']), game['name']))
                self.dbHelper.update_user_games(userId, fetchedGames)
            

    def fetchUpdates(self):
        parsedUsersResults = []
        for userId in self.user_ids:
            jsonResponse = self.steamWebApi.getOwnedGames(userId)["response"]["games"]
            fetchedGames = list()
            parsedUserResult = ParsedUserResult(userId)
            parsedUserResult.set_username(self.steamWebApi.getUserUsername(userId))
            for game in jsonResponse:
                fetchedGames.append(Game(str(game['appid']), game['name'])) 
            
            newGames = self.dbHelper.get_new_games(userId, fetchedGames)
            
            for game in newGames:
                parsedUserResult.add_game(game)
            self.dbHelper.update_user_games(userId, newGames)
            parsedUsersResults.append(parsedUserResult)
        return parsedUsersResults

    def _parseUserIds(self, links: list[str]) -> list[str]:
        usersIds = []
        for link in links:
            userId = self.steamWebApi.getUserIdFromVanityLink(link)
            if(userId == None):
                parsedId = link.rstrip("/").split("/")[-1]
                if len(SteamWebApi().getUserInfo(parsedId)["response"]["players"]) == 0:
                    raise Exception(f"User {link} not found")
                usersIds.append(parsedId)
            else:
                usersIds.append(userId)

        return usersIds


