text = "special topics"
strlen = len(text)
for x in range(strlen-1,-1,-1):
  print text[x]
  
  
message = ""  
for x in range(strlen-1,-1,-1):  
  message = message + text[x]
print message
#write a program to ask the user to enter a string
#reverse the string and display the reverse string

user = input("Enter a string yo:")
strlen2 = len(user)
reversed = ""
for x in range(strlen2-1,-1,-1):  
  reversed = reversed + user[x]
print reversed