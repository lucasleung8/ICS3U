#ask user for first number
firstNum = int(input('In this program I will check if a number is greater than 10. Provide a number: '))

#first number comparison
if(firstNum > 10):
  print(f'Yes, {firstNum} is greater than 10.')
elif(firstNum < 10):
  print(f'No, {firstNum} is less than 10.')
elif(firstNum == 10):
  print(f'{firstNum} is equal to 10.')

#second number comparison to first number
secondNum = int(input(f'I will compare a second number to your first number, {firstNum}: '))
if(secondNum) > (firstNum):
  print(f'Yes, {secondNum} is greater than {firstNum}.')
elif(secondNum) < (firstNum):
  print(f'No, {secondNum} is less than {firstNum}.')
elif(secondNum) == (firstNum):
  print(f'{secondNum} is equal to {firstNum}.')

#asks for text input, fav fruit, and provides 4 diff responses
fruit = input('Enter your favourite fruit and I will tell you the nutritional info about it: ')
if fruit == 'apple' or 'apples':
  print('https://www.hsph.harvard.edu/nutritionsource/food-features/apples/')
elif fruit == 'banana' or 'bananas':
  print('https://www.hsph.harvard.edu/nutritionsource/food-features/bananas/')
elif fruit == 'strawberry' or 'strawberries':
  print('https://www.healthline.com/nutrition/foods/strawberries')
elif fruit == 'blueberry' or 'blueberries':
  print('https://www.webmd.com/diet/health-benefits-blueberries')
else:
  print('Sorry, unrecognized fruit.')