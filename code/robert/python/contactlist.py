import csv


with open('contactsforinput.csv', 'r') as file:
    raw_csv = (file.read().split('\n'))
    print(raw_csv)

csv_workinprogress = []
header_to_keys = raw_csv[0].split(',')

#print(header_to_keys)

#print(len(file))

for items in range(1,len(raw_csv)):
    file_values_to_input = raw_csv[items].split(',')
    file_values_in_dictionary = dict(zip(header_to_keys,file_values_to_input))
    csv_workinprogress.append(file_values_in_dictionary)
    #print(csv_workinprogress)

def create():
    name = input("Name of new lead: ")
    fruit = input("What's their favorite fruit: ")
    color = input("What's their favorite color: ")
    
    contact = {
        'name': name,
        'favorite fruit' : fruit,
        'favorite color' : color
    }

    write_to_list(contact)

def write_to_list(contact):
    csv_workinprogress.append(contact)

def retrieve():
    name = input("Name of existing lead: ")

    for contact in csv_workinprogress:

        if contact['name'] == name:
            print(f"""
            Name: {contact['name']}
            Favorite Fruit: {contact['favorite fruit']}
            Favorite Color: {contact['favorite color']}
            \n""")
    
    return name

def update():
    name = retrieve()
    choice = input("What would you like to update (Name, Fruit, or Color?  ").lower()
    new_value = input("New Value is ").lower()

    for contact in csv_workinprogress:
        if contact['name'] == name: 
            if choice == 'name':
                contact['name'] = new_value
            elif choice == 'fruit':
                contact['favorite fruit'] = new_value
            elif choice == 'color':
                contact['favorite color'] = new_value


def delete():
    name = retrieve()

    for contact in range(len(csv_workinprogress)):
        if name == csv_workinprogress[contact]['name']:
            csv_workinprogress.pop(contact)
            break

def list_of_all():
    counter = 1

    for contact in csv_workinprogress:
        print(f"{counter} {contact['name']}, {contact['favorite fruit']}, {contact['favorite color']}\n")
        counter += 1

def save_to():

    data_to_save = f"Name,Favorite Fruit,Favorite Color\n"
    for data in csv_workinprogress:
        data_to_save += f"{data['name']},{data['favorite fruit']},{data['favorite color']}\n"

    return data_to_save

def main_menu():

    while True:
        user_options = input("""\nWelcome to Color and Fruit Contact List?
        1: Create a New Record
        2: Retrieve a Record
        3: Update an Existing Record
        4: Delete a Record
        5: Retrieve All Records
        6: Close
        Please Select an Option From Above:
         """)

        if user_options == '1':
            create()
        elif user_options == '2':
            retrieve()
        elif user_options == '3':
            update()
        elif user_options == '4':
            delete()
        elif user_options == '5':
            list_of_all()
        else:

            finalcsv = save_to()
            
            with open('finalcontacts.csv', 'w') as file:
                file.write(finalcsv)
            
            print('Thanks for Using Our CRUDL')
            
            break

main_menu()