"""def encrypt(pad, secret):
    return ''.join([chr(ord(c) ^ ord(secret[i])) for i, c in enumerate(pad[:len(secret)])])





secret = 'i am a secret'
pad = '33116f14-9b6f-42c6-9636-3dbd31c0548d'
enc = encrypt(pad, secret)
print("Encrypted: ",enc)
assert secret == encrypt(pad, enc)
print("Decrypted: ",secret)"""
import onetimepad

cipher = onetimepad.encrypt('OmorSourov', 'random')
print("Cipher text is ")
print(cipher)
print("Plain text is ")
msg = onetimepad.decrypt(cipher, 'random')

print(msg)