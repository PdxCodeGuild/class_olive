


# fix for mismatching unicode 
# file = open(filename, encoding="utf8")
# ----------------------------------------------------------------

with open('book.txt', encoding="utf8") as file:
    book = file.read()

with open('book_2.txt', encoding="utf8") as file:
    book_2 = file.read()

with open('book_3.txt', encoding="utf8") as file:
    book_3 = file.read()

# ----------------------------------------------------------------

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

# ----------------------------------------------------------------

character_count = 0
word_count = 0
sentence_count = 0

# ----------------------------------------------------------------

# for character in book:
#     character_count = character_count + 1
#     if character == ' ':
#         word_count = word_count + 1
#     if character == '.':
#         sentence_count = sentence_count + 1

# ----------------------------------------------------------------


for character in book_2:
    character_count = character_count + 1
    if character == ' ':
        word_count = word_count + 1
    if character == '.':
        sentence_count = sentence_count + 1

# ----------------------------------------------------------------


# for character in book_3:
#     character_count = character_count + 1
#     if character == ' ':
#         word_count = word_count + 1
#     if character == '.':
#         sentence_count = sentence_count + 1

# ----------------------------------------------------------------


print(f'character count = {character_count}\nword count = {word_count}\nsentence count = {sentence_count}\n')

# ----------------------------------------------------------------


def ari():
    ari = 4.71*(character_count / word_count) + 0.5*(word_count/sentence_count) - 21.43
    return ari
    
def get_decimal(ari):
    return float( '0.' + str(ari).split('.')[1] )

# print(ari())
# print(get_decimal(ari()))

ari = float(ari() - get_decimal(ari())) + 1
# print(ari)

if ari in ari_scale:
    ari = ari
else:
    ari = 14


print(f"The ARI for This book is {ari} This corresponds to a {ari_scale[ari]['grade_level']} Grade level of difficulty that is suitable for an average person {ari_scale[ari]['ages']} years old.")


# ----------------------------------------------------------------


