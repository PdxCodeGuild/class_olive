import codecs
from string import ascii_lowercase

user_input = input("enter a string: \n")
offset = int(input("offset? "))

new_string = ""

for x in user_input:
    index_of_english_letters = ascii_lowercase.index(x.lower())
    offset_from_english = ascii_lowercase[(index_of_english_letters + offset) % 26]
    new_string += offset_from_english
    


print(user_input)
print(new_string)


