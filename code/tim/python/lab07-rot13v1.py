# Rot Cipher
# Write a program that prompts the user for a string, and encodes it with ROT13. 
# For each character, find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.

################################################################## 
# Unused lists and dictionaries, saving for v2 if needed           
# english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# rot13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
# rot13 = {'n':0, 'o':1, 'p':2, 'q':3, 'r':4, 's':5, 't':6, 'u':7, 'v':8, 'w':9, 'x':10, 'y':11, 'z':12,'a':13, 'b':14, 'c':15, 'd':16, 'e':17,
#  'f':18, 'g':19, 'h':20, 'i':21, 'j':22, 'k':23, 'l':24, 'm':25}
##################################################################

english = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17,
's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}

# english = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r',
#  18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}

rot13 = {0:'n', 1:'o', 2:'p', 3:'q', 4:'r', 5:'s', 6:'t', 7:'u', 8:'v', 9:'w', 10:'x', 11:'y', 12:'z',13:'a', 14:'b', 15:'c', 16:'d', 17:'e', 
18:'f', 19:'g', 20:'h', 21:'i', 22:'j', 23:'k', 24:'l', 25:'m'}

# eng_input = input("Enter some text: ").lower()
rot_output = ''

##### Take the letters from the input and get their English index positions, then print that ROT13 index, and add each letter to a string
# for letter in eng_input:
#     eng_index = english[letter]
#     rot_letter = rot13.get(eng_index)
#     rot_output = rot_output + rot_letter

# print(f"{eng_input} translated to ROT13 is {rot_output}")  # Works except for spaces/punctuation

test = 'abyz'
rotate = int(input("Rotate by how many numbers?: "))   ## Setting up rotation

for letter in test:
    
    eng_index = english[letter]
    rot_index = eng_index + rotate

    # if eng_index > 25:
    #     rot_index = eng_index - (rotate+13) 
    # else:
    #     rot_index = eng_index + (rotate+13) 
    
    # print(f"Index of {letter} is {eng_index}")
    # print(f"Rotated index is {rot_index}")
     
    rot_letter = str(rot13.get(rot_index))
    # print(type(rot_letter))
    print(f"Rotated letter is {rot_letter}")
    rot_output = rot_output + rot_letter

print(test, rot_output)




print(english[rotate])
