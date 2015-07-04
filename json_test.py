import json
from pprint import pprint

with open('IDs.json') as data_file:
    data = json.load(data_file)

pprint(data['data']['Hyundai'])

data['data']['Hyundai']['Token'] = '987654321'

pprint(data['data']['Hyundai'])

f = open('IDs.json', 'w')
json.dump(data,f)
f.close()
