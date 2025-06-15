import yaml

from src.services.errors.TelegramErrorNotifier import TelegramErrorNotifier
class ErrorNotifierManager:
    _ErrorNotifier = []
    @staticmethod
    def initialize():
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)

        for platform, settings in config["ApplicationNotifier"].items():
            match platform:
                case "Telegram":
                    if settings.get("enabled"):
                        ErrorNotifierManager._ErrorNotifier.append(TelegramErrorNotifier())
                
    @staticmethod
    def notify_error(error_message):
        for notifier in ErrorNotifierManager._ErrorNotifier:
            notifier.notify_error(error_message)