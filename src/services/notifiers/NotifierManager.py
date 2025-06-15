import yaml

from src.models.ParsedUserResult import ParsedUserResult
from src.services.notifiers.TelegramNotifier import TelegramNotifier
from src.services.fetchers.SteamWebApiFetcher import SteamWebApiFetcher

class NotifierManager:
    def __init__(self):
        self.notifiers = []
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        for platform, settings in config["Notifiers"].items():
            match platform:
                case "Telegram":
                    if settings.get("enabled"):
                        self.notifiers.append(TelegramNotifier())
                
    def notify(self, parsedUsersResults : list[ParsedUserResult]):
           
     
        for notifier in self.notifiers:
            notifier.notify(parsedUsersResults)