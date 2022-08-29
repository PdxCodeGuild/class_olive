'''
This lab will build and manage a contacts list CRUD style
'''
# Create
# Read
# Update
# Destroy 

# sometimes CRUD L
# List

import time

with open('contacts_crud.csv', 'r') as file:
    lines = file.read().split('\n')


get_dict_values = []
for x in range(len(lines)):
    get_dict_values += lines[x].split(',')
    

get_dict_keys = []
for x in range(3):
    get_dict_keys.append(get_dict_values.pop(0))


get_contacts_dict = {}
contacts = []
loop_counter = 0
for x in range(int(len(get_dict_values)/3)):
    get_contacts_dict[get_dict_keys[0]] = get_dict_values[loop_counter]
    loop_counter += 1
    get_contacts_dict[get_dict_keys[1]] = get_dict_values[loop_counter]
    loop_counter += 1
    get_contacts_dict[get_dict_keys[2]] = get_dict_values[loop_counter]
    loop_counter += 1
    contacts.append(get_contacts_dict.copy())

print(contacts, 'contacts')

def make_character():
    return_dict = {}
    for key in get_contacts_dict:
        return_dict[key] = input(f'Enter {key}.\n>: ')
    contacts.append(return_dict.copy())

def get_character():
    for sheet in contacts:
        print(f'{sheet["name"]}')
    character = input('Which character?\n>: ')
    for sheet in contacts:
        if character == sheet['name']:
            print(f'''
            Name: {sheet['name']}
            Class: {sheet['class']}
            Alignment: {sheet['alignment']}
            ''')
    return character

def update_character():
    character = get_character()

    user_input_key = input(f'Choose one to update.\n{get_dict_keys}').lower()
    user_input_choice = input(f'Enter new data for {user_input_key}.\n>: ')
    for sheet in contacts:
        if sheet[user_input_key] == character:
            sheet[user_input_key] = user_input_choice
            break

def destroy_character():
    character = get_character()

    for i, person in enumerate(contacts):
        if person['name'] == character:
            contacts.pop(i)

def list_characters():
    for sheet in contacts:
        print(f'''
        Name: {sheet['name']}
        Class: {sheet['class']}
        Alignment: {sheet['alignment']}
        ''')

        

    



while True:
    user_input_main = input(f'''
    Enter the number of what you would like to do?
    1. Create character.
    2. Retrieve character.
    3. Update character.
    4. DESTROY CHARACTER.
    5. List all characters.
    >: ''')

    if user_input_main == '1':
        make_character()
    
    elif user_input_main == '2':
        get_character()
    
    elif user_input_main == '3':
        update_character()
    
    elif user_input_main == '4':
        destroy_character()

    elif user_input_main == '5':
        list_characters()

    print('DEBUG:', contacts)