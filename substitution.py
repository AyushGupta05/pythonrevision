key = input ("whats the key")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while len(key) != 26:
    print ("wrong length. fix")
    key = input ("whats the key")

plaintext = input ("input plaintext").upper()

newstring = ""

for char in plaintext:
    value = alphabet.find(char)
    if value == -1:
        newstring += char
    newstring += key[value]

print (newstring)
