from bs4 import BeautifulSoup
import requests

def get_weather_data():

	# url to take live weather data
	url = "https://www.weather-forecast.com/countries/India-1"

	# get webpage source
	source = requests.get(url).text
	soup = BeautifulSoup(source,'lxml')

	# get weather_table
	weather_table = soup.find(class_="top-city-list-per-country")
	weather_table = weather_table.find_all('li')

	weather_report = []
	for li in weather_table:
		country_name = li.a.text
		weather_info = li.div.img['alt']
		weather_report.append((country_name,weather_info))

	# print(weather_report)
	return weather_report

if __name__ == '__main__':
	get_weather_data()