def encrypt(message,shift,alphabet):
    translated = ''
    for letter in message:
        index = alphabet.find(letter)
        move = index + shift
        if move > (len(alphabet)-1):
            difference = move - len(alphabet)
            char = alphabet[difference]
            translated = translated + char
        elif move <= (len(alphabet)-1):
            char = alphabet[move]
            translated = translated + char
    return translated

def decrypt(ciphertext,shift,alphabet):
    translated = ''
    for letter in ciphertext:
        index = alphabet.find(letter)
        move = index - shift
        if move > (len(alphabet)-1):
            difference = move - len(alphabet)
            char = alphabet[difference]
            translated = translated + char
        elif move <= (len(alphabet)-1):
            char = alphabet[move]
            translated = translated + char
    return translated
            


