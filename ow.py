#!/usr/bin/env python3

import json
import requests

def print_ver_info():
    print("====================================================")
    print("          Welcome to OpenWindow v1.0")	
    print("====================================================")

def apisetup(city_id):
    key = '0000000000000000000000000000' # placeholder
    print("> SETTING UP API REQUEST...")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "id=" + city_id + "&appid=" + key + "&units=imperial"
    return(complete_url)

def get_loc():
    # Prompt user for loc
    city_in = input("Wassup bro, what city are you chillin in? ")
    state_in = input("..and homie what state is that? (2 letters pls) ")
    print("Oh word, you in " + city_in + ", " + state_in + ". Let me check that...")
    city_id = loc_ver(city_in, state_in)
    return str(city_id)

'''
The OpenWeather API has a bigass JSON file with all the cities.
Search that bitch to esnure the user has put in a valid loc
This assumes that there is only a single instance of a city in a given state...
...which I hope is true...idk...

@inputs: {city}{state}
@returns: {city_id} and a message on success
'''
def loc_ver(city, state):
    f = open('city.list.json',)
    city_data = json.load(f)
    for entry in city_data:
        if city == entry['name'] and state == entry['state']:
            print('> CITY IDENTIFIED...')
            return entry['id']

    f.close()

'''
Call the OpenWeather API using the city_id
@input: weather ID
@returns: raw weather data
'''
def get_weather(city_id):
    req = apisetup(city_id)
    print("> SENDING REQUEST...")
    ret = requests.get(req).json()
    print("> RESPONSE RECIEVED...")
    print("***************************")
    print("CURRENT TEMP: " + str(ret['main']['feels_like']) + " F")
    print("***************************")

def main():
    print_ver_info()
    loc_id = get_loc()
    get_weather(loc_id)

if __name__ == "__main__":
    main()
