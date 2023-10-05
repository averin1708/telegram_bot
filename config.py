import telebot
botTimeWeb = telebot.TeleBot('ваш токен из Воtfather')
from telebot import types
@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nКак у тебя дела?"
    mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, fr\nКак уcderffrrла?"
    markup = types.InlineKeyboardMarkup()
    button_good = types.InlineKeyboardButton(text = 'Хорошо', callback_data='good')
    button_bad = types.InlineKeyboardButton(text = 'Плохо', callback_data='bad')
    button_notvery = types.InlineKeyboardButton(text = 'Не очень', callback_data='notvery')
    markup.add(button_bad,button_good,button_notvery)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
botTimeWeb.polling(non_stop=True)
