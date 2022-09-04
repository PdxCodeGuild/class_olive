import urllib.request, requests, json, random, time
from pprint import pprint


#-------------------------------------------------------------------------------------------------#
#convert unusable copy/paste txt file from internet into dictionary
# with open('states.txt', 'r') as file:
#     text = file.read()
# list_states = text.split('\n')
# for line in list_states:
#     if line == "":
#         list_states.remove("")
# dict_states = {}
# for index in range(0, len(list_states), 2):
#     dict_states[list_states[index]] = list_states[index + 1]

dict_states = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}
#-------------------------------------------------------------------------------------------------#

def call_api(url_ending):
    base_url = "https://developer.nps.gov/api/v1/"
    endpoint = base_url + url_ending
    full_url = f"{endpoint}&api_key=pFm8VhiC54asI4hv9lTzsa3hqDk3H3ruTTn8CtNX"
    response = requests.get(full_url)
    # HEADERS = {"Authorization":"pFm8VhiC54asI4hv9lTzsa3hqDk3H3ruTTn8CtNX", "Accept":"application/json"}
    # r = urllib.request.Request(endpoint,headers=HEADERS)
    # text = urllib.request.urlopen(r).read()
    # data = json.loads(text.data)
    #response = requests.get(endpoint, headers=HEADERS)
    data = json.loads(response.text)
    return data


def find_parks(state_or_state_code):
    if len(state_or_state_code) != 2:
        if state_or_state_code in dict_states.keys():
            state_code = dict_states[state_or_state_code]
        else:
            print("Error: state not found.")
    else:
        if state_or_state_code in dict_states.values():
            state_code = state_or_state_code
        else:
            print("Error: state not found")
    data = call_api(f"parks?stateCode={state_code}")
    return data

def slow_print(str):
    for letter in str:
        print(letter, end="", flush=True)
        time.sleep(.04)


quotes = ["""
Of all the paths you take in life, make sure a few of them are dirt. ~ John Muir
 """,
 """
 I’d rather be in the mountains thinking of God, than in church thinking about the mountains. ~ John Muir
 """,
 """
 In every walk with nature one receives far more than he seeks." ~ John Muir
 """,
 """
 Thousands of tired, nerve-shaken, over-civilized people are beginning to find out 
 that going to the mountains is going home; that wildness is a necessity. ~ John Muirs
 """]



slow_print(quotes[random.randint(0, 2)])
time.sleep(1)
print("""
------------------------------------------------------------------------------------------------------
                                    THIS LAND IS YOUR LAND..... SEE IT
                                A JOURNEY IN SEEING ALL THE NATIONAL PARKS

Select an option from the following menu:

        1. See the parks you've been to                     2. See the parks you haven't been to
        3. Plan a trip                                      4. Exit

------------------------------------------------------------------------------------------------------
""")

# # for state in dict_states.keys():
# #     parks_in_state = find_parks(state)['data']
# #     print()
# #     print(f"{state.upper()}\n")
# #     for park in parks_in_state:
# #         if park['designation'] == 'National Park':
# #             print(f"\t{park['fullName']}")
# # print()


# # list_of_parks = data['data']
# # # print(list_of_parks[0])
# # for park in list_of_parks:
# #     if park['designation'] == 'National Park':
# #         print(park['fullName'])
# with open('results.txt', 'w') as file:
#             file.write(str(data))