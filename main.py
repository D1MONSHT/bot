#  Copyright (c) ChernV (@otter18), 2021.

import os
import random

from setup import bot, logger
from webhook import app

# --------------- bot -------------------

@bot.message_handler(commands="start")
def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["С пюрешкой", "Без пюрешки"]
    keyboard.add(*buttons)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


    bot.send_message(message.chat.id, message.text)
@bot.message_handler(commands=["id"])

def get_id(message):

 logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used echo:\n\n%s', message.text)
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    if os.environ.get("IS_PRODUCTION", "False") == "True":
        app.run()
    else:
        bot.infinity_polling()
