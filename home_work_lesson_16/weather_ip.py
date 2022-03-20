import requests
import xmltodict, json


def get_location(ip_data):

    url = ip_data
    headers = {
        'x-rapidapi-host': "ip-geolocation-ipwhois-io.p.rapidapi.com",
        'x-rapidapi-key': "REMOVED"
    }

    response_l = requests.request("GET", url, headers=headers).text

    json_object = json.loads(response_l)
    country = json_object['country']
    city = json_object['city']
    country_code = json_object['country_code']
    region = {'country': json_object['country'], 'city': json_object['city'], 'country_code': json_object['country_code'].lower()}
    return region



def get_weather():
    ip_data = 'http://ipwhois.app/json/'
    weather_region = get_location(ip_data)

    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q": f"{weather_region['city']}, {weather_region['country_code']}", "lat": "0", "lon": "0",
                   "callback": "", "id": "2172797", "lang": "null",
                   "units": "metric", "mode": ""}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "REMOVED"
    }

    response_w = requests.request("GET", url, headers=headers, params=querystring).text
    json_object_w = json.loads(response_w)

    print('Temperature (celsius): ', json_object_w['main']['temp'])
    print('Weather:', json_object_w['weather'][0]['main'])
    print(weather_region['city'], ' ', weather_region['country'])

get_weather()

