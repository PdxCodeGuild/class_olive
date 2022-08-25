import string

def rot13encrypt():

    while True:

        listtoencrypt = list(input("What are we trying to encrypt: "))

        #rotations = int(input("How many times would you like to rotate the cipher: "))
        code_keys = list((string.ascii_lowercase+string.ascii_uppercase))
        code_values = list('nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM')
        cipher = dict(zip(code_keys,code_values))
        encryptanddecrypt = {

        }

        for letter in listtoencrypt:
            encryptanddecrypt[letter] = cipher[letter]
        
        decryptedmessage = list(encryptanddecrypt.keys())
        encryptedmessage = list(encryptanddecrypt.values())

        print(f"This is your encrypted message {encryptedmessage}")
        decrypt_question = int(input('Type any number > 0 to decrypt the message:')) 

        if decrypt_question > 0:
            print(f"This is your decrypted message: {decryptedmessage} - look familiar?")
        
        tryagain = input("Type y if you want to try again: ").upper()
        if tryagain == 'Y':
            True
        else:
            False
            
rot13encrypt()
