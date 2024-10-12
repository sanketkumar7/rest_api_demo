import requests
import json
BASE_URL='http://127.0.0.1:8000'
ENDPOINT='/items/'

def get_resource(id=None):
    response=requests.get(BASE_URL+ENDPOINT+f'{id}')
    print(response.status_code)
    print(response.json())

# get_resource(5)

def post_resource():
    data={  
        'item_id':5,
        'name':'lemon',
        'discription':'yellowish'
        }
    headers={'Content-Type': 'application/json'}
    json_data=json.dumps(data)
    response=requests.post(BASE_URL+ENDPOINT,data=json_data,headers=headers)
    print(response.status_code)
    print(response.json())
# post_resource()

def put_resource(id):
    data={
        'item_id':id,
        'name':'lemon',
        'discription':'green'
    }
    headers={'Content-Type': 'application/json'}
    json_data=json.dumps(data)
    response=requests.put(BASE_URL+ENDPOINT+f'{id}',data=json_data,headers=headers)
    print(response.status_code)
    print(response.json())

# put_resource(5)

def delete_resources(id):
    response=requests.delete(BASE_URL+ENDPOINT+f'{id}')
    print(response.status_code)
    print(response.json())
# delete_resources(3)
    