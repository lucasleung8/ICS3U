## do not delete this line
import mrMarcoMathHelp as help
## do not delete above this line

#1. Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
chosenNum = int(input('Calculate the sum of all numbers from 1 to a given number. Enter your desired number: '))

sum = 0
numbers = list(range(chosenNum))

for val in numbers:
  sum = sum+val+1

print(f'The sum is: {sum}')

#2 print multiplication table of a given number
secondNum = int(input('Enter another number and I will print the muliplication table for it: '))

#print multiplication table, 20 times
multiplicationList = (list(range(1, 20)))
for i in multiplicationList:
  print(i * secondNum)
  endOfList = i
#user can choose to continue the multiplication table 20 more times
else:
  choice = input('List 20 more? (y/n): ').lower()
  if choice == 'y':
    print('Continuing!')
    for i in multiplicationList:
      print((endOfList+i) * secondNum)
    else:
      print('\n')
  else:
    print('\n')

#3 display all prime numbers within a range
start = int(input('Enter start number: '))
end = int(input('Enter end number: '))

numberList = (list(range(start, end+1)))
primeNumberList = []

for num in numberList:
  if help.isPrime(num) == True:
    (primeNumberList.append(int(num)))
  else:
    placeholder = 1

print(f'Prime numbers between {start} and {end} are: ')
for i in primeNumberList:
  print(i)
else:
  exit()