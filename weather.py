import urllib2
import json

def url():
    f = urllib2.urlopen('http://api.wunderground.com/api/987077b70105ec11/hourly/q/NY/New_York_City.json')
    return f
#-----------------uses weather underground api

def getWeather():
  f = url()
  json_string = f.read()
  parsed_json = json.loads(json_string)
  weather = parsed_json['hourly_forecast'][0]['condition']
  f.close()
#-----------------what the sky should look like (ex: cloudy, rainy, etc.)
    return weather

def getTemp():
  f = url()
  json_string = f.read()
  parsed_json = json.loads(json_string)
  temp_f = parsed_json['hourly_forecast'][0]['temp']['english']
  f.close()
#-----------------the expected temperature in fahrenheit. celsius is possible by replacing 'english' with 'metric'
    return temp_f
