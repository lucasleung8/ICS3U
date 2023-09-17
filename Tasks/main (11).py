## do not delete this line
import mrMarcoMathHelp as help
## do not delete above this line

## 1. Rewrite 3.2 Q1, Q2 and Q3 using a while loop instead of a for loop.

#Q1

chosenNum = int(input('Calculate the sum of all numbers from 1 to a given number. Enter your desired number: '))

i = 0
sum = 0
while i < chosenNum:
  i += 1
  sum = sum+i

print(f'The sum is: {sum}')

#Q2
keepPlaying = True

while keepPlaying == True:
  secondNum = int(input('Enter another number and I will print the muliplication table for it: '))
  freq = int(input('How many times should number be multiuplied?: '))

  count = 0
  while count < freq:
    count = count + 1
    print(count * secondNum)
  answer = input('Replay? y/n: ').lower()
  if answer == 'y':
    keepPlaying = True
  else:
    keepPlaying = False
    
#Q3
start = int(input('Enter start number for prime: '))
end = int(input('Enter end number for prime: '))

var = start
primeNumberList = []

while var <= end:
  var = var + 1
  if help.isPrime(var):
    (primeNumberList.append(int(var)))
  else:
    pass
print(f'Prime numbers between {start} and {end} are: ')
print(primeNumberList)

#Part 2 cube of all numbers from 1 to given number

cubedNum = 0
currentCount = 0

cubeGivenNumb = int(input(f'Cube a given number: '))

while currentCount <= cubeGivenNumb:
  currentCount = currentCount + 1
  cubedNum = currentCount ** 3
  print(f'Current Number is: {currentCount}   and the cube is {cubedNum}')

#Part 3 fibnocahci sequence
fibCount = 0
#fibonachhi terms
n = 0
n1 = -1
n2 = 1

#list [0, 1] each sequence of n is appended.

fibChosen = int(input('choose number for fibonachi sequence: '))

while fibCount <= fibChosen:
  n = n1+n2
  n1 = n2
  n2 = n
  fibCount = fibCount + 1
  print(f'The {fibCount}th number of the Fibonacci series is {n}')

###HOW IT WORKS
# -1 + 1 = 0
# n1   n2   n

# 1 + 0 = 1
# n1  n2   n

# 0 + 1 = 1
# n1  n2   n

# 1 + 1 = 2
# n1   n2  n

# 1 + 2 = 3
# n1   n2   n
  
# 2 + 3   = 5




