#import libraries
import random

##Task 1.

#define pay calculator function 
def calculatePay(hourlyRate, hoursPerWeek, numWeeks):
  #if any 3 parameters are negative, print error and return -1
  if (hourlyRate < 0):
    print('hourlyRate cannot be negative')
    return -1
  elif (hoursPerWeek < 0):
    print('hoursPerWeek cannot be negagtive')
    return -1
  elif (numWeeks < 0):
    print('numWeeks cannot be negative')
    return -1
  #calculate and return total amount earned
  totalPay = hourlyRate * hoursPerWeek * numWeeks
  print(f'You got paid ${totalPay} for working {hoursPerWeek} hours/week for {numWeeks} weeks')
  return totalPay

#ask user for hourly pay rate, number of hours per week worked, and weeks worked
hourlyRate = float(input('Your hourly rate: '))
hoursPerWeek = float(input('your hours per week: '))
numWeeks = float(input('number of weeks worked: '))

#use pay rate function
calculatePay(hourlyRate, hoursPerWeek, numWeeks)

#tests to ensure function returns accurate result
assert calculatePay(10, 40, 50) == 20000
assert calculatePay(100, 2, 3) == 600
assert calculatePay(1, 80, 10) == 800
assert calculatePay(40000000, 8, 52) == 16640000000
assert calculatePay(-10, 40, 50) == -1
assert calculatePay(-10, -9.4578687632412343118897987709, 912847) == -1

print('')


##Task 2.

#define second pay calculator function
def calculatePayVersion2(hourlyRate, hoursPerWeek2):
  totalHours = 0
  numWeeks = 0
  #if hourly rate is negative, print error & return -1 
  if (hourlyRate < 0):
    print('Invalid numbers, all numbers must be greater than 0')
    return -1
  else:
    #add up all hours worked and count number of weeks worked
    for i in hoursPerWeek2:
      if i > 0:
        totalHours = totalHours + i
        numWeeks += 1
      #if any hours worked are negative, print error & return -1
      else:
        print('Invalid numbers, all numbers must be greater than 0')
        return -1
    #calculate total money earned & average hours/week
    totalPay = hourlyRate * totalHours
    avgHoursPerWeek = totalHours / numWeeks
    #return total pay
    print(f'You earned ${totalPay} over {totalHours} hours of work during a {numWeeks} week period. In that time you worked an average of {avgHoursPerWeek} hours per week')
    return totalPay

#tests to ensure function returns accurate result
assert calculatePayVersion2(5, [30,50,10]) == 450
assert calculatePayVersion2(10, [20,20,20,20,20]) == 1000
assert calculatePayVersion2(0.05, [100,100,100,100,100]) == 25
assert calculatePayVersion2(677, [55,55]) == 74470
assert calculatePayVersion2(999999999999999999999999999999999999999999999999, [20,20,20,-20,20]) == -1
assert calculatePayVersion2(-420, [20,20,20,-20,20]) == -1

print('')

##Task 3.

#ask user for input
num = int(input('Give me a number: '))

#if chosen number not between 0-100, return error and ask for number again
while num < 0 or num > 100:
  print('Invalid number please give me a number between 0-100')
  num = int(input('Give me a number: '))

#pass chosen number to defined random list function
def createRandomList(num):
  listRandomNumbs = []
  count = 0
  #create list where each number is a random int and list size is equal to the input number
  while count < num:
    listRandomNumbs.append(random.randint(0, num))
    count += 1
  #print sorted list
  listRandomNumbs.sort()
  print(listRandomNumbs)

#use random list function
createRandomList(num)