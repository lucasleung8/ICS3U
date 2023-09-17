
#part 1 - asks for 3 numbers and checks if third number is between first and second number
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
if (num3 < num2 and num3 > num1):
  print(f'{num3} is between {num1} and {num2}')
  print('')
else:
  print(f'{num3} is not between {num1} and {num2}')
  print('')

#part 2 - greets people, different greetings depending on the name inputted
name = input('What is your name?: ').capitalize()
if name == 'Biden':
  print('Welcome, Mr. President')
elif name == 'Aubrey' or name == 'Mari' or name == 'Kel' or name == 'Sunny':
  print(f'how are ya, {name}')
elif name == 'Miller' or name == 'Adam' or name == 'Gurpreet':
  print(f'Hello there, {name}.')
elif name == 'Niko':
  print(f'Hey {name} o/')
else:
  print('Sorry I dont know you')

#part 3 - asks for a name and check if it contains all the letters of my name
secondName = input('Choose another first name: ').lower()

if 'l' in secondName and 'u' in secondName and 'c' in secondName and 'a' in secondName and 's' in secondName:
  print('Are you trying to commit identity theft?')
else:
  print('You are not Lucas')