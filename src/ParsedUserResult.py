from Game import Game


class ParsedUserResult:
    def __init__(self, user_id):
        self.user_id = user_id
        self.games = []
        self.username = ""

    def add_game(self, game : Game):
        self.games.append(game)
    
    def set_username(self, username):
        try:
            self.username = username
        except Exception as e:
            print(f"Error: {e}")
            username = self.user_id
        