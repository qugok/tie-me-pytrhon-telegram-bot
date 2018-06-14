import random

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
    update = yield Message(r'Привет, я Александр Александрович В и я очень люблю платки и шарфики! Меня создали для того, что бы помочь тебе выглядеть стильно и изящно с помощью твоего красивого платочка/шарфика! Хочешь увидеть варианты? Пиши да или /next или /get, и я пришлю тебе картинку и инструкцию, как это сделать.')
    image = MyImage()
    # image = MyLinkImage()
    answer = update.message
    while True:
        if answer.text.startswith('/help'):
            update = yield Message('Меня создали для того, что бы помочь тебе выглядеть стильно и изящно с помощью твоего красивого платочка/шарфика! Хочешь увидеть варианты? Пиши да или /next или /get, и я пришлю тебе картинку и инструкцию, как это сделать.')
            answer = update.message
            continue

        if answer.text.startswith('/next') or answer.text.startswith('/get') or answer.text.lower().startswith('да'):
            # print('start get')
            try:
                picture = next(image)
            except Exception as e:
                picture = Message('Теперь все распространенные способы привязывания вам известны. Остальное, дело ваших рук и фантазии!)', 'Пиши да или /next или /get, если хочешь ещё раз')
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
    # random.shuffle(l)
    for i in l:
        pic = open(str('Images/' + str(i) + '.jpg'), 'rb')
        with open(str('Images/' + str(i)), 'r') as r:
            texts = r.read().split()
        yield PhotoMessage(*texts, photo=pic, reverse=True)
        try:
            pic.close()
        except:
            pass

def MyLinkImage():
    with open('Images/count') as r:
        count = int(r.read())
    l = list(range(count))
    # random.shuffle(l)
    for i in l:
        with open(str('Images/' + str(i)) + 'link', 'r') as r:
            link = r.read()
        with open(str('Images/' + str(i)), 'r') as r:
            text = r.read()
        yield PhotoMessage(text, photo=link)


def openImage():
    update = yield Message('Введите названиие файла')
    name = update.message.text
    try:
        pic = open(str('Images/' + str(name)), 'rb')
        update = yield PhotoMessage('пытаюсь отправить фото', 'фото\n/open', photo=pic)
        try:
            pic.close()
        except:
            pass
        return update
    except:
        update = yield Message('что-то пошло не так')
        return update

def addImage():
    update = yield Message('отправьте картинку, которую хотите добавить\n/cancel чтобы отменить')
    while 'photo' not in update.message.__dict__ or len(update.message.photo) == 0:
        if update.message.text.startswith('/cancel'):
            update = yield Message('закончили')
            return update
        print('cycle')
        update = yield Message('вам нужно отправить картинку', 'отправьте картинку, которую хотите добавить')
    print('cycle end')
    photo = update.message.photo[0].get_file()
    print('photo get')
    update = yield Message('отправьте текст для картинки\n/clear если без подписи')
    text = update.message.text
    if text == '/cancel':
        update = yield Message('закончили')
        return update
    if text == '/clear':
        text = ''
    with open('Images/count') as r:
        count = int(r.read())
    pic = open(str('Images/' + str(count) + '.jpg'), 'xb')
    with open(str('Images/' + str(count)), 'x') as r:
        r.write(text)
    photo.download(out=pic)
    pic.close()
    with open('Images/count', 'w') as r:
        r.write(str(count + 1))
    update = yield Message('Done')
    return update

def adimin_bot(name=None):
    update = yield Message('hello Admin {}!'.format(name))
    answer = update.message
    while True:
        if answer.text.startswith('/help'):
            update = yield Message('/like_user to use user interface\n'
                                   '/end to end user interface\n'
                                   '/show_users to see users\n'
                                   '/add to add image\n'
                                   '/open to open image')
            answer = update.message
            continue

        if answer.text.startswith('/like_user'):
            try:
                update = yield from dialog(name)
                # print(update)
            except Exception as e:
                print('втф ?')
                print(e)
            answer.text = '/help'
            continue

        if answer.text.startswith('/open'):
            try:
                update = yield from openImage()
                # print(update)
            except Exception as e:
                print('втф ?')
                print(e)
            answer = update.message
            continue

        if answer.text.startswith('/add'):
            update = yield Message("sorry it don't works")
            answer = update.message
            continue
            try:
                update = yield from addImage()
                answer = update.message
                continue
            except Exception as e:
                print(e)

        update = yield Message('Я не понимаю что вы написали(',
                                        'Попробуйте подсказку\nТам всё, что я умею\nВы можете её вызвать командой /help\nУдачи!)')
        answer = update.message