#item price and tax calculatotr - WIP add 3 asserts
import math
import random

def price(itemPrice, quantity, tax):
  tax = 1 + tax/100
  total = round(((itemPrice * quantity) * tax), 2)
  print(f'${total}')

price(5, 19.99, 11)
#assert total == 110.94
#assert quantity == 5

#2 2. Write a function called diceRolls(diceSize, numDice) that takes in a dice size and a number of rolls that many dice if the dice size is one of 4, 6, 8, 10, 12, 20
def diceRolls(diceSize, numDice):
  i = 0
  match diceSize:
    case 4 | 6 | 8 | 10 | 12 | 20:
      print('valid')
      while i < numDice:
        rolled = random.randint(1, diceSize)
        print(f'{rolled} is your dice roll')
        i += 1
    case _:
      print("not valid")

diceSize = int(input('Choose dice size: '))
numDice = int(input('Choose dice roll amount: '))
diceRolls(diceSize, numDice)

#3 3. Write a function that called calculateShippingCost(weight) that takes in a weight of a package and return its price. A package costs $10 to ship plus $0.10 per pound over 10, $0.25 per per pound over 25 pounds and $0.50 per pound over 100 pounds. You need to add test cases for this

def calculateShippingCost(weight):
  cost = 0
  if weight <= 10:
    cost = 10
  #  print (f'${cost} is what your package costs to ship')
    return cost
  elif weight > 10 and weight <= 25:
    cost = 10 + (0.10 * (weight - 10))
  #  print (f'${cost} is what your package costs to ship')
    return cost
  elif weight > 25 and weight <= 100:
    cost = 10 + (0.10 * (weight - 10)) + (0.25 * (weight - 25))
  #  print (f'${cost} is what your package costs to ship')
    return cost
  else:
    cost = 10 + (0.10 * (weight - 10)) + (0.25 * (weight - 25)) + (0.50 * (weight - 100))
   # print (f'${cost} is what your package costs to ship')
    return cost

weight = int(input('Enter package weight: '))
calculateShippingCost(weight)
print (f'${cost} is what your package costs to ship')


tenPoundsOrLess = calculateShippingCost(10)
assert tenPoundsOrLess == 10

twentyfivePounds = calculateShippingCost(25)
assert twentyFivePounds == 11.5

fortyPounds = calculateShippingCost(40)
assert fortyPounds == 16.75

twoHundredPounds = calculateShippingCost(40)
assert twoHundredPounds == 122.75