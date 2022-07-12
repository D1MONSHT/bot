#  Copyright (c) ChernV (@otter18), 2021.

import os
import random

from setup import bot, logger
from webhook import app

# --------------- dialog params -------------------
dialog = {
    'hello': {
        'in': ['привет', 'hello', 'hi', 'privet', 'hey'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!']
    },
    'how r u': {
        'in': ['как дела', 'как ты', 'how are you', 'дела', 'how is it going'],
        'out': ['Хорошо', 'Отлично', 'Good. And how are u?']
    },
    'name': {
        'in': ['зовут', 'name', 'имя'],
        'out': [
            'Я telegram-template-bot',
            'Я бот шаблон, но ты можешь звать меня в свой проект',
            'Это секрет. Используй команду /help, чтобы узнать'
        ]
    }
}


# --------------- bot -------------------
@bot.message_handler(commands=['help', 'start'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(
        message.chat.id,
        '<b>Hello for bot!</b>',
        parse_mode='html'
    )
@bot.message_handler(commands=['list'])

def say_list(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_photo(message.chat.id, 'https://www.google.com/search?q=%D1%84%D0%BE%D1%82%D0%BE&sxsrf=ALiCzsaYhI-PVwB3DHMiFOEcxi1fMVFJXQ:1657642627491&tbm=isch&source=iu&ictx=1&vet=1&fir=zKA8Ct0R5qPKGM%252C0VIOfvdZkqu73M%252C_%253BtjaOjcbyWAenTM%252Cqv3bYgAKOmFK9M%252C_%253BkQ4ie-ohy9OThM%252CTk1lAhrAMtACXM%252C_%253BHgZWKUUFpwmrIM%252C989fVJpn7S7e0M%252C_%253Bszq9pXtD1OugNM%252CUf0Kd7wb6NMOQM%252C_%253BfK7SylISiIx1-M%252CVTiWAQsfu3ZyUM%252C_%253BO3oosmQ_Hg1o-M%252Cs-3xaS9p91GbvM%252C_%253BSmaLNhjYJWX97M%252CymXz8zPLcPB7rM%252C_%253BeH6xhsVRGRkUsM%252CcyM20HpU-UzH6M%252C_%253BZOnJnqXnI1IqwM%252Cw8OFW9wEubEiLM%252C_%253BFd2HV93btDH6YM%252Cs-3xaS9p91GbvM%252C_%253B6TZUCyv2nUgKgM%252CSTlVqyv8LyMZTM%252C_%253BhjWMM1IOTHoVcM%252CTk1lAhrAMtACXM%252C_&usg=AI4_-kRAjTLp6DbQwODd_EVKp0jQBz7PWQ&sa=X&ved=2ahUKEwjjmuf_3_P4AhUSSxoKHWTzCtAQ9QF6BAgJEAE&biw=1366&bih=625&dpr=1#imgrc=eH6xhsVRGRkUsM')

    if __name__ == '__main__':
    if os.environ.get("IS_PRODUCTION", "False") == "True":
        app.run()
    else:
        bot.infinity_polling()
