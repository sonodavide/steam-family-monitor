from DbHelper import DbHelper
from SteamWebApi import SteamWebApi
from UpdateFetcher import UpdateFetcher
from ParsedUserResult import ParsedUserResult
from Game import Game
class SteamWebApiFetcher(UpdateFetcher):
    def __init__(self, user_ids: list[str]):
        super().__init__()
        self.user_ids = user_ids
        self.steamWebApi = SteamWebApi()
        self.dbHelper = DbHelper()
        for user in self.user_ids:
            username = self.steamWebApi.getUserInfo(user)["response"]["players"][0]["personaname"]
            #self.dbHelper.add_user(user, username)
        
    def fetchUpdates(self):
        
       

        parsedUsersResults = []
        for userId in self.user_ids:
            jsonResponse = self.steamWebApi.cerca(userId)["response"]["games"]
            fetchedGames = list()
            parsedUserResult = ParsedUserResult(userId)
            for game in jsonResponse:
                fetchedGames.append(Game(game['appid'], game['name'])) 
            
            newGames = self.dbHelper.get_new_games(userId, fetchedGames)
            for game in newGames:
                parsedUserResult.add_game(game)
            self.dbHelper.update_user_games(userId, newGames)
            parsedUsersResults.append(parsedUserResult)
        return parsedUserResult



