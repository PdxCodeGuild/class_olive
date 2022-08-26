from distutils.command.clean import clean
from operator import concat
from posixpath import split
from string import ascii_lowercase, ascii_uppercase


with open('kant.txt', 'r') as file:
    text = file.read()

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

print(text)

words = int(len(text.split()))
sentences = int(text.count('.') + text.count('!') + text.count('?'))
characters = (ascii_lowercase+ascii_uppercase)
#print(characters)

character_counter = 0

for characters in text:
    character_counter += 1

#test_ARI = 5.01
raw_ARI = ((4.71*(character_counter/words))+(.5*(words/sentences))-21.43)
clean_ARI = ' '

'''
if test_ARI > 14:
    clean_ARI = 14
else:
    clean_ARI = round(test_ARI+.49,0)
'''

if raw_ARI > 14:
    clean_ARI = 14
else:
    clean_ARI = round(clean_ARI+.49,0)


print(raw_ARI)
print(clean_ARI)

print(f" There are {character_counter} characters in Kant's Theory of Knowledge")

print(f" There are {words} words in Kant's Theory of Knowledge")

print(f" There are {sentences} sentences in Kant's Theory of Knowledge")

print(f"For this text, the ARI is {clean_ARI} which means the reading age is {(ari_scale[clean_ARI]['ages'])} and the grade level is {ari_scale[clean_ARI]['grade_level']} ")