import time

from src.services.fetchers.SteamWebApiFetcher import SteamWebApiFetcher
from src.services.database.DbHelper import DbHelper
from src.services.notifiers.TelegramNotificationSender import TelegramNotificationSender


steamWebApiFetcher = SteamWebApiFetcher(DbHelper())
print("Fetcher Initialized")
telegramNotificationSender = TelegramNotificationSender()
print("Notifier Initialized")

while(True):

    results = steamWebApiFetcher.fetchUpdates()
    telegramNotificationSender.send_notification(results)
    print("Latest update:", time.strftime("%d-%m-%Y %H:%M"))
    time.sleep(600)




