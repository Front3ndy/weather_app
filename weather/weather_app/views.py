from django.shortcuts import render
from django.views.generic import TemplateView

from .WeatherRequest import WeatherRequest

class MainView(TemplateView):
    template_name = 'weather_app/index.html'

    def get_context_data(self, **kwargs):
        """ Получаем query. Создаем экземпляр класса WeatherRequest, куда передаем query """
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query')

        # Проверка query
        if query is not None:
            wr = WeatherRequest(query)
            context = {
                'city_name': query,
                'current_temp': wr.get_temperature()
            }
        return context


