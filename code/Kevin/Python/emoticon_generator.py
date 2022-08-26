'''
Program for generating random emoticons.
'''

import random

#Assign a variable to output our emoticon.
output_str = ''

#Make a list of potential eyes.
eyes_list = [':',';','x','X','=']

#Make a list of potential noses.
nose_list = ['-','^','+',"'"]
nose_number = random.randint(0, 5)  #66% chance of nose

#Make a list of potential mouths.
mouth_list = ['D','d','p','P','o','O','/','|',']','}',
'{','[','c','C','X','x']

#Make a list of potential brows.
brow_list = ['>', '<',]
brow_number = random.randint(0, 5)      #33% change of brow

#If the "brownumber" is an index in the "brow_list", concatenate a brow.
if brow_number < 2:
    output_str = output_str + brow_list[1]

#Give a random eye.
output_str = output_str + eyes_list[random.randint(0, 4)]

#If "nose_number" is an index in the "nose_list", concatenate a nose.
if nose_number < 4:
    output_str = output_str + nose_list[nose_number]

#Give a random mouth.
output_str =  output_str + mouth_list[random.randint(0,15)]

#???
if random.randint(1,20) == 1:
    print(output_str, "Wow that's ugly")
    
#Print our emoji!
else:
    print(output_str)




