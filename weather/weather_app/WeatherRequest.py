from datetime import date
import datetime

import geocoder
import requests


class WeatherRequest:

    """ Класс, ответсвенный за запрос к API. Подготавливает url и делает запрос """
    def __init__(self, city_name='Moscow'):
        """ Название города на английском языке """
        self.city_name = city_name

    def _setup(self):
        """ Получаем координаты города(широта и долгота). После делаем запрос на API с текущей датой и координатами """
        coords = (round(geocoder.arcgis(self.city_name).json['lat'], 2), round(geocoder.arcgis(self.city_name).json['lng'], 2))
        now_datetime = date.today()
        url = f'https://api.open-meteo.com/v1/forecast?latitude={coords[0]}&longitude={coords[1]}&hourly=temperature_2m&start_date={now_datetime}&end_date={now_datetime}'
        return url

    def get_temperature(self):
        """ Получаем температуру на данный час """
        url = self._setup()
        response = requests.get(url=url)
        hour = datetime.datetime.now().hour
        temperature = response.json()['hourly']['temperature_2m']
        return round(temperature[hour])

