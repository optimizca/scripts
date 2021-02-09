import requests
import base64
import json
import csv
from datetime import datetime
import math
import time

try:
    # Gets data from config.json
    with open('config.json') as json_file:
        data = json.load(json_file)['config']
        baseurl = data[0]['url']
        user = data[0]['user']
        password = data[0]['password']
        account = data[0]['account']
        application_id = data[0]['application_id']
        start_time = data[0]['start_time']
        end_time = data[0]['end_time']
        
except Exception as e:
    print(e)
    
start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
start = int(time.mktime(start_time.utctimetuple()) * 1000 + start_time.microsecond / 1000)

end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
end = int(time.mktime(end_time.utctimetuple()) * 1000 + end_time.microsecond / 1000)

url = baseurl + "/controller/rest/applications/" + str(application_id) + \
                "/problems/healthrule-violations" + \
                "?time-range-type=BETWEEN_TIMES&start-time=" + str(start)  + \
                "&end-time=" + str(end) + \
                "&output=JSON"

# Encodes the auth in base64
auth = user + "@" + account + ":" + password
auth_encode= base64.b64encode(memoryview(bytes(auth, 'utf8')))
fixed_auth = str(auth_encode).replace('b', '', 1).replace("'", '')

headers = {
    "Authorization": "Basic " + fixed_auth
}
r = requests.get(url, headers=headers)

if r.status_code == 200:
    jsons = r.json()
    with open('output.csv', mode='w') as events:
        events_writer = csv.writer(events, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        events_writer.writerow(['affectedEntityId', 
                                'affectedEntityType', 
                                'affectedEntityName', 
                                'deepLinkUrl',
                                'description', 
                                'detectedTimeInMillis', 
                                'endTimeInMillis', 
                                'id', 
                                'incidentStatus',
                                'name', 
                                'severity', 
                                'startTimeInMillis', 
                                'name', 
                                'triggeredEntitiyId',
                                'triggeredEntityType',
                                'triggeredEntityName'
                                ])

        for i in jsons:
            #print(json.dumps(i, indent=4, sort_keys=True))

            events_writer.writerow([i['affectedEntityDefinition']['entityId'], 
                                        i['affectedEntityDefinition']['entityType'],
                                        i['affectedEntityDefinition']['name'], 
                                        i['deepLinkUrl'], 
                                        i['description'], 
                                        i['detectedTimeInMillis'], 
                                        i['endTimeInMillis'], 
                                        i['id'], 
                                        i['incidentStatus'], 
                                        i['name'], 
                                        i['severity'], 
                                        i['startTimeInMillis'], 
                                        i['name'], 
                                        i['triggeredEntityDefinition']['entityId'],
                                        i['triggeredEntityDefinition']['entityType'],
                                        i['triggeredEntityDefinition']['name']
                                        ])
                
else:
    print("Status code: " + str(r.status_code))
        
