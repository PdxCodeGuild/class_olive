def check_duplicate(name):
    for contact in contact_list:
        if contact['Name'] == name:
            print("You already have this contact saved.")
            return True
    return False

def create():
    name = input("\nName: ")
    while check_duplicate(name):
        name = input("\nName: ")
    phone_number = input("Phone-number: ")
    email = input("Email: ")

    contact = {'Name' : name, 'Phone Number': phone_number, 'Email' : email}

    write(contact)

    print(f"\nContact created: Name: {contact['Name']} | Phone: {contact['Phone Number']} | Email: {contact['Email']}")

def write(contact):
    contact_list.append(contact)

def search():
    name = input("\nName: ")
    for contact in contact_list:
        if contact['Name'].lower() == name.lower():
            print(f"\nName: {contact['Name']} | Phone: {contact['Phone Number']} | Email: {contact['Email']}\n")
            return contact
    print(f"\nNo one named {name} was found in your contacts.")

def edit():
    contact = search()
    if contact != None:
        choice = input("Do you want to change name, phone number, or email? ")
        value = input(f"What do you want to change {choice} to? ")

        if choice.lower() == 'name':
            while check_duplicate(value):
                value = input(f"\nNew name for {contact['Name']}: ")
            contact['Name'] = value
        elif choice.lower() == 'phone' or choice.lower == 'phone number' or choice.lower == 'number':
            contact['Phone Number'] = value
        elif choice.lower() == 'email' or choice.lower == 'mail':
            contact['Email'] = value

        print(f"\nThe contact is now: Name: {contact['Name']} | Phone: {contact['Phone Number']} | Email: {contact['Email']}\n")

def delete():
    contact = search()
    for x in range(len(contact_list)):
        if contact_list[x]['Name'] == contact['Name']:
            contact_list.pop(x)
            break
    print(f"You deleted {contact['Name']} from your contact list.")

def save_contacts():
    if len(contact_list) > 0:

        save_string = "Name,Phone Number,Email\n"
        for contact in contact_list:
            save_string += f"{contact['Name']},{contact['Phone Number']},{contact['Email']}\n"

        with open('contact_list.csv', 'w') as file:
            file.write(save_string)

def list():
    print('\n')
    counter = 1
    for contact in contact_list:
        print(f"{counter}. Name: {contact['Name']} | Phone: {contact['Phone Number']} | Email: {contact['Email']}\n")
        counter += 1

def main():
    while True:
        choice = input('''\nWhat would you like to do?
        1. Create a new contact
        2. Search for a contact
        3. Edit a contact
        4. Delete a contact
        5. List all of your contacts
        6. Quit

        Choice:  ''')

        if choice == '1':
            create()
        elif choice == '2':
            search()
        elif choice == '3':
            edit()
        elif choice == '4':
            delete()
        elif choice == '5':
            list()
        elif choice == '6':
            print("\nGoodbye")
            save_contacts()
            break

with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')

keys = lines[0].split(',')
contact_list = []

for x in range(len(lines) - 1):
    line = lines[x + 1].split(',')
    person_dict = {}
    for y in range(len(line)):
        person_dict[f"{keys[y]}"] = line[y]   
    contact_list.append(person_dict)

main()