conversion = input("Are you encrypting or decrypting?")
test = input("What's the secret message?")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipherMessage = ""
key = int(input("What is they key?"))
x = 0
while x < len(test):
  whereisletter = alphabet.find(test[x])
  if conversion == "encrypting" or conversion == "Encrypting":
    newletter = alphabet[(whereisletter + key)%26]
  else:
    newletter = alphabet[(whereisletter - key)%26]
  cipherMessage = cipherMessage + newletter
  x = x + 1
print cipherMessage
