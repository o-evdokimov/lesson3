#!/usr/local/bin/python3

# В этом задании требуется определить, на каких станциях московского метро 
# сейчас идёт ремонт эскалаторов и вывести на экран их названия

# Output:
#
# Station: Кузьминки, Repair escalotors date: 29.11.2018-30.01.2019
# Station: Рязанский проспект, Repair escalotors date: 12.12.2018-08.02.2019
# Station: Рязанский проспект, Repair escalotors date: 04.03.2019-30.04.2019
# Station: ЦСКА, Repair escalotors date: 25.02.2019-24.05.2019


import json
from collections import Counter

def main():
    with open('data-397-2019-05-16.json','r', encoding = 'cp1251') as metro:
        data = json.loads(metro.read())

    print(data[0])
    exit
    stations_rep = [ [item['NameOfStation'],item['RepairOfEscalators']] for item in data ]
    stations = [ item['NameOfStation'] for item in data ]
    
    for station in stations_rep:
        if len(station[1]) != 0:
            print(f'Station: {station[0]}, Repair escalotors date: {station[1][0]["RepairOfEscalators"]}')

if __name__ == '__main__':
    main()