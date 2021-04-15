import telebot
import sqlite3

import weather
import covid
import money
import config

from telebot import types
from datetime import datetime

# настройка бота
bot = telebot.TeleBot(config.tg_token)

# клавиатура
kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)
kbrd.add("COVID-19", "Погода", "Последние новости", "Курс валют", "Рандомайзер", "➡️")

kbrd1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
kbrd1.add("Завершение работы", "Свернуть окна", "Закрыть окна", "⬅️", "???", "???")

markup = types.InlineKeyboardMarkup(row_width=3)
markup.add(config.dollar, config.euro, config.rub, config.btc, config.eth)

# бд
conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()


# инициализация таблицы пользователей
def db_values_us(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO user_message (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	conn.commit()


# инициализация таблицы действий с ПК
def db_values_pc(date: str, user_id: int, status: str):
	cursor.execute('INSERT INTO pc_status (date, user_id, status) VALUES (?, ?, ?)', (date, user_id, status))
	conn.commit()


# старт
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=kbrd)

	us_id = message.from_user.id
	us_name = message.from_user.first_name
	us_sname = message.from_user.last_name
	username = message.from_user.username

	db_values_us(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


# обработчик входящих данных
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == '➡️':
		bot.send_message(message.chat.id, 'Страница 2', reply_markup=kbrd1)
	elif message.text.lower() == '⬅️':
		bot.send_message(message.chat.id, 'Страница 1', reply_markup=kbrd)
	elif message.text.lower() == 'covid-19':
		bot.send_message(message.from_user.id, covid.covid_message, parse_mode='html')
	elif message.text.lower() == 'погода':
		bot.send_message(message.from_user.id, weather.weather_message, parse_mode='html')
	elif message.text.lower() == 'курс валют':
		bot.send_message(message.from_user.id, "Выберете валюту:", reply_markup=markup)
	elif message.text.lower() == 'завершение работы':
		us_id = message.from_user.id
		now = datetime.now()
		db_values_pc(date=now, user_id=us_id, status="OFF")
	else:
		bot.send_message(message.from_user.id, "Я не знаю что ответить :(")


# коллбэки для инлайн-клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
	try:
		if call.message:
			if call.data == 'dl':
				bot.send_message(call.message.chat.id, "Курс доллара: " + str(money.convert1))
	except Exception as e:
		print(repr(e))

# постоянная работа бота
bot.polling(none_stop=True)
