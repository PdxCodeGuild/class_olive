# Lab 11 Contact List

# Import from CSV file to a LIST
with open('lab11_input.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

# Strips out the first line from CSV and saves them to a variable
headers = lines[0]
lines.pop(0)

contacts = []

# Starts looping over imported results
for person in lines:
    # Splits the string at , and saves each line/list index to a variable
    split_line = person.split(',')
    name = split_line[0]
    age = split_line[1]
    job = split_line[2]
    
    # Adds a new dictionary with each contact's information
    contact = {
        'name': name,
        'age': age,
        'job': job
        }
    
    # Adds the contact dictionary to the full list of contacts
    contacts.append(contact)

print(contacts)