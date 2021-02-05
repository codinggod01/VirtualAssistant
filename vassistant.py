import requests

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input()
complete_url = base_url + "q=" + city_name + "&appid=81a878e98ce752a3fee561bd5c21c696"


response = requests.get(complete_url, timeout=30)

x = response.json()

print(x)
