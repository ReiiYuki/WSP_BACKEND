import requests

API = 'https://api.aftership.com/v4/'
API_KEY = '9442c41d-f380-482e-954c-2a1c996f1815'
COURIER = 'thailand-post/'
TRACKING = 'trackings/'
LAST_CHECKPOINT = 'last_checkpoint/'
HEADERS = { 'Content-Type' : 'application/json' , 'aftership-api-key' : API_KEY}

''' ADD Tracking to Aftership '''
def add_tracking(tracking_num) :
    path = API+TRACKING
    body = { 'tracking': { 'tracking_number' : tracking_num } }
    r = requests.post(path,json=body,headers=HEADERS)
    return r.json()['data']['tracking']

''' DELETE Tracking from Aftership '''
def delete_tracking(tracking_num) :
    path = API+TRACKING+COURIER+tracking_num
    r = requests.delete(path,headers=HEADERS)
    return r.json()['data']['tracking']

''' CHECK tracking LAST_CHECKPOINT from Aftership '''
def check_tracking(tracking_num) :
    path = API+TRACKING+COURIER+tracking_num
    r = requests.get(path,headers=HEADERS)
    return r.json()['data']
