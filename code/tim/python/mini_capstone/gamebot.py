import requests, json

# Gives top deals 10 per page
# url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=5&pageSize=10"
# payload={}
# headers = {}
# response = requests.request("GET", url, headers=headers, data=payload)
# data = json.loads(response.text)
# print(data)

''' Example responses
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
   
HEADERS
{
    'Date': 'Wed, 07 Sep 2022 20:49:01 GMT', 
    'Content-Type': 'application/json', 
    'Content-Length': '1593', 
    'Connection': 'keep-alive', 
    'CF-Ray': '74724efdad34c571-SEA', 
    'Accept-Ranges': 'bytes', 
    'Access-Control-Allow-Origin': '*', 
    'Age': '242', 
    'Cache-Control': 'max-age=300, public', 
    'Content-Encoding': 'gzip', 
    'Last-Modified': 'Wed, 07 Sep 2022 20:44:59 GMT', 
    'Vary': 'Accept-Encoding', 
    'CF-Cache-Status': 'HIT', 
    'access-control-allow-headers': '*', 
    'access-control-allow-methods': 'GET, HEAD, OPTIONS', 
    'access-control-expose-headers': 'Content-Encoding, X-Total-Page-Count', 
    'cdn-cache-control': 'max-age=600, stale-while-revalidate=60, stale-if-error=86400, public', 
    'php-cache': 'MISS', 
    'php-cache-age': '0', 
    'php-cache-key': 'd66e5afa40d697df38696fa08ef8f601385db2f9', 
    'php-cache-max-age': '300', 
    'x-powered-by': 'The love of games, an addiction to deals, and a bit of code! :)', 
*   'x-total-page-count': '300',    ***************** useful ******************
    'Report-To': '{
        "endpoints":[
            {"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=bNnMJsdJP%2F60EXWM3%2BoB09RnNnexCTGk%2FKHXyapCyI7o8KHPopnrmSbtEn%2Fx3PW634tU1%2B5cLPZ%2BA%2B7u6NQMjTBElEF70ilViFLq9eZD4KxclgkSnaCh706%2BfZcO24Chre8JZQ%3D%3D"}],"group":"cf-nel","max_age":604800}', 'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}', 'Server': 'cloudflare'}
'''

# counter = 1
# for game in data:
#     # print(game['title'])
#     print(f"{counter}. {game['title']}\nSale price {game['salePrice']} - Normal price {game['normalPrice']}")
#     counter += 1

# selection = int(input("Which game do you want to see more information on?: ")) - 1 

''' Example response
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

# print(f"""\n{data[selection]['title']} - https://www.cheapshark.com/redirect?dealID={data[selection]['dealID']}         
#     Sale price {data[selection]['salePrice']} - Normal price {data[selection]['normalPrice']}       Savings - {data[selection]['savings']}% - Deal Rating {data[selection]['dealRating']}
#     Steam Rating - {data[selection]['steamRatingPercent']}% {data[selection]['steamRatingText']} with {data[selection]['steamRatingCount']} reviews
#     Metacritic Score - {data[selection]['metacriticScore']}%
#     """)

# Runs a new request on the selected game using new variables so old data still present if needed (for now, may change to simplify)
# game_url = f"https://www.cheapshark.com/api/1.0/games?id={data[selection]['gameID']}"
# payload={}
# headers = {}
# response = requests.request("GET", game_url, headers=headers, data=payload)
# game_data = json.loads(response.text)
# print(game_data)

''' Example response - can pull store data/links and cheapest ever info by using game_data instead of data

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


# Search for a game and list results - Can then get the game ID to go directly to that page like above
# game_title = input("Enter a game to search for: ")
# url = f"https://www.cheapshark.com/api/1.0/games?title={game_title}&limit=10&exact=0"
# payload={}
# headers = {}
# response = requests.request("GET", url, headers=headers, data=payload)
# data = json.loads(response.text)
# print(data)

# counter = 1
# for game in data:
#     print(game['external'])
#     # print(game['title'])
#     print(f"{counter}. {game['external']}\nSale price {game['salePrice']} - Normal price {game['normalPrice']}")
#     counter += 1
