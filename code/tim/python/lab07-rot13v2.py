# Rot Cipher version 2

input_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17,
's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
output_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'} 

rot_output = ''

# test = 'abcxyz'
# rotate = 2
text = input("Enter some text with no spaces: ").lower()
rotate = int(input("Rotate by how many numbers?: "))

## Looping over each letter in text input
for letter in text:

    # Shifts the letter in the ROT dictionary based on how many numbers given in input    
    rot_index = input_dict[letter] + rotate
    
    # If rotation will result in an index higher than 25-Z, use modulus to see what the remainder is and that
    # becomes the rotation, loops back to A-0 and counts from there
    if rot_index >= 25:
        rot_index = rot_index % 26   # 25 didn't work like I thought, because there are 26 index positions
        rot_letter = output_dict[rot_index]
    # If it isn't > 25 just use the input rotation as normal    
    else:        
        rot_letter = output_dict[rot_index]

    # Adds each letter as a string to a variable
    rot_output = rot_output + rot_letter
    
print(f"{text} in ROT{rotate} is {rot_output}.")
    
    
  
    
'''
a - ind 0  ROT25 -- z
b - ind 1  ROT25 -- a
if starting index is over 25, need to figure out how to get it to loop back to index 0 and keep counting

modulus idea - if index > 25, rotate % 25 or something like that.  ie, if rotate is 13, z(25) + 13 will error.
but 25+13 = 38 then if that can be divided by 25 or 26, % should give you the remainder
'''
# print(27 % 25)   # 10 (which would be k) -- think this might work, mess with it