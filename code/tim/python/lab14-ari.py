import string

from string import ascii_letters, digits, punctuation
printable = digits + ascii_letters + punctuation   # Variable from string file had whitespace included, removed
# sentence_end = '.?!'

with open('lab14-timemachine.txt', encoding='utf8') as file:
    text = file.read()

# Checks if each character in text is in printable characters from string file and adds 1 to count if so
char_count = 0
for char in text:
    if char in printable:
        char_count += 1
print("Total character count -",    char_count)  # Total printable characters - 145902

# Splits string using blank spaces into a list of words, leaving the number of words
word_count = len(text.split())
print("Total word count -", word_count)   # Total word count - 32453

# Splits string using ! ? . leaving the number of sentences
sentence_count = len(text.split('!')) + len(text.split('?')) + len(text.split('.'))
print("Total sentence count -",     sentence_count)  # Total sentence count - 1970

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

ari = 4.71 * (char_count/word_count) + 0.5 * (word_count/sentence_count) - 21.43

# Adds 1 to ARI then converts to int which rounds down.  Don't see an easy way to round up, workaround.
ari = int(ari+1)

if ari > 14:
    ari = 14

print(f"ARI is {ari}.") 


print(f'''
-------------------------------------------------------------------------
The ARI for timemachine.txt is {ari}.
This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari]['ages']} years old.
-------------------------------------------------------------------------
''')

