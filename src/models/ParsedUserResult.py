from src.models.Game import Game  # Changed from models.Game to src.models.Game


class ParsedUserResult:
    def __init__(self, user_id):
        self.user_id = user_id
        self.games = set()
        self.username = ""

    def add_game(self, game : Game):
        self.games.add(game)
    
    def set_username(self, username):
            self.username = username

    def getProfileLink(self):
        return f"https://steamcommunity.com/profiles/{self.user_id}"
        