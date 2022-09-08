import requests, json

selected_games = []

# Lists top Steam sales
def top_deals():
    counter = 1
    page = 1
    sale_url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=5&pageSize=10&storeID=1"
    payload={}
    headers = {}
    response = requests.request("GET", sale_url, headers=headers, data=payload)
    data = json.loads(response.text)
    
    print("Current Best Deals on Steam:\n")
    for game in data:
        print(f"{counter}. {game['title']}\nSale price {game['salePrice']} - Normal price {game['normalPrice']}")
        counter += 1
    selection = int(input("Which game do you want to see more information on? Or enter Next Page: ")) - 1
    selected_game = data[selection]
    view_game(selected_game)

# View selected game, does 2 get requests because they can't have all the useful info in just one now can they?    
def view_game(selected_game):
    selected_games.append(selected_game)
    gameid_url = f"https://www.cheapshark.com/api/1.0/games?id={selected_game['gameID']}" 
    dealid_url = f"https://www.cheapshark.com/api/1.0/deals?id={selected_game['dealID']}" 
    payload={}
    headers = {}
    gameid_response = requests.request("GET", gameid_url, headers=headers, data=payload)
    gameid_data = json.loads(gameid_response.text)
    dealid_response = requests.request("GET", dealid_url, headers=headers, data=payload)
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
    counter = 1
    game_search = input("Enter a game to search for: ")
    # search_url = f"https://www.cheapshark.com/api/1.0/games?title={game_search}&limit=10&exact=0" # Think this is full game search / not just sales - Add later?
    search_url = f"https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=5&pageSize=10&storeID=1&title={game_search}"
    payload={}
    headers = {}
    response = requests.request("GET", search_url, headers=headers, data=payload)
    data = json.loads(response.text)
    
    print("Results sorted by Deal Rating:\n")
    for game in data:
        print(f"{counter}. {game['title']}\nSale price {game['salePrice']} - Normal price {game['normalPrice']}")
        counter += 1
    selection = int(input("Which game do you want to see more information on? Or enter Next Page: ")) - 1
    selected_game = data[selection]
    view_game(selected_game)

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
            pass
        if choice == '4':
            pass
        if choice == '5':
            exit()
            

gamebot()