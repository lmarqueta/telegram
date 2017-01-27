import telepot as t
from pprint import pprint
import config

if __name__ == "__main__":
    bot = t.Bot(config.token)
    print bot.getMe()

    # Get updates
    response = bot.getUpdates()
    pprint(response)

    # Send a message
    msg = "Test message"
    bot.sendMessage(config.id, msg)
