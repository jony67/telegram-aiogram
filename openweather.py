# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 20:12:09 2020
Получение сведений о текущей погоде и прогнозе с использованием бесплатного
ключа API сайта OpenWeather (https://openweathermap.org/)
@author: sutyamov
"""
import requests
import json
from config import KEY

# Для передачи KEY через параметр виртуального окружения
#import os
#KEY = os.getenv("KEY")

###############################################################################
# Исходные данные
###############################################################################
lang = 'ru'
units = 'metric'  # единицы измерения: standard, metric, imperial
###############################################################################
# Сведения о текущей погоде
###############################################################################
# ------------------------------------------------------------------------------
# Доступные URL API для текущей погоды (Current weather API):
# ------------------------------------------------------------------------------
# - по городу:
# 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
# 'https://api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={API key}'
# 'https://api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}'
# 'https://api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}'
# - по географическим координатам:
# 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
# - по zip-коду:
# 'https://api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}'
# - для нескольких городов в прямоугольной области координат:
# 'https://api.openweathermap.org/data/2.5/box/city?bbox={bbox}&appid={API key}'
# - для нескольких городов в окружности:
# 'https://api.openweathermap.org/data/2.5/box/city?bbox={bbox}&appid={API key}'
# - для нескольких городов по ID:
# 'https://api.openweathermap.org/data/2.5/group?id={id,..,id}&appid={API key}'
# ------------------------------------------------------------------------------
# Функция проверки статуса ответа на запрос
# ------------------------------------------------------------------------------
def status_response(response):
    s = ''
    if response.status_code == 200:
        return True
    if response.status_code == 401:
        s = 'Получен ответ 401. Авторизация не произведена, проверьте API-ключ!\n'
        return s
    if response.status_code == 403:
        s = 'Получен ответ 403. Доступ на сервер закрыт для данного API!\n'
        return s
    if response.status_code == 404:
        s = 'Получен ответ 404. Город не существует, сервер недоступен или неправильный URL!\n'
        return s


# ------------------------------------------------------------------------------
# Функция перевода градусов в румбы
# ------------------------------------------------------------------------------
def wind_direction(deg):
    if (deg > 0 and deg <= 11.25) or (deg > 348.75 and deg <= 0):
        return 'С,'
    elif deg > 11.25 and deg <= 33.75:
        return 'СCВ,'
    elif deg > 33.75 and deg <= 56.25:
        return 'СВ,'
    elif deg > 56.25 and deg <= 78.75:
        return 'ВСВ,'
    elif deg > 78.75 and deg <= 101.25:
        return 'В,'
    elif deg > 101.25 and deg <= 146.25:
        return 'ВЮВ,'
    elif deg > 146.25 and deg <= 168.75:
        return 'ЮВ,'
    elif deg > 168.75 and deg <= 191.25:
        return 'ЮЮВ,'
    elif deg > 191.25 and deg <= 213.75:
        return 'Ю,'
    elif deg > 213.75 and deg <= 236.25:
        return 'ЮЮЗ,'
    elif deg > 236.25 and deg <= 258.75:
        return 'ЮЗ,'
    elif deg > 258.75 and deg <= 281.25:
        return 'ЗЮЗ,'
    elif deg > 281.25 and deg <= 303.75:
        return 'З,'
    elif deg > 303.75 and deg <= 326.25:
        return 'ЗСЗ,'
    elif deg > 326.25 and deg <= 348.75:
        return 'СЗ,'
    elif deg > 0 and deg <= 150.25:
        return 'ССЗ,'
    else:
        return 'недоступно'


# ------------------------------------------------------------------------------
# Функция вывода текущей погоды для выбранного города
# ------------------------------------------------------------------------------
def сurrent_weather(obj_txt):
    weather = json.loads(obj_txt)
    answer = ('1. Координаты города:'
              + '\n- широта: ' + str(weather['coord']['lat'])
              + '\n- долгота: ' + str(weather['coord']['lon'])
              + '\n2. Погода:'
              + '\n- описание: ' + weather['weather'][0]['description']
              + '\n3. Температура:'
              + '\n- сейчас: ' + str(round(weather['main']['temp'])) + u'\u2103'
              + '\n- ощущается как: ' + str(round(weather['main']['feels_like'])) + u'\u2103'
              + '\n4. Атмосферное давление: ' + str(round(weather['main']['pressure'] / 1.333)) + 'мм рт.ст.'
              + '\n5. Видимость: ' + str(weather['visibility']) + 'м'
              + '\n6. Ветер: ' + str(wind_direction(weather['wind']['deg'])) + ' ' + str(weather['wind']['speed']) + 'м/с'
              + '\n7. Влажность: ' + str(weather['main']['humidity']) + '%'
              + '\n9. Облачность: ' + str(weather['clouds']['all']) + '%'
              )
    return answer

# ------------------------------------------------------------------------------
# Функция вывода
# ------------------------------------------------------------------------------
def print_weather(city):
    answer = ''
    url = 'https://api.openweathermap.org/data/2.5/weather/?q=%s&lang=%s&units=%s&appid=%s' % (
        city, lang, units, KEY)
    response_town = requests.get(url)
    if status_response(response_town) == True:
        answer = сurrent_weather(response_town.text)
        return answer
    else:
        answer = status_response(response_town)
        return answer

# ------------------------------------------------------------------------------
