from art import logo

MORSE_CODE = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    store_var = ''
    for letter in message:
        if letter != ' ':
            store_var += MORSE_CODE[letter]
            store_var += ' '
        else:
            store_var += ' '

    return store_var

def decrypt(message):
    message += ' '

    decrypted = ''
    store_char = ''
    i = 0

    for char in message:
        if char != ' ':
            i = 0
            store_char += char
        else:
            i += 1

            if i == 2:
                decrypted += ' '
            else:
                decrypted += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(store_char)]
                store_char = ''

    return decrypted


is_on = True
print(logo)

while is_on:
    choose = input('"E" for Encrypt or "D" for Decrypt: ').lower()
    if choose == "e":
        message = input('Enter your message: ')
        result = encrypt(message.upper())
        print(f"\n{result}\n")
    elif choose == "d":
        message = input('Enter your message: ')
        result = decrypt(message)
        print(f"\n{result}\n")
    else:
        print('\nCommand not found\n')

    choice = input('Continue? "Y" or "N" ').lower()
    if choice == "n":
        is_on = False

