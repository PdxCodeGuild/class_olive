import string

letters = list(string.ascii_lowercase)

plaintext = input("What would you like to encrypt? ")
crypto_key = int(input("What amount of rotation would you like to use? "))

encrypted_text = ''

for letter in plaintext:
    encrypted_index = letters.index(letter) + crypto_key
    if encrypted_index > 25:
        encrypted_index -= 26
    encrypted_text += letters[encrypted_index]

print(encrypted_text)
