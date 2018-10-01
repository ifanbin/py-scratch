#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import bs4
import Handle

resources_file_path = '/flightNameList.txt'
scratch_url = 'http://www.variflight.com/sitemap.html?AE71649A58c77='


def scratch_flight_number(scratch_url, old_flights):
    new_flights = []
    data = requests.get(scratch_url).text
    soup = bs4.BeautifulSoup(data, "html.parser")
    a_flights = soup.find('div', class_='list').find_all('a', recursive=False)
    for flight in a_flights:
        if flight.text not in old_flights and flight.text != '国内航段列表':
            new_flights.append(flight.text)
    return new_flights


if __name__ == '__main__':
    #执行scratch_flight_number函数，传入resources_file_path，scratch_url参数
    Handle.handle(resources_file_path, scratch_url, scratch_flight_number)
