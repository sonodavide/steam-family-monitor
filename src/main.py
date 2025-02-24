import time
from DbHelper import DbHelper
from SteamWebApi import SteamWebApi
from SteamWebApiFetcher import SteamWebApiFetcher
import requests
from pprint import pprint
from TelegramNotificationSender import TelegramNotificationSender

steamWebApiFetcher = SteamWebApiFetcher(DbHelper())
telegramNotificationSender = TelegramNotificationSender()

while(True):

    results = steamWebApiFetcher.fetchUpdates()
    telegramNotificationSender.send_notification(results)
    time.sleep(60)




