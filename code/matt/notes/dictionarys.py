'''
Python Dictionary's
'''

# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, 
# changeable and do not allow duplicates. 

# As of Python version 3.7, dictionaries are ordered. 
# In Python 3.6 and earlier, dictionaries are unordered.


example_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

# We use the key's to get the value.
# if I wanted to get 3 from this dictionary, I need to name the dictionary and then use [] after its name putting the appropriate key in it

# print(example_dict['c']) # 3


# Dictionary's are useful as they store pairs of data. A key give access to its value which can be a literal like 3 or even another 
# dictionary or list. It can store any datatype


# Address Dictionary 

address = {
    'street': '1231 ne main street',
    'city': 'portland',
    'state': 'oregon',
    'zip': 97032
}

# print(f"The location is {address['street']} {address['city']} {address['state']}, {address['zip']}") 
# The location is 1231 ne main street portland oregon, 97032


# Person Dictionary

person = {
    'name': 'Tim',
    'age': 33,
    'weight': 190 
}


# print(f"{person['name']} is {person['age']} years old") # Tim is 33 years old


# Do not have duplicate keys in your dictionary. It will ignore the previous ones
# DONT DO THIS !!!

person = { 
    'name': 'Tim',
    'age': 33,
    'weight': 190,

    'name': 'Bob',
    'age': 55,
    'weight': 130,

}

# print(f"{person['name']} is {person['age']} years old")

# Make a list of dictionaries 
persons = [
    {
        'name': 'Tim',
        'age': 33,
        'weight': 190,
    },
    {
        'name': 'Bob',
        'age': 55,
        'weight': 130,
    }
]

person_0 = persons[0]

# print(person_0['name'])



# --------------------------------------------------------------


# Person Dictionary

person = {
    'name': 'Tim',
    'age': 33,
    'weight': 190
}

# Address Dictionary 

address = {
    'street': '1231 Ne Main Street',
    'city': 'Portland',
    'state': 'Oregon',
    'zip': 97032
}


# if The address dictionary was for the person, Tim, they would not be meaningfully connected.
# By nesting these two dictionary's in each other we get a meaningful collection of workable data


person = {
    'name': 'Tim',
    'age': 33,
    'weight': 190,
    'address':  {
        'street' :'1231 ne main street',
        'city': 'Portland',
        'state': 'Oregon',
        'zip': 97213
    }
}


# print(person['address']['zip'])

print(f"{person['name']} lives in {person['address']['city']}") # Tim lives in Portland