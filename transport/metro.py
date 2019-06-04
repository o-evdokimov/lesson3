#!/usr/local/bin/python3

# В этом задании требуется определить, на каких станциях московского метро 
# сейчас идёт ремонт эскалаторов и вывести на экран их названия

import json
from collections import Counter

def main():
    with open('data-397-2019-05-16.json','r', encoding = 'cp1251') as metro:
        data = json.loads(metro.read())

    print(data[0])
    exit
    stations_rep = [ [item['NameOfStation'],item['RepairOfEscalators']] for item in data ]
    stations = [ item['NameOfStation'] for item in data ]

    #stations1 = set(stations)
    #stations2 = list(stations1)

    #print(stations2)
    
    for station in stations_rep:
        if len(station[1]) != 0:
            print(f'Station: {station[0]}, Repair escalotors date: {station[1][0]["RepairOfEscalators"]}\n')

if __name__ == '__main__':
    main()