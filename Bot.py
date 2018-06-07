import collections

from telegram.ext import Updater, MessageHandler, Filters
from my_read import add_users
from Message import *

admin_usernames = []
other_users = []
my_id = 190016290


class MyBot:

    def __init__(self, token, user_generator, admin_generator=None):
        self.updater = Updater(token=token)  # заводим апдейтера
        text_handler = MessageHandler(Filters.text | Filters.command,
                                      self.handle_message)
        self.updater.dispatcher.add_handler(
            text_handler)  # ставим обработчик всех текстовых сообщений
        if admin_generator is not None:
            self.admin_generator = admin_generator
        else:
            self.admin_generator = user_generator
        self.generator = user_generator
        self.handlers = collections.defaultdict(
            user_generator)  # заводим мапу "id чата -> генератор"

    def start(self):
        # Начинаем поиск обновлений
        print('Init successful. Polling...')
        # self.updater.start_polling()
        self.updater.start_polling(clean=True)
        # Останавливаем бота, если были нажаты Ctrl + C
        self.updater.idle()
        print('start end')
        add_users(*admin_usernames, *other_users)

    def handle_message(self, bot: telegram.Bot, update: telegram.Update):
        # print(update)
        user = update.message['chat']['username']
        chat_id = int(update.message.chat_id)
        if user not in admin_usernames or other_users:
            print(user)
            if chat_id == my_id:
                admin_usernames.append(user)
        if user in admin_usernames and user in other_users:
            other_users.remove(user)
            self.handlers.pop(chat_id, None)
        if str(update.message.text).startswith('/add_admin') and int(chat_id) == my_id:
            admin_usernames.extend(str(update.message.text).split()[1:])
        if str(update.message.text).startswith('/del_admin') and int(chat_id) == my_id:
            try:
                admin_usernames.remove((update.message.text).split()[-1])
            except:
                pass
        if update.message.text == '/show_users' and user in admin_usernames:
            add_users(*admin_usernames, *other_users)
            answer = Message(*other_users, *admin_usernames)
            answer.send(bot, chat_id)
            return
        if update.message.text == '/show_admins' and chat_id == my_id:
            answer = Message(*admin_usernames)
            answer.send(bot, chat_id)
            return
        if update.message.text == '/clear_admins' and int(chat_id) == my_id:
            admin_usernames.clear()
        # if update.message.text.starts
        if update.message.text == "/start":
            # если передана команда /start, начинаем всё с начала -- для
            # этого удаляем состояние текущего чатика, если оно есть
            self.handlers.pop(chat_id, None)
        if chat_id in self.handlers:
            try:
                answer = self.handlers[chat_id].send(update)
            except StopIteration:
                print('stop iteration')
                del self.handlers[chat_id]
                return self.handle_message(bot, update)
        else:
            name = update.message['chat']['first_name']
            if user in admin_usernames or int(chat_id) == my_id:
                self.handlers[chat_id] = self.admin_generator(name)
            else:
                self.handlers[chat_id] = self.generator(name)
                other_users.append(user)
            answer = next(self.handlers[chat_id])
        # отправляем полученный ответ пользователю
        answer.send(bot, chat_id)
