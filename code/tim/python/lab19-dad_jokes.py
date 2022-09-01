# Lab 19 (or is it 10?) Dad Jokes

import requests, json, time

# url = 'https://icanhazdadjoke.com/'
# response = requests.get(url, headers={'Accept': 'application/json'})
# # print(response)
# data = json.loads(response.text)
# print(f"Your random Dad Joke is - \n\n{data['joke']}\n")


# Version 2 
search_term = input('What would you like to search for? ')
url = 'https://icanhazdadjoke.com/search?term=' + search_term

page = 1
payload = {'page': page}
response = requests.get(url, headers={'Accept': 'application/json'}, params=payload)

# print(response)
# print(url)

data = json.loads(response.text)
# print(data)

print(f"There are {data['total_jokes']} results for '{search_term}'\n")

'''   
Example data variable from 'man' search_term
{
    'current_page': 1, 
    'limit': 20, 
    'next_page': 2, 
    'previous_page': 1, 
    'results': [
        {'id': 'V0orcFdFIBd', 'joke': 'What do you do when you see a space man?\r\nPark your car, man.'}, 
        {'id': '9xPCt411ojb', 'joke': 'What did one snowman say to the other snow man? Do you smell carrot?'}, 
        {'id': 'ap4orcpGtrc', 'joke': 'A man walks into a bar and orders helicopter flavor chips. The barman replies “sorry mate we only do plain”'} ...... <then a whole lot more jokes here> ], 
    'search_term': 'man', 
    'status': 200, 
    'total_jokes': 44, 
    'total_pages': 3
}
'''

counter = 1
for joke in data['results']:
    print(f"{counter}:  {joke['joke']}\n")
    counter += 1
    # time.sleep(5)
    if counter > data['limit'] and data['total_pages'] > 1:
        # print('test')
        next_page = input('Go to page Next Page? Y/N: ').upper()
        if next_page == 'Y':
            # print('test pass')
            page += 1
            print(page)
            # response = requests.get(url, headers={'Accept': 'application/json'}, params=payload)   # This should probably be a function so it can just be called again rather than trying to go back to start of loop
        else:
            print('test fail')



# print(f"""
# Current page {data['current_page']}  
# Next page - {data['next_page']} 
# Total pages - {data['current_page']}  """)