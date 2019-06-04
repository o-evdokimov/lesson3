#!/usr/local/bin/python3

# Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, 
# вывести улицу, на которой больше всего остановок.

# Output:
#
# method-1: max_zip: 
#  max_stops = (468, 'проезд без названия')
# method-2: collections_Counter: 
#  max_stops = [('проезд без названия', 468)] 

import json
from collections import Counter

def main():
    with open('data-398-2019-05-28.json','r', encoding = 'cp1251') as transport:
        data = json.loads(transport.read())

    print(data[0])
    streets = [ item['Street'] for item in data ]

    dict = {}   
    for street in streets:
        if street in dict:
            dict[street] += 1
        else:
             dict[street] = 1   

    # method #1
    
    max_stops = max(zip(dict.values(), dict.keys()))
    print(f'\nmethod-1: max_zip: \n max_stops = {max_stops}')
    
    # method #2
    dict_counter = Counter(dict)
    max_stops = dict_counter.most_common(1)
    print(f'method-2: collections_Counter: \n max_stops = {max_stops}\n')

if __name__ == '__main__':
    main()