import requests,json


base_url = "http://api.openweathermap.org/data/2.5/weather?"

def backend_city_name(city):
    city_name = city

    api_key="8c5c31a9e03243b85ae8814d2a0394da"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        return(x)
    else:
        x={}

    return res
