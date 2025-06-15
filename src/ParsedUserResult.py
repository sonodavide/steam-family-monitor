from Game import Game


class ParsedUserResult:
    def __init__(self, user_id):
        self.user_id = user_id
        self.games = []

    def add_game(self, game : Game):
        self.games.append(game)
        