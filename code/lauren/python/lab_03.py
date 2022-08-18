list_of_hundreds = ["zero", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"] 
list_of_tens = ["zero", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
list_of_ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]


num = input("Enter a number 0-999: ")

if int(num) > 99:
  digit_1 = list_of_hundreds[int(num[0])]
  digit_2 = list_of_tens[int(num[1])]
  digit_3 = list_of_ones[int(num[2])]

  if digit_2 == "zero" and digit_3 == "zero":
    print(digit_1)
  elif digit_2 == "zero":
    print(digit_1, digit_2)
  else:
    print(digit_1, digit_2, digit_3)

elif int(num)>19:
   digit_2 = list_of_tens[int(num[0])]
   digit_3 = list_of_ones[int(num[1])]
   if digit_3 == "zero":
     print(digit_2)
   else:
     print(digit_2, digit_3)

else:
   digit_2 = list_of_ones[int(num)]
   print(digit_2)
