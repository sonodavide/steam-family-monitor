class Game:
    def __init__(self, appid, name):
        self.appid : str = appid
        self.link : str = f"https://store.steampowered.com/app/{appid}"
        self.name : int = name