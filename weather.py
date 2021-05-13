import requests

url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "0ed6bea952e8ed0e7b869b68cd7c595f"

params = {"APPID": api_key, "q": "Новосибирск", "units": "metric", "lang": "ru"}
result = requests.get(url, params=params)
weather = result.json()
print(result.url)