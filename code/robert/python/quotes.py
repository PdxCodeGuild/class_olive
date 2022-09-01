import json, requests

url = "https://favqs.com/api/qotd"

response = requests.get(url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

print(response)
    #200!!!!!

data = json.loads(response.text)

    #print(type(data['results']))

print(f"Random Quote of the Day!\n{data['quote']['body']}")

search = input(f"Type in a keyword to search for quotes: ")

page_number = 1

false_check = True

while false_check == True:

    url_search = f"https://favqs.com/api/quotes/?page={page_number}&filter={search}"
    data_search = json.loads(requests.get(url_search, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}).text)
    print(data_search)
    
    for keys in range(len(data_search['quotes'])):
        print(f"{data_search['quotes'][keys]['body']}")

    if len(data_search['quotes'][keys]['body']) < 25:
        lastpage = 'and this is the last page'
    else:
        lastpage = 'and there are more pages'

    print(f"There are {len(data_search['quotes'])} quotes that match {search} on page {page_number} {lastpage}")
    next_page = input("Type yes if you would like to go to the next page or anything else to search again/exit: ").lower()

    if next_page == 'yes':
        page_number += 1
    else:
        new_search = input("Type yes if you would like to search something else or done if finished: ").lower()

        if new_search == 'yes':
            search = input(f"Type in a keyword to search for quotes: ")
            page_number = 1
        else:
           false_check = False
        
