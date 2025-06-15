import time

from src.services.notifiers.NotifierManager import NotifierManager
from src.services.fetchers.FetcherManager import FetcherManager
from src.services.errors.ErrorNotifierManager import ErrorNotifierManager
from src.services.database.DbHelper import DbHelper



ErrorNotifierManager.initialize()
print("ErrorNotifierManager Initialized")
fetcherManager = FetcherManager(DbHelper())
print("FetcherManager Initialized")
notifiersManager = NotifierManager()
print("NotifierManager Initialized")
ErrorNotifierManager.notify_error("sfm started.")
while(True):
    results = fetcherManager.fetch()
    notifiersManager.notify(results)
    print("Latest update:", time.strftime("%d-%m-%Y %H:%M"))
    time.sleep(900)




