# Lab 11: Contact List
'''

Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
Once you've processed the file, your list of contacts will look something like this...

contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]
Note: There is a csv library in Python that will do much of this for you. It is what you would use normally in a project, but for this lab you need to write all the logic yourself.

Version 2
Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
Version 3
When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup contacts.csv because you likely won't write it correctly the first time.

'''

# class ContactList:
#     def __init__(self, file) -> None:
        
contact_dict = {}
keys = []

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
#     print(lines)

# print(lines[0])
# keys.append(lines[0])
# print(keys)
# for key in contact_dict:
for line in lines:
    print(line, '\n')


class Contactlist:
    def __init__(self, firstname, lastname, crew):
        self.firstname = firstname
        self.lastname = lastname
        self.crew = crew

    def add_contact(self, firstname, lastname, crew):
        firstname = input('please enter first name of contact')
        lastname = input('please enter last name of contact')
        crew = input('please enter the name of the crew')
        return firstname + lastname + crew

    def remove_contact(self, firstname, lastname, crew):
        return None


    def edit_contact(self, firstname, lastname, crew):
        return None

    





