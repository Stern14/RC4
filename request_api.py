import requests

local_host = ''
URL = f'{local_host}/robots/api'

robots = []

for robot in robots:
    response = requests.post(URL, json=robot)
    print(response.text)
