#!/usr/local/bin/python3

from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city("Moscow")
    if weather:
        return f"{weather['temp_C']} {weather['FeelsLikeC']}"
    else: return "Service unavailable"
if __name__ == '__main__':
    app.run(debug=True)