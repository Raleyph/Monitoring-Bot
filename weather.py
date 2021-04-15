import pyowm
import config

from pyowm.utils.config import get_default_config

# конфиг
config_dict = get_default_config()
config_dict['language'] = 'ru'


# переменные
owm = pyowm.OWM(config.owm_token, config_dict)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Kramatorsk, UA')
w = observation.weather


# вывод
temperature = round(w.temperature('celsius')['temp'], 1)
press = round(w.pressure['press'] * 0.750062)
wind_speed = round(w.wind()['speed'])
wind_target = w.wind()['deg']

cloud_pos = w.clouds
hum = w.humidity

# какое небо...
if 0 < cloud_pos <= 10:
	all_weather = "Ясно"
elif 10 < cloud_pos <= 30:
	all_weather = "Переменная облачность"
elif 30 < cloud_pos <= 60:
	all_weather = "Облачно"
elif 60 < cloud_pos <= 100:
	all_weather = "Пасмурно"

# время говнокода и техники "индус"
if 337.5 < wind_target <= 22.5:
	wind_t = "Северный"
elif 157.5 < wind_target <= 202.5:
	wind_t = "Южный"
elif 67.5 < wind_target <= 112.5:
	wind_t = "Восточный"
elif 247.5 < wind_target <= 292.5:
	wind_t = "Западный"
elif 25.5 < wind_target <= 67.5:
	wind_t = "Северо-восточный"
elif 112.5 < wind_target <= 157.5:
	wind_t = "Юго-восточный"
elif 202.5 < wind_target <= 247.5:
	wind_t = "Юго-западный"
elif 292.5 < wind_target <= 337.5:
	wind_t = "Северо-западный"

# сообщение
weather_message = f"<b>Погода в Краматорске:</b>\n" \
				  f"{all_weather}\n" \
				  f"\n" \
				  f"Температура воздуха: {temperature} °C\n" \
				  f"Атм. давление: {press} мм рт. ст.\n" \
				  f"\n" \
				  f"Ветер: {wind_t}, {wind_speed} м/с\n" \
				  f"\n" \
				  f"Влажность: {hum} %\n"
