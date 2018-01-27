import Crypto
from Crypto.PublicKey import RSA
# from Crypto.PublicKey import ECC
import base64
import ast

from datetime import datetime

KEY_SIZE = 1024

print "Testing RSA"
key = RSA.generate(KEY_SIZE)

publickey = key.publickey()

print "PublicKey: " + base64.b64encode(publickey.exportKey())

message = "Billpocket is the shit!";

encrypted = publickey.encrypt(message, 0)

print 'encrypted message:' + base64.b64encode(encrypted[0]) #ciphertext

dt = datetime.now()
decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
print "Decryption took: " + str(datetime.now().microsecond  - dt.microsecond ) + " microseconds"

print 'decrypted', decrypted

# print "========================="
# print "Testing ECC, Realy Crypto Has Curves"

# CURVE_NAME = 'P-256'
# key = ECC.generate(curve=CURVE_NAME)
# publickey = key.publickey()

# print "PublicKey: " + base64.b64encode(publickey.exportKey())

# message = "Billpocket is the shit!";

# encrypted = publickey.encrypt(message, 0)

# print 'encrypted message:' + base64.b64encode(encrypted[0]) #ciphertext

# dt = datetime.now()
# decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
# print "Decryption took: " + str(datetime.now().microsecond  - dt.microsecond ) + " microseconds"

# print 'decrypted', decrypted