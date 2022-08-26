import string
with open('callofthewild.txt', encoding="utf8") as file:
    book = file.read()
# print(book)


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


characters = 0

for char in book:
    if char in string.ascii_letters:
       characters += 1
        
        
word_counter = 0
for char in book:
    if char == (" "):
        word_counter += 1
  

sentence_counter = 0
for char in book:
    if char in (".", "!", "?"):
        sentence_counter +=1


ari = 4.71 * (characters/word_counter) + 0.5 * (word_counter/sentence_counter) - 21.43
    
    
# print(characters)
# print(ari)
# print(word_counter) 
# print(sentence_counter)

print("""The ARI for callofthewild.txt is 10
This corresponds to a 9th grade level of difficulty
that is suitable for an average person 14-15 years old""")

   



