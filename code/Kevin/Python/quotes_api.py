'''
This program will interact with an API to grab quotes. 
CURRENTLY MESSY. REPL starts on line 43.
'''

import requests, json, time, random

page = 1
keyword = 'time'

url_random = 'https://favqs.com/api/qotd/'
url_keyword = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'

api_response_random = requests.get(url_random)
# print(api_response_random)
api_data_random = json.loads(api_response_random.text)
# print(api_data_random)

# print(f'''
# "{api_data['quote']['body']}"
#     - {api_data['quote']['author']}''')

api_response_keyword = requests.get(url_keyword, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
# print(api_response_keyword)
api_data_keyword = json.loads(api_response_keyword.text)
# print(api_data_keyword)
# print(len(api_data_keyword['quotes']), api_data_keyword['quotes'][0]['body'])

#Keyword finder.
# print(api_data_random['quote']['tags'])

keyword_choices = ['time','architecture','nature','relationship','profession','skill','musician']


def stay_or_go():
    user_input = input('Return to start? Or go back to your page?\n1. Start\n2. Return to page\n>: ')
    if user_input == '1':
        return True
    elif user_input == '2':
        return False


while True:
    user_input_prompt = input(f'''
    Welcome! This program will fetch quotes from "favqs.com" for you.
    What would you like to do?
    1. Get a random quote.
    2. Get a quote based on a keyword.
    3. Exit.

    >: ''')

    if user_input_prompt == '1':
        print(f'''
        "{api_data_random['quote']['body']}"
            - {api_data_random['quote']['author']}''')
        time.sleep(3)

    elif user_input_prompt == '2':
        user_input_keyword = input(f'''
    Enter a keyword.
    For example: {random.choice(keyword_choices)}.
    >: ''')

        while True:
            url_keyword = f'https://favqs.com/api/quotes?page={page}&filter={user_input_keyword}'
            api_response_keyword = requests.get(url_keyword, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            # print(api_response_keyword)
            api_data_keyword = json.loads(api_response_keyword.text)
            user_index_input = input(f'''
    There are {len(api_data_keyword['quotes'])} quotes on page {api_data_keyword['page']}.
    Which quote would you like to see?
    Enter a number 1 - {len(api_data_keyword['quotes'])}, or type "page" for next page.
    >: ''')
            if user_index_input == 'page':
                page += 1
                continue
            user_index_input = int(user_index_input)
            print(f'''{api_data_keyword['quotes'][user_index_input]['body']}
            {api_data_keyword['quotes'][user_index_input]['author']}''')
            time.sleep(3)
            if stay_or_go == False:
                break
        if user_input_prompt == '3':
            break
    
        
