from django.shortcuts import render

# Create your views here.

def weather_info(request):
	return render(request,"weather/weather_info.html")