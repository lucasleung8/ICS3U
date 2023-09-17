#  1. Write a Python function to add a key to a dictionary only if it does not exist. for example

def addKey(dict, key, value):
    if key not in dict.keys():
      dict[key] = value
    newDictionary = dict
    return newDictionary
  
d = {'a': 300,
     'b': 200}

newDictionary = addKey(d, 'c', 100)
print(newDictionary)

  #2. Write a Python function to get the maximum and minimum value in a dictionary. This function should return a dictionary with the keys min and max

def getMinMax(d):
  max = list(d.values())[0]
  min = list(d.values())[0]
  dict = {}
  for num in d.values():
    if max <= num:
      max = num
    if min >= num:
      min = num
  dict['max'] = max
  dict['min'] = min
  return dict

d = {'a': 300, 'b': 200, 'c': 100, 'd': 999}
result = getMinMax(d)
print(result)


# 3. Write a function to count every instance of each character in a string. Return a dictionary with all the values.
def countCharacters(myString):
  result = {}
  for letter in myString.lower():
    if letter in result.keys():
      result[letter] += 1
    else:
      result[letter] = 1
  return result

result = countCharacters('Hello Class how it it going')
print(result)

#  4. Convert two lists into a dictionary. Both list are guarenteed to be the same size with no duplicate keys. for example

def combine(keys, values):
  finalDict = {}
  iii = 0
  while iii < len(keys):
    keyInt = keys[iii]
    valueInt = values[iii]
    finalDict[keyInt] = valueInt
    iii += 1
  return finalDict
  
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = combine(keys, values)
print(result)

# car = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# for key in car.keys():
#   print(key) #key
#   print(car[key]) #value associtate with key