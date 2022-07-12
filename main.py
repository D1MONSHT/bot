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

user_dict = {}  # {1234567890: {'photo': photo_id, 'caption': some_text}}


def start_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    send = types.InlineKeyboardButton(text='send photo', callback_data='send')
    keyboard.add(send)
    return keyboard


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(
        message.chat.id,
        'Выберите действие ⤵', reply_markup=start_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == 'send')
def admin_send(call):
    bot.send_message(call.from_user.id, 'Отправьте картинку.')
    bot.register_next_step_handler(call.message, photo_handler)


def photo_handler(message):
    try:
        # если изображение есть в словаре - заменяем его и убираем описание
        if user_dict.get(message.chat.id) is not None:
            user_dict[message.chat.id]['photo'] = message.photo[len(message.photo) - 1].file_id
            user_dict[message.chat.id]['caption'] = ''
        else:
            # если фото нет - создаем словарь и добавляем изображение
            user_dict[message.chat.id] = {'photo': '', 'caption': ''}
            user_dict[message.chat.id]['photo'] = message.photo[len(message.photo) - 1].file_id
    except Exception as e:
        bot.reply_to(message, e)
    else:
        bot.send_message(message.chat.id, 'Теперь введите текст к картинке')
        bot.register_next_step_handler(message, text_handler)


def text_handler(message):
    # добавляем описание изображения фото в словарь
    user_dict[message.chat.id]['caption'] = message.text
    bot.send_message(message.chat.id, 'Напишите "отправить" чтобы разослать картинку пользователям')
    bot.register_next_step_handler(message, send_to_users)


def send_to_users(message):
    if message.text.lower() == 'отправить':
        # здесь можно добавить отправку в цикле      
        bot.send_photo(
            message.chat.id,
            photo=user_dict[message.chat.id]['photo'],
            caption=user_dict[message.chat.id]['caption'],
            parse_mode='HTML'
        )
    else:
        bot.send_message(message.chat.id, 'Напишите "отправить" чтобы разослать картинку пользователям')
        bot.register_next_step_handler(message, send_to_users)


bot.polling(none_stop=True, interval=0)
Последнее редактирование: Янв 13, 2022
Мне нравится Реакции:rosvo
 0 
rosvo
rosvo


if __name__ == '__main__':
    if os.environ.get("IS_PRODUCTION", "False") == "True":
        app.run()
    else:
        bot.infinity_polling()
