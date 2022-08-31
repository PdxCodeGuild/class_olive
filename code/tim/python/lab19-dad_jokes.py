# Lab 19 (or is it 10?) Dad Jokes

import requests, json

url = 'https://icanhazdadjoke.com/'
response = requests.get(url, headers={'Accept': 'application/json'})
# response.headers['accept': 'application/json']
# headers = {'Accept': 'application/json'}

# print(response)

data = json.loads(response.text)
print(f"Your random Dad Joke is - \n\n{data['joke']}\n")