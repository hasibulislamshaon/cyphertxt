def caesar_cipher(raw_text, key): #function called
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[26-key:]+alphabet[0:(26-key)]
    cipher_text = ""

    for i in range(len(raw_text)):
        char = raw_text[i]
        idx = alphabet.find(char.upper())
        if idx == -1:
            cipher_text = cipher_text + char
        elif char.islower():
            cipher_text = cipher_text + shifted_alphabet[idx].lower()
        else:
            cipher_text = cipher_text + shifted_alphabet[idx] 

    return(cipher_text)

text = "ATTACKATONCE"
keyword=4
print("Encripted text: ",caesar_cipher(text,keyword))
print("Decripted text: ",caesar_cipher(caesar_cipher(text,keyword),26-keyword))