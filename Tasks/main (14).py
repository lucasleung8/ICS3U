#Task 1
def stringlength(myStr):
  count = 0
  for char in myStr:
    count = count + 1
  return count

print(stringlength('Hi'))
assert stringlength('Hello') == 5
assert stringlength('pneumonoultramicroscopicsilicovolcanoconiosis') == 45
assert stringlength('Kinematics') == 10
assert stringlength('Galois') == 6

#Task 2
#go through each word in list. if current word is longer than the previous word, save it as the longest. Also save the index
def longestWord(myList):
  longest = 0
  for i in myList:
    if len(i) > longest:
      longest = len(i)
      indexNum = myList.index(i)
  print(myList[indexNum])
  return longest

myList = ['Hi', 'Batman', 'bob', 'antidisestablishmentarianism']
assert longestWord(myList) == 28
assert longestWord(['No', 'Yes', 'God']) == 3
assert longestWord(['Kinematics', 'Joe']) == 10
assert longestWord(['Galois']) == 6

#Task 3 -- increment by 1 if each character is a number
def countDigits(myString):
  counter = 0
  for n in myString:
    if n.isdigit():
      counter = counter + 1
  return counter

assert countDigits('2He2llo2') == 3
assert countDigits('1337') == 4
assert countDigits('h3llo') == 1
assert countDigits('ics3u0') == 2

#Task 4 -- go backwards from string and append each character to list. then return list
def stringReversed(myString):
  cnt =0
  ii = 0
  reversed = []
  while ii < len(myString):
    cnt -= 1
    temp = myString[cnt]
    reversed.append(temp)
    ii += 1
  return "".join(reversed)

print(stringReversed('andrew'))
assert stringReversed('andrew') == 'werdna'
assert stringReversed('bob') == 'bob' 
assert stringReversed('Abdul') == 'ludbA' 

#Task 5 -- increment by 1 for each . and ! in string. also if the last character in the string does not have a period, increment by 1.
def numberofSentences(text):
  sentenceCount = 0
  sentenceCount += text.count('.')
  sentenceCount += text.count('!')
  return sentenceCount

print(numberofSentences('Hello everyone. Welcome back to class. Today we work on strings!'))
print(numberofSentences('Hello everyone. Welcome back to class. Today we work on strings! They are simple.'))
print(numberofSentences('Hello everyone. Welcome back to class.')) == 2
assert numberofSentences('This is a sentence. Idk what to write.') == 2
assert numberofSentences('Yet another sentence.') == 1
assert numberofSentences("This is a story about a man named Stanley. Stanley worked for a company in a big building where he was Employee #427. Employee #427's job was simple: he sat at his desk in Room 427 and he pushed buttons on a keyboard.") == 3

#Task 6
def stringToWords(myStr):
    myStr = myStr.lower().replace(".","").replace(",","").replace("!","").replace("?","").replace(":","").replace(";","").replace("&","").split()
    return myStr

print(stringToWords('Hello Class. Today, we will be looking at strings!'))
assert stringToWords('Hi everyone. No class today!') == ['hi', 'everyone', 'no', 'class', 'today']
assert stringToWords('another sentence. my fav drink is water & ice tea') == ['another', 'sentence', 'my', 'fav', 'drink', 'is', 'water', 'ice', 'tea']