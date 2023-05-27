from django.shortcuts import render
import requests

def index(request):
    appid = '6a67aa38413b18c4c6d500ad1f260b13'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    
    city = 'London'
    res = requests.get(url.format(city)).json() 
# получили конвертирование json формата в словарь
    
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    context = {'info': city_info}
    return render(request, 'museum/index.html', context)
