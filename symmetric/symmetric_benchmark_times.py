from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import DES3

from datetime import datetime

import base64

AES_BLOCK_SIZE=16
DES_BLOCK_SIZE=8

aes_pad = lambda s: s + (AES_BLOCK_SIZE - len(s) % AES_BLOCK_SIZE) * chr(AES_BLOCK_SIZE - len(s) % AES_BLOCK_SIZE)
aes_unpad = lambda s : s[0:-ord(s[-1])]

def aes_encrypt(message, cipherKey):
    message = aes_pad(message)
    IV = Random.new().read(AES_BLOCK_SIZE)
    aes = AES.new(cipherKey, AES.MODE_CBC, IV)
    return base64.b64encode(IV + aes.encrypt(message))

def aes_decrypt(encrypted, cipherKey):
    encrypted = base64.b64decode(encrypted)
    IV = encrypted[:AES_BLOCK_SIZE]
    aes = AES.new(cipherKey, AES.MODE_CBC, IV)
    return aes_unpad(aes.decrypt(encrypted[AES_BLOCK_SIZE:]))


des_pad = lambda s: s + (DES_BLOCK_SIZE - len(s) % DES_BLOCK_SIZE) * chr(DES_BLOCK_SIZE - len(s) % DES_BLOCK_SIZE)
des_unpad = lambda s : s[0:-ord(s[-1])]

def des3_encrypt(message, cipherKey):
    message = des_pad(message)
    IV = Random.new().read(DES_BLOCK_SIZE)
    des3 = DES3.new(cipherKey, DES3.MODE_CBC, IV)
    return base64.b64encode(IV + des3.encrypt(message))

def des3_decrypt(encrypted, cipherKey):
    encrypted = base64.b64decode(encrypted)
    IV = encrypted[:DES_BLOCK_SIZE]
    des3 = DES3.new(cipherKey, DES3.MODE_CBC, IV)
    return des_unpad(des3.decrypt(encrypted[DES_BLOCK_SIZE:]))

print "Benchmarking AES"

randomKey = Random.new().read(AES_BLOCK_SIZE*2)

print "Da key: " + base64.b64encode(randomKey)

message = "Billpocket is the shit!" * 4096

dt = datetime.now()
ciphertext = aes_encrypt(message, randomKey)
print "Decryption took: " + str(datetime.now().microsecond  - dt.microsecond ) + " microseconds"


deciphered = aes_decrypt(ciphertext, randomKey)


print "====================="

print "Benchmarking 3DES"

randomKey = Random.new().read(DES_BLOCK_SIZE*3)

print "Da key: " + base64.b64encode(randomKey)

ciphertext = des3_encrypt(message, randomKey)

dt = datetime.now()
deciphered = des3_decrypt(ciphertext, randomKey)
print "Decryption took: " + str(datetime.now().microsecond  - dt.microsecond ) + " microseconds"