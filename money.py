from bs4 import BeautifulSoup
import requests

# страницы для парсинга
rub = "https://www.google.com/search?sxsrf=ALeKk03leJxfKpwQ3XHmAUsJYxa_4Be5pg%3A1618404974961&ei=buZ2YMj3OYvX3AOSgoaQCw&oq=курс+рубля&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEEYQggIyBQgAELEDMggIABCxAxCDATICCAAyAggAMgIIADIFCAAQsQMyAggAMgIIADIICAAQsQMQgwE6BwgAEEcQsAM6BwgAELADEEM6BwgAELEDEENQmEZY5Ulg30poAnACeACAAYMBiAHFBJIBAzUuMZgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwjI5omt5P3vAhWLK3cKHRKBAbIQ4dUDCA0&uact=5"
dol = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0&client=opera-gx&hs=hum&sxsrf=ALeKk0328ToFsW0GR7wsXJALgSuaALJi-w%3A1618421195181&ei=yyV3YIPQCvCrrgTBno2ACQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAMyDAgAEIcCEBQQRhCCAjIHCAAQhwIQFDIKCAAQsQMQgwEQCjICCAAyAggAMgIIADICCAAyAggAMgoIABCxAxCDARAKMgIIADoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoECCMQJzoICAAQsQMQgwE6BQgAELEDOgQIABBDOgkIIxAnEEYQggJQiL4BWJ3EAWCWyAFoAnACeACAAfgBiAGwBpIBBTUuMS4xmAEAoAEBqgEHZ3dzLXdpesgBCsABAQ&sclient=gws-wiz&ved=0ahUKEwjD4b3joP7vAhXwlYsKHUFPA5AQ4dUDCA0&uact=5"
eur = "https://www.google.com/search?sxsrf=ALeKk039bh6YjYMIind3JEd77p8wWt_p4g%3A1618405017680&ei=meZ2YMv3KKWtrgTjtbXYBw&oq=курс+евро&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEEYQggIyBQgAELEDMggIABCxAxCDATICCAAyCAgAELEDEIMBMgUIABCxAzIFCAAQsQMyAggAMggIABCxAxCDATIICAAQsQMQgwE6BwgjELADECc6BwgAEEcQsAM6BwgAELADEEM6CggAEIcCELEDEBRQwj9Yj0Rg6khoAnACeACAAaUBiAGDBJIBAzQuMZgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwiLqLnB5P3vAhWllosKHeNaDXsQ4dUDCA0&uact=5"
btc = "https://www.google.com/search?sxsrf=ALeKk039bh6YjYMIind3JEd77p8wWt_p4g%3A1618405017680&ei=meZ2YMv3KKWtrgTjtbXYBw&oq=курс+бит&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQsQMQRhCCAjIFCAAQsQMyAggAMgIIADIICAAQsQMQgwEyBQgAELEDMgIIADIFCAAQsQMyBQgAELEDMgIIADoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQhwIQsQMQFFDNJli7KGD5LWgCcAJ4AIABc4gBiAOSAQMzLjGYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz"
eth = "https://www.google.com/search?sxsrf=ALeKk02jwq6ZhsnTcv2znDBrJFuc_QfR2A%3A1618405041411&ei=seZ2YPfBGJa43APyrJ24CA&oq=курс+ефи&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQsQMQgwEQCjIECAAQCjIKCAAQsQMQgwEQCjIECAAQCjIECAAQCjIECAAQCjIKCAAQsQMQgwEQCjIECAAQCjIECAAQCjIECAAQCjoHCAAQRxCwAzoHCAAQsAMQQzoECCMQJzoKCAAQhwIQsQMQFDoICAAQsQMQgwE6AggAOgUIABCxAzoHCAAQhwIQFDoFCAAQyQNQ6kRYgFBgllhoAnACeACAAYMCiAG9BJIBBTEuMi4xmAEAoAEBqgEHZ3dzLXdpesgBCsABAQ&sclient=gws-wiz"

# рубль
full_page = requests.get(rub)
soup = BeautifulSoup(full_page.content, 'lxml')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

# доллар
full_page1 = requests.get(dol)
soup1 = BeautifulSoup(full_page1.content, 'lxml')
convert1 = soup1.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

# евро
full_page2 = requests.get(eur)
soup2 = BeautifulSoup(full_page2.content, 'lxml')
convert2 = soup2.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

# биткоин
full_page3 = requests.get(btc)
soup3 = BeautifulSoup(full_page3.content, 'lxml')
convert3 = soup3.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

# ефириум
full_page4 = requests.get(eth)
soup4 = BeautifulSoup(full_page4.content, 'lxml')
convert4 = soup4.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
