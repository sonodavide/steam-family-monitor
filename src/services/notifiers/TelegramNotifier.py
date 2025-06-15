from src.services.api.TelegramApi import TelegramApi
from src.services.notifiers.BaseNotifier import BaseNotifier
from src.models.ParsedUserResult import ParsedUserResult
import requests
import yaml

class TelegramNotifier(BaseNotifier):
    def __init__(self):
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        self.chatIds=config["Notifiers"]["Telegram"]["chatIds"]
        self.telegramBot = TelegramApi(config["Notifiers"]["Telegram"]["botToken"])

    

    

    def notify(self, parsedUsersResults : list[ParsedUserResult]):
        for user in parsedUsersResults:
            if len(user.games) == 0:
                continue
            message = ""
            messageFooter = f'\n<b>~ <a href="{user.getProfileLink()}">{user.username}</a></b>'
            media = []
            for i, game in enumerate(user.games):
                if len(message) + len(game.name) + len(messageFooter)> 2023:
                    self._sendMediaGroup(media, message+messageFooter)
                    media = []
                    message = ""
                media_item = {
                    "type": "photo",
                    "media": game.getStoreLink(),
                }
                media.append(media_item)
                message += f'<b>• <a href="{game.getStoreLink()}">{game.name}</a></b>\n'

                if i == len(user.games) - 1 or len(media) == 10:
                    self._sendMediaGroup(media, message+messageFooter)
                    media = []
                    message = ""
        return 
    
    
    def _sendMediaGroup(self, media, caption):
        parse_mode="HTML"
        for chat in self.chatIds:
            self.telegramBot.sendMediaGroup(chat, media, caption, parse_mode)