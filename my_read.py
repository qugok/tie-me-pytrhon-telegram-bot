def read_telegram_token():
    with open('myToken') as f:
        my_token = f.readline().replace('\n', '')
    return my_token

def add_users(*args):
    with open('users') as f:
        old_users = f.read().split()
    print(old_users)
    print(args)
    with open('user', 'w') as f:
        f.write('\n'.format(*old_users, *args))

# def read_message(message_name: str):
#     with open('messages/' + message_name, encoding='utf-8') as f:
#         message = f.read()
#     return message
