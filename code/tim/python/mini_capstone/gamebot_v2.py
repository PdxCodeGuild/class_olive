import requests, json
from pprint import pprint

selected_games = []

# Lists top Steam sales
def top_deals():
    page = 0
    while True:
        counter = 1
        payload={}
        headers = {}
        deals_url = f"https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=5&pageSize=10&pageNumber={page}"
        deals_response = requests.request("GET", deals_url, headers=headers, data=payload)
        deals_data = json.loads(deals_response.text)
        print("Current Best Deals on Steam:\n")

        for game in deals_data:
            print(f"{counter}. {game['title']}\nSale price {game['salePrice']} - Normal price {game['normalPrice']}")
            counter += 1
        
        print(f"\nPage {page+1} of {deals_response.headers['x-total-page-count']}")
        selection = input("Which game do you want to see more information on? Or use + and - to change pages: ")
        if selection == '+':
            page += 1
        elif page == 0 and selection == '-':
            page == 0
        elif selection == '-':
            page -= 1
        else:         
            break
    
    selected_game = deals_data[int(selection)-1]
    view_game(selected_game)

# View selected game, does 2 get requests because they can't have all the useful info in just one now can they?    
def view_game(selected_game):
    selected_games.append(selected_game)
    payload={}
    headers = {}
    gameid_url = f"https://www.cheapshark.com/api/1.0/games?id={selected_game['gameID']}" 
    dealid_url = f"https://www.cheapshark.com/api/1.0/deals?id={selected_game['dealID']}" 
    gameid_response = requests.request("GET", gameid_url, headers=headers, data=payload)
    dealid_response = requests.request("GET", dealid_url, headers=headers, data=payload)
    gameid_data = json.loads(gameid_response.text)
    dealid_data = json.loads(dealid_response.text)
    
    # Checks if the current price is the cheapest it has ever been, adds a note if so
    cheapest_ever = gameid_data['cheapestPriceEver']['price']
    if dealid_data['gameInfo']['salePrice'] == gameid_data['cheapestPriceEver']['price']:
        cheapest_ever = f"{gameid_data['cheapestPriceEver']['price']} ** CURRENTLY THE CHEAPEST IT'S EVER BEEN **"
    else:
        cheapest_ever = cheapest_ever

    print(f"""\n{gameid_data['info']['title']} - Metacritic Score - {dealid_data['gameInfo']['metacriticScore']}%          
    Sale price ${dealid_data['gameInfo']['salePrice']} - Normal price ${dealid_data['gameInfo']['retailPrice']} - Savings {gameid_data['deals'][0]['savings']}% 
    Cheapest Price Ever - ${cheapest_ever}

    Steam Rating - {dealid_data['gameInfo']['steamRatingPercent']}% {dealid_data['gameInfo']['steamRatingText']} with {dealid_data['gameInfo']['steamRatingCount']} reviews
    Link to sale - https://www.cheapshark.com/redirect?dealID={gameid_data['deals'][0]['dealID']}
    """)

# Search current Steam sales
def search_deals():
    page = 0
    game_search = input("Enter a game to search for: ")
    while True:
        counter = 1
        payload={}
        headers = {}
        search_url = f"https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=5&pageSize=10&title={game_search}&pageNumber={page}"
        search_response = requests.request("GET", search_url, headers=headers, data=payload)
        search_data = json.loads(search_response.text)
        print("Results sorted by Deal Rating:\n")
        
        for game in search_data:
            print(f"{counter}. {game['title']}\nSale price {game['salePrice']} - Normal price {game['normalPrice']}")
            counter += 1
        
        print(f"\nPage {page+1} of {search_response.headers['x-total-page-count']}")
        search_selection = input("Which game do you want to see more information on? Or use + and - to change pages: ")
        if search_selection == '+':
            page += 1
        elif page == 0 and search_selection == '-':
            page == 0
        elif search_selection == '-':
            page -= 1
        else:         
            break
        
    selected_game = search_data[int(search_selection)-1]
    view_game(selected_game)

def set_alert():
    print("Not yet")

def view_alerts():
    print("Not yet")

def gamebot():
    
    while True:
        choice = input("""Steam Game Bot Menu
        1. Current best deals
        2. Search current sales
        3. Set a sale price alert for a game (WIP)
        4. Manage alerts (WIP)
        5. Exit
        Choice: """)
        
        if choice == '1':
            top_deals()
        if choice == '2':
            search_deals()
        if choice == '3':
            set_alert()
        if choice == '4':
            view_alerts()
        if choice == '5':
            exit()
            

gamebot()

'''
deals_data  
[  
{'dealID': 'dJNCeHkZV3iaXZQFBSpYh3B2tz6ZuMvBaFpI6d1QYiU%3D',
  'dealRating': '10.0',
  'gameID': '154838',
  'internalName': 'TUMBLESTONE',
  'isOnSale': '1',
  'lastChange': 1662409231,
  'metacriticLink': '/game/pc/tumblestone',
  'metacriticScore': '91',
  'normalPrice': '24.99',
  'releaseDate': 1468281600,
  'salePrice': '2.49',
  'savings': '90.036014',
  'steamAppID': '269710',
  'steamRatingCount': '126',
  'steamRatingPercent': '88',
  'steamRatingText': 'Very Positive',
  'storeID': '1',
  'thumb': 'https://cdn.cloudflare.steamstatic.com/steam/apps/269710/capsule_sm_120.jpg?t=1646164113',
  'title': 'Tumblestone'},
]

gameid_data 
{  
 'cheapestPriceEver': {'date': 1640201740, 'price': '2.49'},
 'deals': [{'dealID': 'dJNCeHkZV3iaXZQFBSpYh3B2tz6ZuMvBaFpI6d1QYiU%3D',
            'price': '2.49',
            'retailPrice': '24.99',
            'savings': '90.036014',
            'storeID': '1'},
           {'dealID': 'nDJpJR66SXSgVdWyeQYWrEEXcOiQKDjx4fn%2BiXtfbXk%3D',
            'price': '24.99',
            'retailPrice': '24.99',
            'savings': '0.000000',
            'storeID': '21'},
           {'dealID': 'vBcBR5HWelc%2BiepW0ceo1R9oJ%2B9wpjDbDU2s07JCbvk%3D',
            'price': '24.99',
            'retailPrice': '24.99',
            'savings': '0.000000',
            'storeID': '11'},
           {'dealID': 'VRCmFsaIviXjxxM0Ns0s1R8VWAkA7%2FUVACGrMZje5jU%3D',
            'price': '24.99',
            'retailPrice': '24.99',
            'savings': '0.000000',
            'storeID': '3'},
           {'dealID': 'uf1WXGkGc9YQpyJrlpvtyzxH0CaPqNhY%2FdWyFzqmUAw%3D',
            'price': '24.99',
            'retailPrice': '24.99',
            'savings': '0.000000',
            'storeID': '30'}],
 'info': {'steamAppID': '269710',
          'thumb': 'https://cdn.cloudflare.steamstatic.com/steam/apps/269710/capsule_sm_120.jpg?t=1646164113',
          'title': 'Tumblestone'}}


dealid_data
{
 'cheaperStores': [],
 'cheapestPrice': {'date': 0},
 'gameInfo': {'gameID': '154838',
              'metacriticLink': '/game/pc/tumblestone',
              'metacriticScore': '91',
              'name': 'Tumblestone',
              'publisher': 'N/A',
              'releaseDate': 1468281600,
              'retailPrice': '24.99',
              'salePrice': '2.49',
              'steamAppID': '269710',
              'steamRatingCount': '126',
              'steamRatingPercent': '88',
              'steamRatingText': 'Very Positive',
              'steamworks': '1',
              'storeID': '1',
              'thumb': 'https://cdn.cloudflare.steamstatic.com/steam/apps/269710/capsule_sm_120.jpg?t=1646164113'}}

search_data
[
{
  'dealID': 'dJNCeHkZV3iaXZQFBSpYh3B2tz6ZuMvBaFpI6d1QYiU%3D',
  'dealRating': '10.0',
  'gameID': '154838',
  'internalName': 'TUMBLESTONE',
  'isOnSale': '1',
  'lastChange': 1662409231,
  'metacriticLink': '/game/pc/tumblestone',
  'metacriticScore': '91',
  'normalPrice': '24.99',
  'releaseDate': 1468281600,
  'salePrice': '2.49',
  'savings': '90.036014',
  'steamAppID': '269710',
  'steamRatingCount': '126',
  'steamRatingPercent': '88',
  'steamRatingText': 'Very Positive',
  'storeID': '1',
  'thumb': 'https://cdn.cloudflare.steamstatic.com/steam/apps/269710/capsule_sm_120.jpg?t=1646164113',
  'title': 'Tumblestone'}
]
'''