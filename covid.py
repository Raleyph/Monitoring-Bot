import COVID19Py

covid = COVID19Py.COVID19()
location = covid.getLocationByCountryCode("UA")

date = location[0]['last_updated'].split("T")
time = date[1].split(".")

covid_message = f"<u>Данные по Украине:</u>\n" \
				f"Население: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\n" \
				f"<u>Последние данные:</u>\n" \
				f"<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n" \
				f"<b>Смертей: </b>{location[0]['latest']['deaths']:,}"
