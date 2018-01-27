lettersToInteger = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
integerToLetter = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

ciphertext = "OVYYCBPXRG VF GUR FUVG"

for key in range(1,26):
	deciphered = ""
	for c in ciphertext.upper():
	    if c.isalpha(): deciphered += integerToLetter[ (lettersToInteger[c] - key)%26 ]
	    else: deciphered += c

	print "For key " + str(key) + ": " + deciphered