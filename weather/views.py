from django.shortcuts import render
from . import weather_data

# Create your views here.

def weather_info(request):
	weather_table = weather_data.get_weather_data()
	return render(request,"weather/weather_info.html",{"weather_table":weather_table})