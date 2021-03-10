from bs4 import BeautifulSoup
import requests

def get_weather_data():

	# url to take live weather data
	url = "https://www.timeanddate.com/weather/?continent=asia"

	# get webpage source
	source = requests.get(url).text
	soup = BeautifulSoup(source,'lxml')

	# get weather_table
	weather_table = soup.findAll('table')
	weather_table = weather_table[0]

	weather_table.findAll('tr')

	return weather_table

if __name__ == '__main__':
	get_weather_data()