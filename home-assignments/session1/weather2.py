import urllib
import json
import requests
import pycountry
import socket
from requests import get

ip = "208.67.222.222"

latlong = get('https://ipapi.co/{}/latlong/'.format(ip)).text.split(',')

url_3 = get("http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=3c4744337b9371cb417e061754f3e61f".format(latlong[0], latlong[1])).json()

latlong = get('https://ipapi.co/{}/latlong/'.format(ip)).text.split(',')

formatted_data = url_3['main']['temp']


print ("The weather at my coordintes is " + str(formatted_data))




url = "http://api.openweathermap.org/data/2.5/weather?appid=3c4744337b9371cb417e061754f3e61f&q="

cities = {'London', 'Tel Aviv', "Rome"}

for city in cities:
	app_city_file = requests.get(url+city)
	app_json_file = app_city_file.json()
	temperature =  app_json_file['main']['temp']
	print ("The weather in " + city + " is " + str(temperature) + " degrees")


quit()

