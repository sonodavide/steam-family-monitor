from SteamWebApi import SteamWebApi
from UpdateFetcher import UpdateFetcher
from ParsedUserResult import ParsedUserResult
from Game import Game
class SteamWebApiFetch(UpdateFetcher):
    def __init__(self, user_ids: list[str]):
        super().__init__()
        self.user_ids = user_ids
        self.steamWebApi = SteamWebApi()
        
    def fetchUpdates(self):
        parsedUsersResults = []
        for userId in self.user_ids:
            parsedUserResult = ParsedUserResult(userId)
            parsedUserResult.add_game(self._parseGames(self.steamWebApi.cerca(userId))) 


    def _parseGames(self, response) -> list[Game]:
        games = []
        ## processa la response.
        return games