#Note i added time by following this in the doc https://docs.python.org/3/library/time.html

import time
from time import strftime

#Asks your for your name, then your student number, then which classes you are taking. After all the information is collected print a string for each that makes use of string formating.

name = input('What is your name?')

studentNumber = input('What is your student number?')

school = input('Whats your school?')

class1 = input('What is your first class?')
class2 = input('What is your second class?')
class3 = input('What is your third class?')
class4 = input('What is your fourth class?')

time.sleep(0.5)
print('.')
time.sleep(0.5)
print('.')
time.sleep(0.5)
print('.')
time.sleep(0.5)
print('.')

missionTime = strftime("%a, %d %b %Y %H:%M:%S")
print(missionTime)
print('**Mission Briefing**')
print(
  f'Hello Agent {name}, ID {studentNumber}. Your objective today is an ordinary yet important one: learn, and gather documents referred to as "homework". Our intel assessments indicate practically no risk. Your destination is {school}. It is imperative to head to {class1} from 8:30AM to 9:45AM. Then, {class2} from 9:48 to 11:03. After lunch, you need to attend {class3} from 12:03 to 1:18. Finally, you must visit {class4} from 1:21 until 2:36, then you can head for an exit.'
)

print('    ')

#Asks you what is your favorite hobby, then when did you start doing it, then how good you are at it. After have the program print out 3 responses that use the inputed value

favoriteHobby = input('Whats your favorite hobby?')
startHobby = input(f'When did you start doing {favoriteHobby}?')
skillHobby = input(f'How good are you at {favoriteHobby}?')

print(f'Interesting, never heard of {favoriteHobby} before. Its impressive that your skill level is {skillHobby}. {startHobby} feels like such a long time ago.')
print('     ')