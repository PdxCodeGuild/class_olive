import string

with open('The_Sun_Also_Rises.txt', encoding="utf8") as file:
    text = file.read()

letters = list(string.ascii_letters)
sentence_ending_symbols = ['.', '?', '!']


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

sentence_count = 0
letter_count = 0

text = text.replace('\n', ' ')
text.strip()

for letter in text:
    if letter in letters:
        letter_count += 1

text_list = text.split(" ")
words = len(text_list)

for item in text_list:
    not_word = True
    for letter in item:
        if letter != ' ':
            not_word = False
    if not_word:
        words -= 1

for item in text_list:
    if len(item) > 1:
        if item[-1] == '"' and len(item > 1):
            if item[-2] in sentence_ending_symbols:
                sentence_count += 1
        if item[-1] in sentence_ending_symbols:
            sentence_count += 1
        
ARI = int((4.71 * (letter_count / words)) + (0.5 * (words / sentence_count)) - 21.43)

print(f'''
--------------------------------------------------------
The ARI for The Sun Also Rises is {ARI}
This corresponds to a {ari_scale[ARI]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ARI]['ages']} years old.
--------------------------------------------------------
''')
        
