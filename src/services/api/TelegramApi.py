import requests

class TelegramApi:
    
    def __init__(self, botToken: str):
        self.TOKEN = botToken
        self.base_url = f"https://api.telegram.org/bot{self.TOKEN}"

    def sendMediaGroup(self,chatId, media, caption="", parse_mode="None"):
        media[-1]["caption"] = caption
        media[-1]["parse_mode"] = "HTML"
        media[-1]["disable_web_page_preview"] = False
        url = f"{self.base_url}/sendMediaGroup"
        payload = {
            "chat_id": chatId,
            "media": media
        }
        response = requests.post(url, json=payload)
        return response
    
    def sendMessage(self, chatId, message, parse_mode="None"):
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": chatId,
            "text": message,
            "parse_mode": parse_mode
        }
        response = requests.post(url, json=payload)
        return response