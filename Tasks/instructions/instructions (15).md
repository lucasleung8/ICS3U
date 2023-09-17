# Instructions  

  1. Write a Python function to add a key to a dictionary only if it does not exist. for example
```python
d = {'a': 300, 
     'b': 200}

newDictionary = addKey(d, 'c', 100)

print(newDictionary) ## would print {'a': 300, 'b': 200, 'c': 100}

newDictionary = addKey(d, 'a', 400) 
print(newDictionary) ## would print {'a': 300, 'b': 200}

```
 
  2. Write a Python function to get the maximum and minimum value in a dictionary. This function should return a dictionary with the keys min and max. For example
```python
d = {'a': 300, 'b': 200, 'c': 100}

result = getMinMax(d)

print(result) ## would print {'min': 100, 'max': 300}

```

  3. Write a function to count every instance of each character in a string. Return a dictionary with all the values.

```python

result = countCharacters('Hello Class how it it going')

print(result) ## {'h': 2, 'e': 1, 'l': 3, 'o': 3, ' ': 5, 'c': 1, 'a': 1, 's': 2, 'w': 1, 'i': 3, 't': 2, 'g': 2, 'n': 1}

```

  4. Convert two lists into a dictionary. Both list are guarenteed to be the same size with no duplicate keys. for example
```Python
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = combine(keys, values)

print(result) # would print {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
```
  