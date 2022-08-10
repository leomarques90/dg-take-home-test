import os
import requests
import logging
import json

BASE_URL_SAMPLE_DATA = "https://api.openweathermap.org/data/2.5/weather"
BASE_URL_HISTORICAL_DATA = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
API_KEY = os.getenv("API_KEY")

logging.basicConfig(level=logging.INFO)


def get_data_from_api(url: str, params: dict):
    return requests.get(url, params=params).json()


def write_file(content, path_file: str) -> None:
    with open(path_file, 'w') as f:
        f.write(content)


def get_cities_lat_long(cities):
    cities_with_lat_lon = {}

    for city in cities:
        logging.info(f"Getting latitude and longitude for city {city}...")

        params = {
            "q": city,
            "appid": API_KEY
        }

        response = get_data_from_api(BASE_URL_SAMPLE_DATA, params)

        city_lat_long = response["coord"]
        cities_with_lat_lon.update({city: city_lat_long})

        logging.info(
            f"Latitude and longitude successfully recovered for city {city}!")

    logging.info(f"All latitude and longitude values were recovered")

    return cities_with_lat_lon


def _main():
    cities = [
        "Shenzhen", "Fez", "Rio De Janeiro", "Taipei", "São Paulo", "Isfahan", "Warsaw", 
        "Bengaluru", "Dar es Salaam", "Nagpur"
    ]  # list generated by https://www.randomlists.com/random-world-cities?dup=false&qty=10

    sample_file = "cities-lat-long.json"
    raw_dir = "data/01_raw"

    cities_with_lat_lon = json.load(open(f"{raw_dir}/{sample_file}")) if sample_file in os.listdir(raw_dir) else get_cities_lat_long(cities)

    print(cities_with_lat_lon)


if __name__ == '__main__':
    _main()
