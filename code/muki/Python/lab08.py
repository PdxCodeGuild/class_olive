# Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.

# Part 1
# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the Accept header as application/json. This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.

# response = requests.get("https://icanhazdadjoke.com", headers={
#     'Accept': 'application/json'
# })
# Part 2
# Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time.

# response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
#     'Accept': 'application/json'
# })


import requests
dadjokes = "https://icanhazdadjoke.com/"
response = requests.get(dadjokes)
response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})

# print(dadjokes)
# print(response)
# print(response.json())

dad_joke_dic = response.json()
joke = dad_joke_dic['joke']

print(f'\n{joke}\n-pulled from icanhazdadjoke.com')

search_word = input("What kind of dad joke would you like?\t>")
response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_word}", headers={
    'Accept': 'application/json'
})

dad_joke_sjson = response.json()
result = dad_joke_sjson['results']
# print(result)
# joke2 = dad_joke_searched['joke']
# print(joke2)
for value in result:
    print(value['joke'])
    print('\n')