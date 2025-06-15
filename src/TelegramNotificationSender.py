from NotificationSender import NotificationSender 
import requests
import yaml

from ParsedUserResult import ParsedUserResult
class TelegramNotificationSender(NotificationSender):
    def __init__(self):
        with open('../config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        self.chatIds=config["TelegramNotification"]["chatIds"]
        self.TOKEN=config["TelegramNotification"]["botToken"]

    

    """def send_notification(self, parsedUsersResults):
        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage"
        for user in parsedUsersResults:
            if len(user.games) == 0:
                continue
            message = f"👤: {user.username}\n🛒\n"
            for game in user.games:
                message += f'<a href="{game.link}">{game.name}</a>\n'
            for chat in self.chatIds:
                payload = {
                    "chat_id": chat,
                    "text": message,
                    "parse_mode": "HTML",
                    "disable_web_page_preview": len(user.games) > 1
                }
                response = requests.post(url, json=payload)
        return """

    def send_notification(self, parsedUsersResults : list[ParsedUserResult]):
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
    
    def _sendMediaGroup(self, media, message):
        media[-1]["caption"] = message
        media[-1]["parse_mode"] = "HTML"
        media[-1]["disable_web_page_preview"] = False
        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMediaGroup"
        for chat in self.chatIds:
                payload = {
                    "chat_id": chat,
                    "media": media
                }
                response = requests.post(url, json=payload)
                print(response.text)
