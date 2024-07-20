import requests

zip_code = input('Enter the zip code for the weather?\n')
url = 'http://api.weatherapi.com/v1/current.json?key=08a00cd44a284d2ea6c183106242007&q='+zip_code+ '&aqi=no'
response = requests.get(url)
weather_json = response.json()


temp = weather_json.get('current').get('temp_f')
area = weather_json.get('location').get('name')  # Corrected to get the name of the area
region = weather_json.get('location').get('region')  # Added to get the region
description = weather_json.get('current').get('condition').get('text')

print(f"Today's weather in {area}, {region} is {description} and {temp} degrees.")