# Steam Family Monitor (SFM)

A monitoring tool that sends notifications when any member of your Steam family purchases a new game.

## Features
- Track game purchases across multiple Steam accounts
- Send notifications via Telegram when new games are detected
- Easily extendable for other notification platforms
## Installation
### Prerequisites
- Python 3.10 or higher
- A Steam Web API key (get one at [Steam Developer Portal](https://steamcommunity.com/dev/apikey))
- A Telegram bot token (create one using [@BotFather](https://t.me/botfather))

### Setup
1. Clone the repository and Install dependencies
```bash
git clone https://github.com/yourusername/steam-family-monitor.git
cd steam-family-monitor
pip install -r requirements.txt
```
2. Create your configuration file
```bash
cp config.example.yaml config.yaml
```

3. Edit the configuration file with your details
```bash
# Steam family members accounts
SteamProfilesLinks:
  - https://steamcommunity.com/id/YourFamilyMember1/
  - https://steamcommunity.com/profiles/12345678901234567/

Fetchers:
  SteamWebApi:
    enabled: true
    apiKey: YOUR_STEAM_API_KEY_HERE

Notifiers:
  Telegram:
    enabled: true
    botToken: YOUR_TELEGRAM_BOT_TOKEN
    chatIds:
      - YOUR_CHAT_ID

ApplicationNotifier:
  Telegram:
    enabled: true
    botToken: YOUR_TELEGRAM_BOT_TOKEN
    chatIds:
      - YOUR_CHAT_ID
```
## Usage

```bash
python main.py
```
The application will:

1. Initialize the notification system
2. Check for new game purchases every 15 minutes
3. Send notifications when new games are detected
4. Log updates in the console

## Extending the Application
1. Create a new class that extends the appropriate base class
2. Update your configuration file to include the new fetcher
3. Update FetcherManager to include your new fetcher.


## License

[MIT](https://choosealicense.com/licenses/mit/)
