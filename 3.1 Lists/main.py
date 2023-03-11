#1 - greets people, different greetings depending on the name inputted
presidentNames = ['Biden']
omoriNames = ['Aubrey', 'Mari', 'Kel', 'Sunny']
genericNames = ['Miller', 'Adam', 'Gurpreet']
oneShotNames = ['niko', 'Niko', 'Cedric', 'Silver', 'Alula']

name = input('What is your name?: ').capitalize()

if name in presidentNames:
  print('Welcome, Mr. President\n')
elif name in omoriNames:
  print(f'how are ya, {name}\n')
elif name in genericNames:
  print(f'Hello there, {name}.\n')
elif name in oneShotNames:
  print(f'Hey {name} o/\n')
else:
  print('Sorry I dont know you\n')

#2 asks for input and returns the index of an item if in the list and "{item} is not in the list" if its not there

iceCreamFlavor = input('Whats your favurite icecrema: ')
iceCreamFlavorList = ['chocolate', 'strawberry', 'vanilla', 'caramel', 'neopolitan']

if iceCreamFlavor in iceCreamFlavorList:
  indexNum = iceCreamFlavorList.index(iceCreamFlavor)
  print (f'{iceCreamFlavor} is at index {indexNum}\n')
else:
  print(f'{iceCreamFlavor} is not in the list\n')

# 3 Write a program that asks for 5 numbers. Create a list from those 5 numbers and then sort that list. Print the sorted list.

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))
num4 = int(input('Enter a number: '))
num5 = int(input('Enter a number: '))

numList = [num1, num2, num3, num4, num5]
numList.reverse()
numList.sort()
print('Reversed and sorted: \n')
print(numList)