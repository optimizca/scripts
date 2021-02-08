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
        summary = data[0]['summary']
        event_types = data[0]['event_types']
        severities = data[0]['severities']
        start_time = data[0]['start_time']
        end_time = data[0]['end_time']
    # uncomment to re-add python 3 .timestamp
    #start = math.trunc(datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
    #end = math.trunc(datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S').timestamp() * 1000) 


    # For python 2
    start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    start = int(time.mktime(start_time.utctimetuple()) * 1000 + start_time.microsecond / 1000)

    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    end = int(time.mktime(end_time.utctimetuple()) * 1000 + end_time.microsecond / 1000)


    url = baseurl + "/controller/rest/applications/" + str(application_id) + "/events?summary=" + summary + \
                    "&event-types=" + event_types + \
                    "&severities=" + severities + \
                    "&time-range-type=BETWEEN_TIMES&start-time=" + str(start) + \
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
        with open('output '+ str(datetime.now()).replace(':', '-') +'.csv', mode='w') as events:
            events_writer = csv.writer(events, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            events_writer.writerow(['archived', 
                                    'deepLinkUrl', 
                                    'eventTime', 
                                    'id',
                                    'markedAsRead', 
                                    'markedAsResolved', 
                                    'severity', 
                                    'subType', 
                                    'summary',
                                    'triggeredEntity', 
                                    'type', 
                                    'entityType', 
                                    'name', 
                                    'entitiyId'])
            for i in jsons:
                # Pretty print each result
                #print(json.dumps(i, indent=4, sort_keys=True))
                for j in i['affectedEntities']:
                    events_writer.writerow([i['archived'], 
                                            i['deepLinkUrl'],
                                            i['eventTime'], 
                                            i['id'], 
                                            i['markedAsRead'], 
                                            i['markedAsResolved'], 
                                            i['severity'], 
                                            i['subType'], 
                                            i['summary'], 
                                            i['triggeredEntity'], 
                                            i['type'], 
                                            j['entityType'], 
                                            j['name'], 
                                            j['entityId']])
    else:
        print("Status code: " + r.status_code)
            
except Exception as e:
    print(e)