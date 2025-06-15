import time
from SteamWebApi import SteamWebApi
from SteamWebApiFetcher import SteamWebApiFetcher
import requests
from pprint import pprint
from TelegramNotificationSender import TelegramNotificationSender


results = SteamWebApiFetcher().fetchUpdates()
#TelegramNotificationSender().send_notification(results)
print(pprint(results))
TelegramNotificationSender().send_notification(results)
    




