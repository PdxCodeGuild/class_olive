# CRUD

# Create
# Read
# Update
# Destroy 

# sometimes CRUD L
# List


contacts = [
    {
        'name': 'sarah',
        'age': 25,
        'city': 'Portland'
    },
    {
        'name': 'bob',
        'age': 99,
        'city': 'Florida'
    }
]



# Create a single person
def create():
    name = input('Name: ')
    age = input("Age: ")
    city = input("City: ")

    person = {
        'name': name,
        'age': age,
        'city': city
    }

    write(person)

# Write the change
def write(person):
    contacts.append(person)

# Retrieve a single person
def read():
    name = input("Enter the name of the person you are searching for: ")
    for person in contacts:

        if person['name'] == name:
            print(f"""
            Name: {person['name']}
            Age: {person['age']}
            City: {person['city']}
            \n""")

    return name

# Update a single person
def update():
    name = read()
    choice = input("Update their name, age or city?  ")
    new_value = input("Change the Value to: ")

    for person in contacts:
        if person['name'] == name: 
            if choice == 'name':
                person['name'] = new_value
            elif choice == 'age':
                person['age'] = new_value
            elif choice == 'city':
                person['city'] = new_value

# Delete a single contact
def delete():
    name = read()

    for index in range(len(contacts)):
        if name == contacts[index]['name']:
            contacts.pop(index)
            break

# List all contacts
def list_contacts():
    counter = 1
    for person in contacts:
        print(f"{counter} {person['name']}, {person['age']} {person['city']}\n")
        counter += 1

def main():
    while True:
        choice = input("""\nWelcome, what would you like to do to your contacts?: 
        1: Create a new contact
        2: Retrieve a record
        3: Update a record
        4: Delete a record
        5: List all records
        6: Quit
        
        Choice: """)

        if choice == '1':
            create()
    
        elif choice == '2':
            read()

        elif choice == '3':
            update()

        elif choice == '4':
            delete()

        elif choice == '5':
            list_contacts()

        elif choice == '6':
            print("Goodbye")
            break

main()



