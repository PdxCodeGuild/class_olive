# Lab 11 Contact List
## Version 1

# Import from CSV file to a LIST
with open('lab11_input.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

# Strips out the first line from CSV and saves them to a variable
headers = lines[0]
lines.pop(0)

visitors = []

# Starts looping over imported results
for person in lines:
    # Splits the string at , and saves each line/list index to a variable
    split_line = person.split(',')
    name = split_line[0]
    age = split_line[1]
    job = split_line[2]
    
    # Adds a new dictionary with each contact's information
    visitor = {
        'name': name,
        'age': age,
        'job': job
        }
    
    # Adds the contact dictionary to the full list of contacts
    visitors.append(visitor)

## Version 2 - Implement a CRUD REPL

# Create a user
def create():
    name = input("Name: ").lower()
    age = input("Age: ").lower()
    job = input("Job: ").lower()

    visitor = {
        'name': name,
        'age': age,
        'job': job
    }

    # Passes the new user to the write function
    write(visitor)

# Write the change by adding it to the full contact list
def write(visitor):
    visitors.append(visitor)
    
# Retrieve a user
def read():
    name = input("Enter the name of the visitor you are searching for: ").lower()
    for visitor in visitors:

        if visitor['name'] == name:
            print(f"""
            Name: {visitor['name']}
            Age: {visitor['age']}
            Job: {visitor['job']}
            \n""".title())
    return name    

# Update a user
def update():
    # Calls the read function to pull up existing user and display info first
    name = read().lower()
    choice = input("Update name, age, or job?: ").lower()
    new_value = input("Change to: ")

    # Input choice becomes dictionary key, updates with new_value
    for visitor in visitors:
        if visitor['name'] == name:
            if choice == 'name':
                visitor['name'] = new_value
            elif choice == 'age':
                visitor['age'] = new_value
            elif choice == 'job':
                visitor['job'] = new_value
            
            print(f""" 
                    *** New Information ***\n
                    Name: {visitor['name']}
                    Age: {visitor['age']}
                    Job: {visitor['job']}
                    \n""".title())
# Delete a user
def delete():
    # Calls the read function to pull up existing user and display info first
    name = read()

    for index in range(len(visitors)):
        if name == visitors[index]['name']:
            print(f"{visitors[index]['name']}".title(), "has been deleted.")
            visitors.pop(index)
            break

# List all users
def list_visitors():
    counter = 1
    for visitor in visitors:
        print(f"{counter} {visitor['name']}, {visitor['age']}, {visitor['job']}\n".title())
        counter += 1

# Exit and save changes
def exit():
    # Data to export starts with headers saved earlier
    output_data = f"{headers}\n"
    
    # Loops through each visitor and adds them to a string for export
    for visitor in visitors:
        output_data = output_data + f"{visitor['name']},{visitor['age']},{visitor['job']}\n"
    
    print(output_data)
    
    # Write to output csv
    with open('lab11_output.csv', 'w') as file:
        file.write(output_data)
    print('Visitor list saved.  Goodbye.')    
    quit()

def itsaunixsystem():
    
    while True:
        choice = input("""Welcome to Jurassic Park visitor records.  Hold on to your butts.
        1: Add a new visitor                                    4: Remove a visitor (the nice way)                         
        2: Retrieve a visitor's information                     5: Remove a visitor / Feed the T-Rex
        3: Update a visitor's information                       6: List current visitors
        
        7: Exit and save changes
        Choice: """)
        
        if choice == '1':
            create()
        if choice == '2':
            read()
        if choice == '3':
            update()
        if choice == '4':
            delete()
        if choice == '5':
            while True:
                print("Ah ah ah, you didn't say the magic word!")
        if choice == '6':
            list_visitors()
        if choice == '7':
            exit()

itsaunixsystem()   