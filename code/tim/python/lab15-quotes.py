# Lab 15/18 Quotes API
import requests, json

# Version 1

# url = 'https://favqs.com/api/qotd/'
# response = requests.get(url)    # Already json, don't need to add headers to original URL
# print(response)   # <Response [200]>
# data = json.loads(response.text)
# print(data)
# print(f"Your random QOTD is - \n\n{data['quote']['body']}\n     - {data['quote']['author']}")   # Prints

''' Data response with one page
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

# Version 2 

''' Data response with multiple pages
{
    'page': 1, 
    'last_page': False, 
    'quotes': [
        {
        'id': 859, 
        'dialogue': False, 
        'private': False, 
        'tags': ['age', 'strength'], 
        'url': 'https://favqs.com/quotes/erma-bombeck/859-youngsters-of-t-', 
        'favorites_count': 0, 
        'upvotes_count': 0, 
        'downvotes_count': 0, 
        'author': 'Erma Bombeck', 
        'author_permalink': 'erma-bombeck', 
        'body': 'Youngsters of the age of two and three are endowed with extraordinary strength. They can lift a dog twice their own weight and dump him into the bathtub.'
        },
        {next jokes....
'''

def qotd():
    
    page = 1
    print("\nWelcome to QOTD search\n")
    keyword = input("Enter a keyword to search quotes for, or type 'exit' to quit: ").lower()
    
    # Easy to loop back to current page of results with this loop
    while True:
        
        if keyword == 'exit':
            
            print("Goodbye.")
            quit()
        
        else:
            
            url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
            response = requests.get(url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            data = json.loads(response.text)
            quotes_per_page = len(data['quotes'])
            quote_count = 1
            last_page = data['last_page']

            for quote in data['quotes']:
                    
                    if quote['body'] == 'No quotes found':
                        print(f"No results found for {keyword}.  Restarting.")
                        qotd()
                    else:
                        print(f"{quote_count}. {quote['body']}\n   - {quote['author']}")
                        quote_count += 1
            
            if last_page == True:
                print(f"{quotes_per_page} results total on last page.")               
                page_or_quit = input("Type 'restart'  or  'exit': ").lower()
            else:
                print(f"{quotes_per_page} results on page {data['page']}....")
                page_or_quit = input("Type 'next page'  'restart'  or  'exit': ").lower()
            if page_or_quit == 'exit':
                print("Goodbye.")
                quit()
            elif page_or_quit == 'next page':
                    page += 1
            elif page_or_quit == 'restart':
                qotd()
            else:
                print("PEBKAC")
                
qotd()