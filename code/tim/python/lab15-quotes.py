# Lab 15/18 Quotes API

import requests, json

url = 'https://favqs.com/api/qotd/'
response = requests.get(url)    # Already json, don't need to add headers to original URL
# print(response)   # <Response [200]>
data = json.loads(response.text)
# print(data)

'''
example data response
{
    'qotd_date': '2022-09-02T00:00:00.000+00:00', 
    'quote': {
        'id': 40574, 
        'dialogue': False, 
        'private': False, 
        'tags': ['men', 'money'], 
        'url': 'https://favqs.com/quotes/sophocles/40574-money-is-the--', 
        'favorites_count': 0, 
        'upvotes_count': 1, 
        'downvotes_count': 0, 
        'author': 'Sophocles', 
        'author_permalink': 'sophocles', 
        'body': 'Money is the worst currency that ever grew among mankind. This sacks cities, this drives men from their homes, this teaches and corrupts the worthiest minds to turn base deeds.'
    }
}
'''
print(f"Your random QOTD is - \n\n{data['quote']['body']}\n     - {data['quote']['author']}")   # Prints