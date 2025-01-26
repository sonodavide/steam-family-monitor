from SteamWebApi import SteamWebApi
from SteamWebApiFetcher import SteamWebApiFetcher


userIds = []

results = SteamWebApiFetcher(userIds)
print(results.fetchUpdates())