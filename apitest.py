import telepot as t
from pprint import pprint
import sys
import config

if __name__ == "__main__":
    if len(sys.argv) == 2:
        msg = sys.argv[1]
    else:
        err = "Usage: {} <message>\n".format(sys.argv[0])
        sys.stderr.write(err)
        sys.exit(1)

    bot = t.Bot(config.token)
    print bot.getMe()

    # Get updates
    response = bot.getUpdates()
    pprint(response)

    # Send a message
    bot.sendMessage(config.id, msg)
