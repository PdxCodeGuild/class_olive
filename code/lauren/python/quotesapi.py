from turtle import done
import requests, json
page = 1

def get_quote(user_input):
    url = f'https://favqs.com/api/quotes?page={page}&filter={user_input}'

    response = requests.get(url, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

    info = json.loads(response.text)

    # print(info['quote']['body'])
    # print(info['quote']['author'])

    quote_list = info['quotes']
    # print(quote_list[0]['body'])
    print(info['page'], len(quote_list))
    for index in range(len(quote_list)):
        print(quote_list[index]['body'],'\n')

again = '' 

while True:
    user_input = input('enter a keyword: ')
    get_quote(user_input)  
    
    while again != "done":
        again = input('Enter next page or done: ')
        page += 1
        get_quote(user_input) 
        break
        
    if user_input == 'done':
        break