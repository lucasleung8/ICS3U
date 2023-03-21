#1. Write a program that asks for input 3 times. A starting number, and end number and a 3rd number will be our multiple. Your code should print out all multiples of the 3rd number that exist between the first 2.

startNum = int(input('Enter starting number '))
endNum = int(input('Enter end number '))
multipNum = int(input('Enter multiple '))

numberList = (list(range(startNum+1, endNum+1)))
wholeNums = (list(range(0, endNum + 999)))

#print(wholeNums)
#print(numberList)

for i in numberList:
  if (i / multipNum) in wholeNums:
    print (i)
  else:
    pass

#2. Assuming a list is given and defined, write a loop to calculate the average of all the numbers in the loop. for example myList = [3, 6, 20, 1] would have an average of 7.5

myList = [3, 6, 20, 1]
avg = sum(myList) / len(myList)
print(f'{avg} is the average\n')

#3. 3. Extend the previous program to use a loop when asking for input so the user can enter the numbers they want the average for.
numInput = int(input('How many numbers to calculate the average? '))

count = 0
customNumbersList = []

while count < numInput:
  newNum = input('Enter a number: ')
  (customNumbersList.append(int(newNum)))
  count += 1

customAvg = sum(customNumbersList) / len(customNumbersList)
customAvgRounded = round(customAvg)

print(f'The avg of {customNumbersList} is {customAvg}. The rounded avg would be {customAvgRounded}')