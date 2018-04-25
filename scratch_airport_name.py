# -*- coding: UTF-8 -*-
import requests
import bs4
import json
import Handle

resources_file_path = '/airportNameList.txt'
scratch_url = 'https://data.variflight.com/profiles/profilesapi/search'


def scratch_airport_name(scratch_url, old_airports):
    new_airports = []
    data = requests.get(scratch_url).text
    all_airport_json = json.loads(data)['data']['list']
    for airport_by_word in all_airport_json.values():
        for airport in airport_by_word:
            if airport['profiles_city'] and airport['profiles_name'] not in old_airports:
                new_airports.append(airport['profiles_city'] + ',' + airport['profiles_name'])
    return new_airports


if __name__ == '__main__':
    Handle.handle(resources_file_path, scratch_url, scratch_airport_name)
