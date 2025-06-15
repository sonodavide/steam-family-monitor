import time
from DbHelper import DbHelper
from SteamWebApi import SteamWebApi
from SteamWebApiFetcher import SteamWebApiFetcher
import requests
from pprint import pprint
from TelegramNotificationSender import TelegramNotificationSender


results = SteamWebApiFetcher(DbHelper()).fetchUpdates()
#TelegramNotificationSender().send_notification(results)
TelegramNotificationSender().send_notification(results)
    




