'''
This lab calculates the ARI for a given book.
'''

import string

with open('The_King_in_Yellow.txt', 'r') as file:
    book = file.read()

#Dictionary containing ARI scale.
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


#Declare a dict and store all upper and lower case letters.
char_list = []
char_list += string.ascii_letters
# print(char_list)

#Declare a dict for punctuation.
punctuation_list = ['!', '.', '?']
# print(punctuation_list)

#Decare a dict for spaces.
white_space = [' ']
# print(white_space)

#Decare a variable for remembering the last character inside our for loop.
last_char = ''

#Declare variables for our total numbers of characters, words, and sentences withing the book.
char_int = 0
word_int = 0
sentence_int = 0


# "char" becomes each and every characters in the book.
for char in book:
    if char in char_list:       #If "char" is a character, add 1 to "char_int."
        char_int += 1
    if char in punctuation_list:        #If "char" is in "punctuation", we decide that 1 sentence has occurred.
        sentence_int += 1
    if char in white_space and char != last_char:       #If "char" is a space, and the last "char" was not a space, 
                                                        # we declare that a word has occurred.
        word_int += 1
    last_char = char

# print(char_int, word_int, sentence_int)

#Formula for ARI. 
result = 4.71 * (char_int/word_int) + 0.5 * (word_int/sentence_int) - 21.43
print(result)

#Round up final result.
result = int((result//1) + (result % 1 > 0))
print(result)

#Set result to 14 if above 14.
if result > 14:
    result = 14

print(f'''
The ARI for The King in Yellow is {result}.
This corresponds to a(n) {ari_scale[result]['grade_level']} level of difficulty.
This book is suitable for ages {ari_scale[result]['ages']}
''')