'''
This program will work with an API to grab dad jokes.
'''


import time , requests, json

url = 'https://icanhazdadjoke.com/search'



response = requests.get(url, headers={'Accept': 'application/json'})
data = json.loads(response.text)
print(data, type(data))
