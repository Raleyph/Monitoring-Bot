from telebot import types

tg_token = '1348869076:AAEkWZ5gEJl8sB7uMfWGvKCie6YTZFRTHxo'
owm_token = 'a99967bc9ee70d5b4bd387902982f400'

dollar = types.InlineKeyboardButton("$", callback_data='dl')
euro = types.InlineKeyboardButton("€", callback_data='eu')
rub = types.InlineKeyboardButton("₽", callback_data='rb')
btc = types.InlineKeyboardButton("₿", callback_data='bt')
eth = types.InlineKeyboardButton("Ξ", callback_data='eh')
