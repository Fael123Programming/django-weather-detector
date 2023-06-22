import json
import urllib.request
from django.shortcuts import render
from decouple import config

def index(request):
    city = ''
    weather_data = None
    if request.method == 'POST':
        city = request.POST['city'].strip();
        if len(city) > 0:
            city_url = city.replace(' ', '+')
            api_key = config('API_KEY')
            response = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city_url}&appid={api_key}&units=metric')
            json_data = json.loads(response.read())
            weather_data = {
                "country_code": str(json_data["sys"]["country"]),
                "coordinates": str(json_data["coord"]["lon"]) + "," + str(json_data["coord"]["lat"]),
                "temp": str(json_data["main"]["temp"]) + " °C",
                "pressure": str(json_data["main"]["pressure"]),
                "hum": str(json_data["main"]["humidity"]) 
            }
        
    context = {
        'city': city[0].upper() + city[1:] if len(city) > 0 else city,
        'weather_data': weather_data
    }
    
    return render(request, 'index.html', context)
