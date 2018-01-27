lettersToInteger = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
integerToLetter = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 13
plaintext = "BILLPOCKET IS THE SHIT"
print plaintext

# encipher
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha(): ciphertext += integerToLetter[ (lettersToInteger[c] + key)%26 ]
    else: ciphertext += c

print ciphertext

# decipher
deciphered = ""
for c in ciphertext.upper():
    if c.isalpha(): deciphered += integerToLetter[ (lettersToInteger[c] - key)%26 ]
    else: deciphered += c

print deciphered