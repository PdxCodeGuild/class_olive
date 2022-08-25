from re import A


input_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17,
's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
output_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'} 

rot_output = ''

test = 'abc'
rotate = int(input("Rotate by how many numbers?: "))

for letter in test:
    # print(f"{letter} - {input_dict[letter]}")
    
    rot_index = input_dict[letter] + rotate
    
    rot_letter = output_dict[rot_index]

    print(f"The input letter was *{letter}* and your output letter is *{rot_letter}*")
         
    # # print(type(rot_letter))
    # print(f"Rotated letter is {rot_letter}")
    # rot_output = rot_output + rot_letter
    
'''
a - ind 0  ROT25 -- z
b - ind 1  ROT25 -- a
if starting index is over 25, need to figure out how to get it to loop back to index 0 and keep counting
'''