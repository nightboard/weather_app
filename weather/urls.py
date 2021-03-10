from django.urls import path
from . import views

app_name = "weather"
urlpatterns = [
	path('weather_info/',views.weather_info,name="weather_info"),
]