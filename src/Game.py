class Game:
    STEAM_STORE_URL = "https://store.steampowered.com/app"
    def __init__(self, appid, name):
        self.appid : str = appid
        self.name : int = name

    def getStoreLink(self):
        return f"{self.STEAM_STORE_URL}/{self.appid}/"