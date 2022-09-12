import random, time
from nps_parks_api import NPSParks
from config import token


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

#-------------------------------------------------------------------------------------------------#

def format_state(state):
    dict_states = {'Alabama': 'AL', 'Alaska': 'AK', 'American Samoa': 'AS', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL', 'Georgia': 'GA', 'Guam': 'GU', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Northern Mariana Islands': 'MP', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Puerto Rico': 'PR', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virgin Islands': 'VI', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}
    if len(state) != 2:
        if state.title() in dict_states.keys():
            state_code = dict_states[state.title()]
        else:
            print("Error: state not found.")
            return 'Error'
    else:
        if state.upper() in dict_states.values():
            state_code = state.upper()
        else:
            print("Error: state not found")
            return 'Error'
    return state_code



def slow_print(str):
    for letter in str:
        print(letter, end="", flush=True)
        time.sleep(.04)

def print_menu():
    print(f"""\n
------------------------------------------------------------------------------------------------------
                                    THIS LAND IS YOUR LAND..... SEE IT
                                A JOURNEY IN SEEING ALL THE NATIONAL PARKS

Select an option from the following menu:

        1. See the parks you've been to                     2. See the parks you haven't been to
        3. Plan a trip                                      4. See a random National Park
        5. Add a park you've been to                        6. Exit                        

------------------------------------------------------------------------------------------------------
""")

def choice_1():
    try:
        with open('save.txt', 'r') as file:
            parks_been_to = file.read().split(',')
    except:
            print("There was an error loading your data.")
            return
    print()
    for park in parks_been_to:
        print(park)
    print()

def choice_2(national_parks):
    try:
        with open('save.txt', 'r') as file:
            parks_been_to = file.read().split(',')
    except:
            print("There was an error loading your data.")
            return
    parks_not_been_to = []

    for park in national_parks:
        if park['fullName'] not in parks_been_to:
            parks_not_been_to.append(park['fullName'])
    
    print()
    for park in parks_not_been_to:
        print(park)
    print()

def choice_5(national_parks, parks: NPSParks):
    setup = True
    while True:
        if setup:
            try:
                with open('save.txt', 'r') as file:
                    parks_been_to = file.read().split(',')
            except:
                print("There was an error loading your data.")
                return
            setup = False
            for park in parks_been_to:
                try:
                    parks_been_to.remove('')
                except:
                    break
        # if setup:
        #     parks_been_to = ['Yosemite National Park']
        #     setup = False


        national_park_names = []
        for park in national_parks:
            national_park_names.append(park['fullName'])

        while True:        
            state = input("\nCongrats!\nWhat state was the park in or enter exit to go to the main menu:  ").upper()     
            if state.lower() == 'exit':
                return 
            while True:
                state_return = format_state(state)
                if state_return == 'Error':
                    return
                else:
                    break
            park_in_the_state = parks.get_parks(stateCode=state_return)
            park_in_the_state = park_in_the_state['data']
            counter = 1
            national_parks_in_this_state = []
            print()
            for this_park in park_in_the_state:
                if this_park['fullName'] in national_park_names:                    
                    print(f"{counter}. {this_park['fullName']}")
                    counter += 1    
                    national_parks_in_this_state.append(this_park)
            if len(national_parks_in_this_state) == 0:
                print("This state does not have any National Parks.")
            else:
                break
        while True:
                park_choice = input("""\nWhich park did you go to? 
            Select the parks number on the list or enter list to see the list again: """)
                if park_choice.lower() == 'list':
                    counter = 1
                    print()
                    for park in national_parks_in_this_state:
                        print(f"{counter}. {park['fullName']}")
                        counter += 1
                    print()
                    continue
                if park_choice.isdigit():
                    if int(park_choice) <= counter:
                        park_choice = national_parks_in_this_state[int(park_choice) - 1]
                        break
        if park_choice['fullName'] not in parks_been_to:
            parks_been_to.append(park_choice['fullName'])        
            while True:
                your_choice = input(f"""{park_choice['fullName']} has been added to your list! Would you like to add another park?
        yes or no? """)  
                if your_choice.lower() == 'yes':
                    break
                if your_choice.lower() == 'no':
                    parks_been_to_str = ""
                    if len(parks_been_to) != len(set(parks_been_to)):
                        print("Error: You tried to save duplicates. Cannot save.")
                        return
                    for another_park in parks_been_to:
                        parks_been_to_str += f",{another_park}"
                    try:
                        with open('save.txt', 'w') as file:
                                file.write(parks_been_to_str)
                    except:
                        print("There was an error saving your data.")
                    return
        else:
            print("You've already been to this park.")
            your_choice = input("""Would you like to add another park?
        yes or no? """)  
            if your_choice.lower() == 'yes':
                continue
            if your_choice.lower() == 'no':
                parks_been_to_str = ""
                if len(parks_been_to) != len(set(parks_been_to)):
                        print("Error: You tried to save duplicates. Cannot save.")
                        return
                for another_park in parks_been_to:
                    parks_been_to_str += f",{another_park}"
                try:
                    with open('save.txt', 'w') as file:
                            file.write(parks_been_to_str)
                except:
                    print("There was an error saving your data.")
                return


def choice_4(national_parks):
    park_of_the_day = see_park_of_day(national_parks)
    while True:
        learn_more = input(f"""\n
    Would you like to learn more about {park_of_the_day['fullName']}? 
    Yes or No? """)
        if learn_more.lower() == 'yes':
            get_to_know_a_park(park_of_the_day)
            break
        elif learn_more.lower() == 'no':
            break

def get_state_going_to():
    while True:
        state = input("\nWhat state are you going to? ").upper()
        state_return = format_state(state)
        if state_return == 'Error':
            continue
        else:
            break
    return state_return

def get_list_national_parks(national_parks):
    national_parks_list = []
    for park in national_parks:
        national_parks_list.append(park['fullName'])
    return national_parks_list
    
def do_you_want_national_parks_or_all():
    valid_choice = ('national parks', 'national park', 'all')
    while True:
        np_or_all = input("""
    Do you want to see only National Parks or all federal parks in this state? 
    National Parks or All? """)
        np_or_all = np_or_all.lower()
        if np_or_all not in valid_choice:
            continue
        else:
            return np_or_all
    
def print_these_parks(this_states_parks, national_parks_list):
    while True:
        np_or_all = do_you_want_national_parks_or_all()
        this_park_list = []
        if np_or_all.lower() == 'national parks' or np_or_all.lower() == 'national park':       
            no_national_parks = True
            counter = 1
            print()
            for park in this_states_parks:
                if park['fullName'] in national_parks_list:
                    print(f"{counter}. {park['fullName']}")
                    no_national_parks = False
                    counter += 1    
                    this_park_list.append(park)
            print()   
            if no_national_parks:
                print("There are no National Parks in this state.") 
                continue
            else:
                return this_park_list, counter
        else:
            no_parks_at_all = True
            counter = 1
            print()
            for park in this_states_parks:
                print(f"{counter}. {park['fullName']}")
                counter += 1
                no_parks_at_all = False
                this_park_list.append(park)
            print()
            if no_parks_at_all:
                print("There are no Parks in this state.")
                return "Error"
            else:
                return this_park_list, counter
                
def find_park_of_interest(this_park_list, counter):
    choice_again = 'yes'
    while choice_again.lower() == 'yes':
        while True:
            park_choice = input("""\nWhich park are you interested in? 
        Select the parks number on the list or enter list to see the list again: """)
            if park_choice.lower() == 'list':
                counter = 1
                print()
                for park in this_park_list:
                    print(f"{counter}. {park['fullName']}")
                    counter += 1
                print()
                continue
            if park_choice.isdigit():
                if int(park_choice) <= counter:
                    park_choice = this_park_list[int(park_choice) - 1]
                    break
        while True:
            choice = input(f"""\nWould you like to see more about {park_choice['fullName']}? 
        yes or no: 
        """)
            if choice.lower() == 'yes' or choice.lower() == 'no':
                break
        if choice.lower() == 'yes':
            get_to_know_a_park(park_choice)
        while True:
            valid_choice = ('yes', 'no')
            choice_again = input("""Would you like to check out another park? 
    yes or no: """)
            choice_again = choice_again.lower()
            if choice_again not in valid_choice:
                break
            elif choice_again.lower() == 'yes':
                break
            elif choice_again.lower() == 'no':
                return


def choice_3(parks:NPSParks, national_parks):   
    status = "Error"
    go_again = "yes"
    while status == "Error" or go_again.lower() == "yes":
        state = get_state_going_to()
        national_parks_list = get_list_national_parks(national_parks)
        this_states_parks = parks.get_parks(stateCode=state)
        this_states_parks = this_states_parks['data']
        status, counter = print_these_parks(this_states_parks, national_parks_list)
        if status == "Error":
            continue
        else:
            find_park_of_interest(status, counter)
            while True:
                go_again = input(f"\nWould you like to check out another state? Yes or No: ")
                if go_again.lower() == 'yes':
                    break
                elif go_again.lower() == 'no':
                    break
                else:
                    continue


            
        



def print_park_menu(park):
    print(f"""\n
------------------------------------------------------------------------------------------------------
                                    {park['fullName']}
        1. Activities                                               2. Address
        3. Contact Info                                             4. Park Description
        5. Get Directions                                           6. Entrance Fees Info
        7. Entrance Pass Info                                       8. Operating Hours Info
        9. Weather Info                                             10. Exit

------------------------------------------------------------------------------------------------------

    """)

def get_national_parks(parks: NPSParks):
    all_parks = parks.get_parks(limit=500)['data']
    the_forgotten_ones = ['crla', 'npsa', 'redw', 'seki', 'neri']
    national_parks = []
    for park in all_parks:
        if park['designation'] == "National Park" or park['designation'] == "National Park & Preserve" or park['designation'] == "National Parks" or park["parkCode"] in the_forgotten_ones:
            national_parks.append(park)
    return national_parks

def see_park_of_day(national_parks):
    park_of_the_day = random.choice(national_parks)
    slow_print(f"\nThe park randomly selected for you is................. {park_of_the_day['fullName']}")
    return park_of_the_day

def get_to_know_a_park(park): 
    print_park_menu(park)
    choice = input("What would you like to see? ")  
    while True:       
        if choice == '1':
            print()
            for activity in park['activities']:
                print(activity['name'])
        if choice == '2':
            print()
            for address in park['addresses']:
                print(f"""{address['type']}: 
    {address['line1']}{address['line2']}{address['line3']}
    {address['city']}, {address['stateCode']} {address['postalCode']}\n""")
        if choice == '3':
            print()
            contacts = park['contacts']
            if len(contacts['emailAddresses']) > 0:
                print('Email Addresses:')
            for email in contacts['emailAddresses']:
                print(email['emailAddress'])
            if len(contacts['phoneNumbers']) > 0:
                print('\nPhone Numbers:')
            for phone in contacts['phoneNumbers']:
                print(phone['phoneNumber'])
        if choice == '4':
            print()
            print(park['description'])
        if choice == '5':
            print()
            print(park['directionsInfo'])
        if choice == '6':
            print()
            for fee in park['entranceFees']:
                print(f"""{fee['title']}:
    {fee['cost']}
    {fee['description']}\n""")
        if choice == '7':
            print()
            for fee in park['entrancePasses']:
                print(f"""{fee['title']}:
    {fee['cost']}
    {fee['description']}\n""")
        if choice == '8':
            print()
            for hour in park['operatingHours']:
            #     if len(hour['exceptions']) == 0:
            #         hour['exceptions'] = 'None'
            #     else:
            #         for exception in hour['exceptions']:
            #             exception_string = f"{exception}\n"
            #         hour['exceptions']['name'] = exception_string
                print(f"""{hour['name']}:
Description:
{hour['description']}

Standard Hours:
Monday: {hour['standardHours']['monday']}
Tuesday: {hour['standardHours']['tuesday']}
Wednesday: {hour['standardHours']['wednesday']}
Thursday: {hour['standardHours']['thursday']}
Friday: {hour['standardHours']['friday']}
Saturday: {hour['standardHours']['saturday']}
Sunday: {hour['standardHours']['sunday']}
""")
        if choice == '9':
            print()
            print(park['weatherInfo'])
        if choice == '10':
            break
        print_park_menu(park)
        choice = input("Anything else? ") 

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
 that going to the mountains is going home; that wildness is a necessity. ~ John Muir
 """]

### START OF APP --------------------------------------------------------------------------------------------------------------- ###

national_parks_app = NPSParks(token)
national_parks = get_national_parks(national_parks_app)
slow_print(random.choice(quotes))
time.sleep(.25)
while True:
    print_menu()
    choice = input("What would you like to choose? ")

    if choice == '1':
        choice_1()

    if choice == '2':
        choice_2(national_parks)

    if choice == '3':
        choice_3(national_parks_app, national_parks)

    if choice == '4':
        choice_4(national_parks)
    
    if choice == '5':
        choice_5(national_parks, national_parks_app)
    
    if choice == '6':
        break
    