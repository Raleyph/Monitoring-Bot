import telebot
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

import weather
import config

from telebot import types

# настройка бота
bot = telebot.TeleBot(config.tg_token)


# клавиатура
kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)
kbrd.add("COVID-19", "Погода", "Последние новости", "Секретные функции")


# бд
conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()


# инициализация бд
def db_values(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO user_message (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	conn.commit()


def plot_set():
	x = np.random.randint(low=1, high=11, size=50)
	y = x + np.random.randint(1, 5, size=x.size)
	data = np.column_stack((x, y))
	 
	fig, (ax1, ax2) = plt.subplots(
		nrows=1, ncols=2,
		figsize=(8, 4)
	)

	ax1.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
	ax1.set_title('Scatter: $x$ versus $y$')
	ax1.set_xlabel('$x$')
	ax1.set_ylabel('$y$')
	 
	ax2.hist(
		data, bins=np.arange(data.min(), data.max()),
		label=('x', 'y')
	)
	 
	ax2.legend(loc=(0.65, 0.8))
	ax2.set_title('Frequencies of $x$ and $y$')
	ax2.yaxis.tick_right()
	 
	fig.savefig('cock')


# старт
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=kbrd)

	us_id = message.from_user.id
	us_name = message.from_user.first_name
	us_sname = message.from_user.last_name
	username = message.from_user.username

	db_values(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


# обработчик входящих данных
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'covid-19':
		plot_set()
		bot.send_photo(message.from_user.id, open("cock.png", 'rb'))
	elif message.text.lower() == 'погода':
		bot.send_message(message.from_user.id, weather.weather_message, parse_mode='html')
		print(weather.cloud_pos)
	else:
		bot.send_message(message.from_user.id, "Я не знаю что ответить :(")


bot.polling(none_stop=True)
