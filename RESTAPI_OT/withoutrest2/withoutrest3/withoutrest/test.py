import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'
def get_resource():
    resp=requests.get(BASE_URL+END_POINT+id+'/')
    print(resp.status_code)
    print(resp.json())

get_resource()
