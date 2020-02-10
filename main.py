highest = 0
lowest = 10
total = 0
counter = 0
exitKey = 'y'
overallAvg = 0

while exitKey == 'y' or exitKey == 'Y':
  counter+=1
  highest = 0
  lowest = 10
  total = 0
  
  for x in range(5):
    number = float(input("Enter a number"))
    while number < 0 or number > 10:
      number = float(input("Invalid Input! Please Reenter: "))
    total += number
    if number < lowest:
      lowest = number
    elif number > highest:
      highest = number
  
  print "Highest score is", highest,"Lowest score is", lowest
  avg = (total - (highest+ lowest)) / 3
  print "Average is", avg
  print "Counter is:",counter
  overallAvg += avg
  exitKey = input("Would you like to continue? (Type y or n)")

print "Final Average is: ", (overallAvg / counter)