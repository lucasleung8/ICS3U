# 1. write a function to calculate your grade on an assignment. The function takes in your grade and number of days late from today and takes off 2% per day. For example calculateGrade(75, 10) would return 55. calculateGrade(65, 0) would return 65 and calculateGrade(20, 100) would return 0.

def calcGrade(grade, daysLate):
  finalGrade = grade - (daysLate * 2)
  if finalGrade > 0:
    return finalGrade
  else:
    finalGrade = 0
    return finalGrade

grade = int(input('What is your percentage grade: '))
daysLate = int(input('How many days late: '))
print(calcGrade(grade, daysLate))

assert calcGrade(75, 10) == 55
assert calcGrade(65, 0) == 65

# FIX RETURN 2. write a function called levelGrade(numberGrade) that given number grade, it prints and returns the corresponding level grade for that. For example levelGrade(91) would return 4. levelGrade(71) would return 3

#WIP fix return
def levelGrade(numberGrade):
  if numberGrade >= 91:
    return 4
  if numberGrade >= 71 and numberGrade < 91:
    return 3
  if numberGrade >= 60 and numberGrade < 71:
    return 2
  if numberGrade <= 50 and numberGrade < 60:
    return 1

numberGrade = int(input('What is your percentage grade: '))
print(levelGrade(numberGrade))
    
# 3. Write a function called differenceOfEvenAndOdd(list) that takes in a list of numbers and calculate the difference between the sum of even numbers and the sum of odd numbers. For example differenceOfEvenAndOdd([1,2,5,2]) would return -2 because the sum of even numbers is 2+2 = 4 and the sum of odd number is 1+5 = 6. 4 - 6 = -2

#append even and odd numbs from orgiinal list into two new lists. add sum of both then subtract the sums

def differenceOfEvenAndOdd(list):
  i = 0
  ieven = 0
  iodd = 0
  evenNum = 0
  oddNum = 0
  evenNumbs = []
  oddNumbs = []
  evenSum = 0
  oddSum = 0
  while i < len(list):
    for num in list:
      if num % 2 == 0:
        evenNumbs.append(num)
        i += 1
      else:
        oddNumbs.append(num)
        i += 1
  while ieven < len(evenNumbs):
    for evenNum in evenNumbs:
      evenSum = evenSum + evenNum
      ieven += 1
  while iodd < len(oddNumbs):
    for oddNum in oddNumbs:
      oddSum = oddSum + oddNum
      iodd += 1
  return print(f'The difference is ' + str(evenSum - oddSum))

list = [1,2,5,2]
differenceOfEvenAndOdd(list)