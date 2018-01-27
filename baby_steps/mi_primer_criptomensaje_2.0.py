from Crypto import Random
from Crypto.Cipher import AES
import base64

BLOCK_SIZE=16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s : s[0:-ord(s[-1])]

def encrypt(message, cipherKey):
    message = pad(message)
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(cipherKey, AES.MODE_CBC, IV)
    return base64.b64encode(IV + aes.encrypt(message))

def decrypt(encrypted, cipherKey):
    encrypted = base64.b64decode(encrypted)
    IV = encrypted[:BLOCK_SIZE]
    aes = AES.new(cipherKey, AES.MODE_CBC, IV)
    return unpad(aes.decrypt(encrypted[BLOCK_SIZE:]))



randomKey = Random.new().read(BLOCK_SIZE*2)

print "Da key: " + base64.b64encode(randomKey)

message = 'Billpocket is the shit!'

ciphertext = encrypt(message, randomKey)

print "Da ciphertext: " + ciphertext

deciphered = decrypt(ciphertext, randomKey)

print "Da original message: " + deciphered