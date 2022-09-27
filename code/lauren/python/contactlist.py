with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
headers = lines[0]
headers =  headers.split(',')
print(headers[2])

lines.pop(0)
print(lines)

contacts = []

    
for item in lines:
    print(item)
    person = item.split(',')
    print("wtf")
    #print(item)   
    try:
        person_dictionary = {
            headers[0]: person[0],
            headers[1]: person[1],
            headers[2]: person[2]
        }
        contacts.append(person_dictionary)
    except:
        pass
    

def create():
    name = input('Enter your name: ')
    occupation = input('Enter your occupation: ')
    phone_number = input('Enter your phone number: ')
    
    person = {
        'name': name,
        'occupation': occupation,
        'number': phone_number
    }

    write(person)
    
def write(person):
    contacts.append(person)
    
def read():
    name = input('Enter the name of the person you are searching for: ')
    for person in contacts:
        
        if person ['name'] == name:
            print (f'''
                   Name: {person['name']}
                   Occupation: {person['occupation']}
                   Phone number: {person['number']}
                   \n''')  
    return name
            
def update():
    name = read()   
    choice = input('Update name, occupation or phone number? ')
    new_choice = input('Enter updated information: ')
    
    for person in contacts:
        if person['name'] == name:
            if choice == 'name':
                person['name'] == new_choice
            elif choice == 'occupation':
                person['occupation'] == new_choice
            elif choice == 'phone number':
                person ['number'] == new_choice
                
def delete():
    name = read()
    
    for index in range (len(contacts)):
        if name == contacts[index]['name']:
            contacts.pop(index)
            break
        
def list_contacts():
    counter = 1
    for person in contacts:
        print(f" {counter} {person['name']}, {person['occupation']}, {person['number']}\n")
        counter += 1
        
def updatecsv():
    with open('contacts.csv', 'w') as f:
        f.write("name,occupation,number\n")
        for index, person in enumerate(contacts):
            f.write(f"{person['name']},{person['occupation']},{person['number']}\n")
            
        
def main():
    while True:
        choice = input("""\nWelcome to the employee directory, what would you like to do?:
        1: Create new work contact
        2: retrieve employee record
        3: update employee information
        4: delete employee
        5: list all records
        6: quit
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
            updatecsv()
            print('Goodbye')
            break
        
main()
                          
        
        
            
              
    

