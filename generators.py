import random

from Message import Message, PhotoMessage
from PIL import Image

def dialog(name=None):
    if name is not None:
        update = yield Message('Здравствуй, {}\nМожно тебя так называть?'.format(name),
                               parse_mode='HTML').make_keyboard(
            # update = yield Message(start_message.format(name)).make_keyboard(
            [['Да'], ['Нет']])
        answer = update.message
    if name is None or str(answer.text).lower().startswith('нет'):
        update = yield Message('Как мне тебя называть?')
        answer = update.message
        name = answer.text.rstrip(".!").capitalize()
    update = yield Message(r'Привет, я Александр Александрович В и я очень люблю галстуки! Меня создали для того, что бы помочь тебе выглядеть стильно и изящно с помощью твоего красивого галстука! Хочешь увидеть варианты? Пиши да или /next или /get, и я пришлю тебе картинку и инструкцию, как это сделать.')
    image = MyImage()
    answer = update.message
    while True:
        if answer.text.startswith('/help'):
            update = yield Message('Меня создали для того, что бы помочь тебе выглядеть стильно и изящно с помощью твоего красивого галстука! Хочешь увидеть варианты? Пиши да или /next или /get, и я пришлю тебе картинку и инструкцию, как это сделать.')
            answer = update.message
            continue

        if answer.text.startswith('/next') or answer.text.startswith('/get') or answer.text.lower().startswith('да'):
            # print('start get')
            try:
                picture = next(image)
            except Exception as e:
                # print('error start', e, e.args, 'error end')
                picture = Message('Теперь все распространенные способы завязывания вам известны. Остальное, дело ваших рук и фантазии!)', 'Пиши да, если хочешь ещё раз')
                image = MyImage()
                # picture = next(image)
            update = yield picture
            answer = update.message
            continue
        if answer.text.startswith('/end'):
            return update

        update = yield Message('Я не понимаю что вы написали(',
                                        'Попробуйте подсказку\nТам всё, что я умею\nВы можете её вызвать командой /help\nУдачи!)')
        answer = update.message


def MyImage():
    with open('Images/count') as r:
        count = int(r.read())
    l = list(range(count))
    random.shuffle(l)
    for i in l:
        pic = open(str('Images/' + str(i) + '.jpg'), 'rb')
        # try:
        #     with open(str('Images/' + str(i) + '.jpg')) as im:
        #         try:
        #             pic = im.read()
        #         except Exception as e:
        #             print(1, e)
        # except Exception as e:
        #     print(2, e)
        # # print(pic)
        yield PhotoMessage(photo=pic)

# def addImege(update: T)

def adimin_bot(name=None):
    update = yield Message('hello Admin {}!'.format(name))
    answer = update.message
    while True:
        if answer.text.startswith('/help'):
            update = yield Message('/like_user to use user interface\n/end to end user interface\n/show_users to see users')
            answer = update.message
            continue

        if answer.text.startswith('/like_user'):
            try:
                update = yield from dialog(name)
            except Exception as e:
                print('втф вообще?')
                print(e)
            answer = '/help'
            continue

        update = yield Message('Я не понимаю что вы написали(',
                                        'Попробуйте подсказку\nТам всё, что я умею\nВы можете её вызвать командой /help\nУдачи!)')
        answer = update.message