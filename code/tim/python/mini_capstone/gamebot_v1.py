import requests, json

''' 1) Example responses for top deals 
[
  {
    "internalName": "DEUSEXHUMANREVOLUTIONDIRECTORSCUT",
    "title": "Deus Ex: Human Revolution - Director's Cut",
    "metacriticLink": "/game/pc/deus-ex-human-revolution---directors-cut",
    "dealID": "HhzMJAgQYGZ%2B%2BFPpBG%2BRFcuUQZJO3KXvlnyYYGwGUfU%3D",
    "storeID": "1",
    "gameID": "102249",
    "salePrice": "2.99",
    "normalPrice": "19.99",
    "isOnSale": "1",
    "savings": "85.042521",
    "metacriticScore": "91",
    "steamRatingText": "Very Positive",
    "steamRatingPercent": "92",
    "steamRatingCount": "17993",
    "steamAppID": "238010",
    "releaseDate": 1382400000,
    "lastChange": 1621536418,
    "dealRating": "9.6",
    "thumb": "https://cdn.cloudflare.steamstatic.com/steam/apps/238010/capsule_sm_120.jpg?t=1619788192"
  },
   
Only useful HEADER for setting up multiple pages of results
{
    *   'x-total-page-count': '300',
    
'''

''' 1.1) Example response of selected game
{ 
    'internalName': 'TUMBLESTONE', 
    'title': 'Tumblestone', 
    'metacriticLink': '/game/pc/tumblestone', 
    'dealID': 'dJNCeHkZV3iaXZQFBSpYh3B2tz6ZuMvBaFpI6d1QYiU%3D', 
    'storeID': '1', 
    'gameID': '154838', 
    'salePrice': '2.49', 
    'normalPrice': '24.99', 
    'isOnSale': '1', 
    'savings': '90.036014', 
    'metacriticScore': '91', 
    'steamRatingText': 'Very Positive', 
    'steamRatingPercent': '88', 
    'steamRatingCount': '126', 
    'steamAppID': '269710', 
    'releaseDate': 1468281600, 
    'lastChange': 1662409231, 
    'dealRating': '10.0', 
    'thumb': 'https://cdn.cloudflare.steamstatic.com/steam/apps/269710/capsule_sm_120.jpg?t=1646164113'
    }
'''

''' 1.2) Example response of new url request on selected game

{
    'info': {
        'title': 'Tumblestone', 
        'steamAppID': '269710', 
        'thumb': 'https://cdn.cloudflare.steamstatic.com/steam/apps/269710/capsule_sm_120.jpg?t=1646164113'}, 
        'cheapestPriceEver': {'price': '2.49', 'date': 1640201740}, 
        'deals': [
            {'storeID': '1', 'dealID': 'dJNCeHkZV3iaXZQFBSpYh3B2tz6ZuMvBaFpI6d1QYiU%3D', 'price': '2.49', 'retailPrice': '24.99', 'savings': '90.036014'}, 
            {'storeID': '21', 'dealID': 'nDJpJR66SXSgVdWyeQYWrEEXcOiQKDjx4fn%2BiXtfbXk%3D', 'price': '24.99', 'retailPrice': '24.99', 'savings': '0.000000'}, 
            {'storeID': '11', 'dealID': 'vBcBR5HWelc%2BiepW0ceo1R9oJ%2B9wpjDbDU2s07JCbvk%3D', 'price': '24.99', 'retailPrice': '24.99', 'savings': '0.000000'}, 
            {'storeID': '3', 'dealID': 'VRCmFsaIviXjxxM0Ns0s1R8VWAkA7%2FUVACGrMZje5jU%3D', 'price': '24.99', 'retailPrice': '24.99', 'savings': '0.000000'}, 
            {'storeID': '30', 'dealID': 'uf1WXGkGc9YQpyJrlpvtyzxH0CaPqNhY%2FdWyFzqmUAw%3D', 'price': '24.99', 'retailPrice': '24.99', 'savings': '0.000000'}]
            }
'''

''' 2) Example response of game search result
{
    'gameID': '238507', 
    'steamAppID': '1828710', 
    'cheapest': '1.99', 
    'cheapestDealID': 'YjVBQFdCGHGlSvk2tOM71xGLHo0LU9JqusFDkhdnlJg%3D', 
    'external': 'Tumble', 
    'internalName': 'TUMBLE', 
    'thumb': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1828710/capsule_sm_120.jpg?t=1639612855'
    }
'''

def gamebot():
    counter = 1
    page = 1
    print(f"""  Steam Game Bot Menu
    1. Current best deals
    2. Search current sales
    3. Set a sale price alert for a game (WIP)
    4. Manage alerts (WIP)
    5. Exit
    """)
    main_menu = input("> ")

    while True:
        if main_menu == '5':
            print("Goodbye.")
            quit()

        # List 20 deals (****NEED TO ADD page support)
        if main_menu == '1':
            url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=5&pageSize=10&storeID=1"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            data = json.loads(response.text)
            # print(data)  
            print("Current Best Deals :\n")
            for game in data:
                print(f"{counter}. {game['title']}\nSale price {game['salePrice']} - Normal price {game['normalPrice']}")
                counter += 1

            # print(f"Page  of {response.headers['X-Total-Page-Count']}")   # add &pageNumber=2   to url
            selection = int(input("Which game do you want to see more information on? Or enter Next Page: ")) - 1
            
            

            # Runs a new request on the selected game using new variables
            game_url = f"https://www.cheapshark.com/api/1.0/games?id={data[selection]['gameID']}"
            payload={}
            headers = {}
            response = requests.request("GET", game_url, headers=headers, data=payload)
            game_data = json.loads(response.text)
            
            cheapest_ever = game_data['cheapestPriceEver']['price']
            if data[selection]['salePrice'] == game_data['cheapestPriceEver']['price']:
                cheapest_ever = f"{game_data['cheapestPriceEver']['price']} ** CURRENTLY THE CHEAPEST IT'S EVER BEEN **"
            else:
                cheapest_ever = cheapest_ever

            print(f"""\n{data[selection]['title']} - Metacritic Score - {data[selection]['metacriticScore']}%          
            Sale price ${data[selection]['salePrice']} - Normal price ${data[selection]['normalPrice']} - Savings {data[selection]['savings']}% 
            Deal Rating {data[selection]['dealRating']} - Cheapest Price Ever - ${cheapest_ever}
            
            Steam Rating - {data[selection]['steamRatingPercent']}% {data[selection]['steamRatingText']} with {data[selection]['steamRatingCount']} reviews
            Link to sale - https://www.cheapshark.com/redirect?dealID={data[selection]['dealID']}
            """)
            
            gamebot()

        # Search for a game and list results - Can then get the game ID to go directly to that page like above
        if main_menu == '2':
            game_title = input("Enter a game to search for: ")
            # url = f"https://www.cheapshark.com/api/1.0/games?title={game_title}&limit=10&exact=0"
            url = f"https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=5&pageSize=10&storeID=1&title={game_title}"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            data = json.loads(response.text)
            # print(data)     

            print("Results sorted by Deal Rating:\n")
            for game in data:
                print(f"{counter}. {game['title']}\nSale price {game['salePrice']} - Normal price {game['normalPrice']}")
                counter += 1
          
            selection = int(input("Which game do you want to see more information on?: ")) - 1
            # Runs a new request on the selected game using new variables
            game_url = f"https://www.cheapshark.com/api/1.0/games?id={data[selection]['gameID']}"
            payload={}
            headers = {}
            response = requests.request("GET", game_url, headers=headers, data=payload)
            game_data = json.loads(response.text)
            
            cheapest_ever = game_data['cheapestPriceEver']['price']
            if data[selection]['salePrice'] == game_data['cheapestPriceEver']['price']:
                cheapest_ever = f"{game_data['cheapestPriceEver']['price']} ** CURRENTLY THE CHEAPEST IT'S EVER BEEN **"
            else:
                cheapest_ever = cheapest_ever

            print(f"""\n{data[selection]['title']} - Metacritic Score - {data[selection]['metacriticScore']}%          
            Sale price ${data[selection]['salePrice']} - Normal price ${data[selection]['normalPrice']} - Savings {data[selection]['savings']}% 
            Deal Rating {data[selection]['dealRating']} - Cheapest Price Ever - ${cheapest_ever}
            
            Steam Rating - {data[selection]['steamRatingPercent']}% {data[selection]['steamRatingText']} with {data[selection]['steamRatingCount']} reviews
            Link to sale - https://www.cheapshark.com/redirect?dealID={data[selection]['dealID']}
            """)
            
            gamebot()

        if main_menu == '3':
            print("main menu 3")
            break
        if main_menu == '4':
            print("main menu 4")
            break
        else:
            print("You hit main menu else condition.")
            break
gamebot()