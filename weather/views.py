from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = '5b1df83a508d4adf5fdafa864d54f06d'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    all_city_info = []
    cities = City.objects.all()

    for city in cities:
        try:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': res['name'],
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
            }
            all_city_info.insert(0, city_info)
        except Exception:
            pass

    context = {'all_info': all_city_info, 'form': form}

    return render(request, 'weather/index.html', context)