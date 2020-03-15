'''
Python program to find out what the weather's like.
Overall, the program does the following:
    • Reads the requested location from the command line.
    • Downloads JSON weather data from OpenWeatherMap.org.
    • Converts the string of JSON data to a Python data structure.
    • Prints the weather for today and the next two days

'''
import json
import requests
import sys

if len(sys.argv) < 2:
    print('Usage: quick location')
    sys.exit()
location = ' '.join(sys.argv[1:])

#Download the JSON data from the APIs.
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&appid=b6907d289e10d714a6e88b30761fae22' % (location)
response = requests.get(url)
response.raise_for_status()

#Load JSON into a var
weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s: ' % (location))

for v in w:
    print(v['weather'][0]['main'], '-', x['weather'][0]['description'])
'''
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
'''