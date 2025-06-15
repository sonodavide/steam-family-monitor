from src.services.api.TelegramApi import TelegramApi
import yaml
class TelegramErrorNotifier:
    def __init__(self):
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        self.telegramBot = TelegramApi(config["ApplicationNotifier"]["Telegram"]["botToken"])
        self.chatIds = config["ApplicationNotifier"]["Telegram"]["chatIds"]
    
    def notify_error(self, error_message):
        for chat in self.chatIds:
            self.telegramBot.sendMessage(chat, error_message)
        
