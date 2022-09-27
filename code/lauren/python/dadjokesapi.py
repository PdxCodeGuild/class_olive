import requests, json

response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

data = json.loads(response.text)

print(data['joke'])