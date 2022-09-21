def encrypt(pad, secret):
    return ''.join([chr(ord(c) ^ ord(secret[i])) for i, c in enumerate(pad[:len(secret)])])
secret = 'i am a secret'
pad = '33116f14-9b6f-42c6-9636-3dbd31c0548d'
enc = encrypt(pad, secret)
print(enc)
assert secret == encrypt(pad, enc)
print(secret)