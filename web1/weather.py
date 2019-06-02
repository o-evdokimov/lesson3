#!/usr/local/bin/python3

# https://api.worldweatheronline.com/premium/v1/weather.ashx?key=e7706bc65d3143e1ab0213947190106&q=Moscow&format=json&num_of_days=1

import requests


def weather_by_city(city_name):
    params = {
        "key": "e7706bc65d3143e1ab0213947190106",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    weather_url = "https://api.worldweatheronline.com/premium/v1/weather.ashx"
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False

if __name__ == "__main__":
    print(weather_by_city("Moscow"))
