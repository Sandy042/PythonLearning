import requests
import json
city=input("Enter the city name to get weather details")
url=f"http://api.weatherapi.com/v1/current.json?key=72942e13875040629cb80922252303&q={city}&aqi=yes"
r=requests.get(url)
weather_dict=json.loads(r.text)
print(weather_dict["location"]["name"],weather_dict["current"]["temp_c"])
print(weather_dict["current"]["temp_c"])
