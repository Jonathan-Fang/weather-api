# Import required libraries
import requests

# Notes
# https://console.cloud.google.com/apis/credentials/key/c8751f47-8eec-4042-a17a-8c6db94dec87?project=geocode-api-395201
# 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

# ask what city they want the weather for and take user input
location = input('Where do you want to know the weather for?\n') # \n newline, line break

# turn the user input, feed it into geocode, return latitude and longitude
get_link = "https://geocode.maps.co/search?q=" + location

geocode_API = requests.get(get_link)

# spit out json
geocode_json_output = geocode_API.json()

# navigate
lat = geocode_json_output[0]["lat"]
lon = geocode_json_output[0]["lon"]

response_API = requests.get('https://api.weather.gov/points/' + lat + ',' + lon)
# fetch data from weather API; latitude to gridpoint
# response_API = requests.get('https://api.weather.gov/points/38.8894,-77.0352')

# rename and takes output
coords_json_output = response_API.json()

# print dict; key and value
# print(coords_json_output["properties"]["forecast"]) # success

# rename
gridpoint = coords_json_output["properties"]["forecast"]

# navigate to the thing; gridpoint to forecast; fetch data
forecast_response_API = requests.get(gridpoint)

# rename and takes output
forecast_response_output = forecast_response_API.json()

# print(forecast_response_output["properties"]["periods"]) # success

# rename
checkpoint = forecast_response_output["properties"]["periods"][0]

weather_prompt = location + "'s weather: "

print(weather_prompt + checkpoint["detailedForecast"]) # success