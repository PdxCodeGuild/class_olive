'''
This program encodes strings into ROT13
'''


letter_dict = {
    ' ':0,
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26
}

letter_list = [' ','a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

user_input_str = 'abcdefghijklmnop'
output_str = ''


for x in user_input_str:
    letter_value = 0
    if x != ' ':
        letter_value = letter_dict[x] + 13
        if letter_value > 26:
            letter_value -= 26
    output_str += letter_list[letter_value]

print(output_str)
    