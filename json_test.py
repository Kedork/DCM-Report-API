import json
from pprint import pprint

with open('IDs.json') as data_file:
    data = json.load(data_file)

#pprint(data['data']['Hyundai'])

#data['data']['Hyundai']['Token'] = '987654321'

#pprint(data['data']['Hyundai'])

for alldata in data['data']:
    profile_id = data['data'][alldata]['Profile']
    for Reports in data['data'][alldata]['Reports']:
        report_id = data['data'][alldata]['Reports'][Reports]
        #profile_id = account["Profile"]
        #print profile_id

#f = open('IDs.json', 'w')
#json.dump(data,f)
#f.close()
