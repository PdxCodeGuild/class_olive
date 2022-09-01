import json, requests

while True:
    search = input("Type a search term: ")
    url_page = []
    url = "https://icanhazdadjoke.com/search?term="
    url_search = f"{url}{search}{url_page}"

    response = requests.get(url_search, headers = {'Accept': "application/json"})

    print(response)
    #200!!!!!

    data = json.loads(response.text)

    #print(type(data['results']))

    print(f"There are {data['total_jokes']} jokes with that keyword and {data['total_pages']} pages")

    for items in data['results']:

        pages = range(0,int(data['total_pages']))
        total_jokes = range(0,int(data['total_jokes']))
        jokenumber = int(input(f"Select a random number for your joke (1 - {data['total_jokes']}) or any letter for a new search: "))
        if jokenumber >-1 and jokenumber < 20:
            print(data['results'][jokenumber-1]['joke'])
        elif jokenumber > 19 and jokenumber < 30:
            url_page = f"&page=2"
            url_search = f"{url}{search}{url_page}"
            response = requests.get(url_search, headers = {'Accept': "application/json"})
            data = json.loads(response.text)
            print(data['results'][jokenumber-21]['joke'])
        elif jokenumber > 29 and jokenumber < 40:
            url_page = f"&page=2"
            url_search = f"{url}{search}{url_page}"
            response = requests.get(url_search, headers = {'Accept': "application/json"})
            data = json.loads(response.text)
            print(data['results'][jokenumber-31]['joke'])
        elif jokenumber > 39 and jokenumber < 50:
            url_page = f"&page=3"
            url_search = f"{url}{search}{url_page}"
            response = requests.get(url_search, headers = {'Accept': "application/json"})
            data = json.loads(response.text)
            print(data['results'][jokenumber-41]['joke'])
        elif jokenumber > 49 and jokenumber < 60:
            url_page = f"&page=3"
            url_search = f"{url}{search}{url_page}"
            response = requests.get(url_search, headers = {'Accept': "application/json"})
            data = json.loads(response.text)
            print(data['results'][jokenumber-51]['joke'])
        elif jokenumber > 59 and jokenumber < 70:
            url_page = f"&page=4"
            url_search = f"{url}{search}{url_page}"
            response = requests.get(url_search, headers = {'Accept': "application/json"})
            data = json.loads(response.text)
            print(data['results'][jokenumber-61]['joke'])
        else:
            print(f"Let's try that again with a different search parameter")

