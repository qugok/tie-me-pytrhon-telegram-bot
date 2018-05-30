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
    update = yield Message('gwrgwergv')
    image = MyImage()
    answer = update.message
    while True:
        if answer.text.startswith('/help'):
            update = yield Message('gwrgwergv')
            answer = update.message
            continue

        if answer.text.startswith('/get'):
            print('start get')
            try:
                picture = next(image)
            except Exception as e:
                print('error start', e, e.args, 'error end')
                picture = Message('произошла какая-то ошибка, сейчас разберёмся)')
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
    count = 2
    for i in range(count):
        pic = open(str('Images/' + str(i) + '.jpg'),'rb')
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

def adimin_bot(name=None):
    update = yield Message('gwrgwergv')
    answer = update.message
    while True:
        if answer.text.startswith('/help'):
            update = yield Message('gwrgwergv')
            answer = update.message
            continue

        if answer.text.startswith('/like user'):
            update = yield from dialog(name)
            answer = update.message
            continue

        update = yield Message('Я не понимаю что вы написали(',
                                        'Попробуйте подсказку\nТам всё, что я умею\nВы можете её вызвать командой /help\nУдачи!)')
        answer = update.message