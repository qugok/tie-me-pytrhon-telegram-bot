from Message import Message, PhotoMessage


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
    image = Image()
    answer = update.message
    while True:
        if answer.text.startswith('/help'):
            update = yield Message('gwrgwergv')
            answer = update.message
            continue

        if answer.text.startswith('/get'):
            try:
                picture = next(image)
            except:
                image = Image()
                picture = next(image)
            update = yield picture
            answer = update.message
            continue

        update = yield Message('Я не понимаю что вы написали(',
                                        'Попробуйте подсказку\nТам всё, что я умею\nВы можете её вызвать командой /help\nУдачи!)')
        answer = update.message


def Image():
    count = 2
    for i in range(count):
        with open(str('Images/' + str(i) + '.jpg')) as im:
            pic = im.read()
        print(pic)
        yield PhotoMessage(photo=pic)

def bad_bot(name='Никита'):
    """
    специально для Никиты
    :return:
    """
    count = 0
    while count < 10:
        yield Message('Я с тобой не разговариваю!')
        count += 1
    yield Message('Тебе не надоело?').make_keyboard([['Да'], ['Нет']])
