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
temperature = w.temperature('celsius')['temp']
max_t = w.temperature('celsius')['temp_max']
min_t = w.temperature('celsius')['temp_min']

cloud_pos = w.clouds

if 0 < cloud_pos <= 10:
	all_weather = "Ясно"
elif 10 < cloud_pos <= 30:
	all_weather = "Переменная облачность"
elif 30 < cloud_pos <= 60:
	all_weather = "Облачно"
elif 60 < cloud_pos <= 100:
	all_weather = "Пасмурно"

weather_message = f"<b>Погода в Краматорске:</b>\n" \
				  f"Температура воздуха: {temperature}\n" \
				  f"Атмосферное давление: \n" \
				  f"Ветер: \n" \
				  f"Погода: {all_weather}"
