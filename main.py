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
    bot.send_photo(message.chat.id, 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fkartinkin.net%2Fuploads%2Fposts%2F2022-02%2F1645962851_1-kartinkin-net-p-krasivie-kartinki-devushek-narisovannie-1.jpg&imgrefurl=https%3A%2F%2Fkartinkin.net%2F75043-krasivye-kartinki-devushek-narisovannye.html&tbnid=7fF-_j2LRWbq4M&vet=12ahUKEwjAyZ6b4_P4AhWIo3IEHTQbBjYQMygBegUIARCyAQ..i&docid=O2WmcBCAmLgULM&w=1024&h=1280&q=%D1%84%D0%BE%D1%82%D0%BE&hl=ru&ved=2ahUKEwjAyZ6b4_P4AhWIo3IEHTQbBjYQMygBegUIARCyAQ')

    if __name__ == '__main__':
    if os.environ.get("IS_PRODUCTION", "False") == "True":
        app.run()
    else:
        bot.infinity_polling()
