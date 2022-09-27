import requests, json

def get_quotes(keyword, counter):
    url = f"https://favqs.com/api/quotes?page={counter}&filter={keyword}"
    response = requests.get(url, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    data = json.loads(response.text)
    if data['quotes'][0]['body'].lower() != 'no quotes found':
        for quote in data['quotes']:
            list_of_quotes.append(quote['body'] + " - " + quote['author'])
        return list_of_quotes
    else:
        return None

def print_results(list_of_quotes, keyword, counter):
    print(f"{len(list_of_quotes)} quotes associated with {keyword} - page {counter + 1}")
    print(list_of_quotes)

while True:
    counter = 0
    list_of_quotes = []

    keyword = input("Enter a keyword to search for quotes or 'I am done' to quit: ")
    if keyword.lower() != 'i am done':
        list_of_quotes = get_quotes(keyword, counter) 
        if list_of_quotes != None:   
            print_results(list_of_quotes, keyword, counter)
            counter += 1
        else:
            print("No result")
            continue
        while True:
            choice = input("Enter 'next page' or 'done': ")
            if choice.lower() == 'next page':
                list_of_quotes = get_quotes(keyword, counter)
                if list_of_quotes != None:
                    print_results(list_of_quotes, keyword, counter)
                    counter += 1
                else:
                    print("No more of these quotes")
                    break
            elif choice.lower() == 'done':
                break
    else:
        break
        
   