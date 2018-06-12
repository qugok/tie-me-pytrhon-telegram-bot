#!/usr/bin/python3


import my_read
import Bot
from Bot import MyBot
from generators import dialog, adimin_bot


if __name__ == "__main__":
    try:
        telegram_token = my_read.read_telegram_token()
    except:
        print("I can't find telegram token")
        exit()
    dialog_bot = MyBot(telegram_token, dialog, adimin_bot)
    # dialog_bot = MyBot(telegram_token, dialog)
    dialog_bot.start()
    print('main end')
