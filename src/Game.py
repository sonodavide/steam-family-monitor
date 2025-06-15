class Game:
    def __init__(self, appid, name):
        self.appid = appid
        self.link = f"https://store.steampowered.com/app/{appid}"
        self.name = name