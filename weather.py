import requests

url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "0ed6bea952e8ed0e7b869b68cd7c595f"

def weather(city_name):
    params = {"APPID": api_key, "q": city_name, "units": "metric", "lang": "ru"}
    result = requests.get(url, params=params)
    weather = result.json()
    print(weather)
    result = ""
    if weather['cod'] == '404':
        result = "Город не найден"
    else:
        result = "В городе " + weather['name'] + '\n'
        result += "Погода: "+ weather['weather'][0]['description'] +"\n"
        result += "Температура " + str(weather['main']['temp']) + "°C\n"
        result += "Ощущается как " + str(weather['main']['feels_like']) + "°C\n"
        result += "Давление " + str(weather['main']['pressure']) + "ммрт\n"
        result += "Влажность " + str(weather['main']['humidity']) + "%\n"
        result += "Скорость ветра " + str(weather['wind']['speed']) + "м/с\n"
        result += "Восход " + str(weather['sys']['sunrise']) + "\n"
        result += "Закат " + str(weather['sys']['sunset']) + "\n"
    return result

city_name = input("Введи название города: ")
data = weather(city_name)
print(data)