
def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]   
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result




text = "ATTACKATONCE"
shift = 4
print ("Text  : " + text)
print ("Shift : " + str(shift))
print ("Cipher: " + encrypt(text,shift))
#print ("Cipher: " + decripyt(text,shift))

