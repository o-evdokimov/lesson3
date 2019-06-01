#!/usr/local/bin/python3

import json

def main():
    with open('data-398-2019-05-28.json','r', encoding = 'cp1251') as transport:
        data = json.loads(transport.read())

    for item in data:
        print(item["Street"])

if __name__ == '__main__':
    main()