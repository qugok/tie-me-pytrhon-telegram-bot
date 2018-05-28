#!/usr/bin/python3


import my_read
from MyBot import MyBot
from generators import dialog, bad_bot


if __name__ == "__main__":
    telegram_token = my_read.read_telegram_token()
    dialog_bot = MyBot(telegram_token, dialog, bad_bot)
    dialog_bot.start()
