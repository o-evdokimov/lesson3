#!/usr/local/bin/python3

# Объединить наборы данных из предыдущих задач и посчитать, 
# у какой станции метро больше всего остановок (в радиусе 0.5 км).

# Output: 
# ................
# Super station is Юго-Западная, вход-выход 3 в южный вестибюль, stops = 32


import json
import time
from collections import Counter
from math import sin, cos, sqrt, atan2, radians

def get_distance(p1,p2):
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(p1[0])
    lon1 = radians(p1[1])
    lat2 = radians(p2[0])
    lon2 = radians(p2[1]) 
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def main():
    
    max_distance = 0.5
    zero_coordinate = [55.751999, 37.617734]

    with open('data-398-2019-05-28.json','r', encoding = 'cp1251') as transport:
        data_stops = json.loads(transport.read())

    with open('data-397-2019-05-16.json','r', encoding = 'cp1251') as metro:
        data_metro = json.loads(metro.read())

    #on_earth_stations = [ [item['Name'],item['geoData']['coordinates']] for item in data_stops ]
    on_earth_stations = {item['Name']:item['geoData']['coordinates'] for item in data_stops}
    #metro_stations = [ [item['Name'],item['geoData']['coordinates']] for item in data_metro ]  
    metro_stations = {item['Name']:item['geoData']['coordinates'] for item in data_metro}


    #print(on_earth_stations[])
    sorted_d = sorted((value[0] + value[1]) for (key,value) in on_earth_stations.items())
    print(sorted_d)
    exit(1)
    i=0
    max_number_stops=0
    for metro_station_name in metro_stations.keys():
        n = 0
        i+=1
        for on_earth_station_name in on_earth_stations.keys():
            x1 = on_earth_stations[on_earth_station_name][0]
            y1 = on_earth_stations[on_earth_station_name][1]
            x2 = metro_stations[metro_station_name][0]
            y2 = metro_stations[metro_station_name][1]
            distance = get_distance([x1,y1],[x2,y2])
            if distance <= max_distance:
                n+=1
        super_metro_station_candidate = {"Name":metro_station_name, "CountStops":n}
        if super_metro_station_candidate["CountStops"] > max_number_stops:
            result = super_metro_station_candidate
            max_number_stops = super_metro_station_candidate["CountStops"]
        print('.'*n)
    print(f'Super station is {result["Name"]}, stops = {result["CountStops"]}')

if __name__ == '__main__':
    t1 = time.time()
    main()
    print(f'   total time = {int(time.time() - t1)}')