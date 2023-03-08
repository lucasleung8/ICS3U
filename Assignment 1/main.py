#Multipurpose calculator created By Lucas Leung for ICS3U course, TLK S.S., Feb 24 2023
#time for waiting https://docs.python.org/3/library/time.html
#random num https://docs.python.org/3/library/random.html

import math
import time
import random

#language selection for the user 
lang = 0

print('Choose your preferred language')
print('1 = English')
print('2 = Francais/French')
lang = int(input(''))

#english selection
if lang == 1:
  #introduction of program functions to user
  name = input(f'You chose option {lang}. Hello! What is your name? ')
  print(' ')
  print('Welcome, ' + name + '! This program is a random number generator, magic 8ball, squareroot calculator and factorial finder all in one.')
  print(' ')
  time.sleep(2)
  print("We'll start with choosing a random number. Then, use the 8ball. After you can find the squareroot of a number. Lastly, the factorial.")
  print(' ')
  time.sleep(2)
  #generate random number integer
  minNum = int(input('Before generating a random number, we need to know the range. What is the smallest number you want to allow? '))
  maxNum = int(input('What is the largest number you want to allow? '))
  randomNum = random.randint(minNum, maxNum)
  print (f'You selected the range of {minNum} to {maxNum}. {randomNum} is your random number!')
  print(' ')
  #user asks question for magic 8ball
  ballQuestion = input('What is your queston for the 8ball? ')
  print(f'Ill shake the 8ball now and ask it {ballQuestion}.')
  print(' ')
  print('Let me see what the 8ball says. Just a sec...')
  print('.')
  time.sleep(1)
  print('.')
  time.sleep(1)
  print('.')
  time.sleep(1)
  print(f'In response to {ballQuestion}, the 8ball says it is certain.')
  print('')
  #find squareroot of chosen number
  sqrtRequested = int(input('Enter a number to find the squareroot of it: '))
  sqrtAns = math.sqrt(sqrtRequested)
  print(f'The squareroot of {sqrtRequested} is {sqrtAns}')
  #find factorial of number
  factorialNum = int(input('Enter a number to find the factorial: '))
  factorialAns = math.factorial(factorialNum)
  print(f'The factorial of {factorialNum} is {factorialAns}.')
  #final part of program, asking for user feedback.
  feedback = input('Lastly how would you rate your experience? Id love to hear feedback. ')
  print(f'Your feedback: "{feedback}" is appreciated.')
  print(f'Thanks for using this program {name} :)')


#french selection
if lang == 2:
  #introduction of program to user
  name = input(f"Vous avez choisi l'option {lang}. Bonjour! Quel est ton nom? ")
  print(' ')
  print('Bienvenue, ' + name + '! Ce programme est un générateur de nombres aléatoires, une boule magique 8, une calculatrice de racine carrée et un chercheur factoriel tout en un.')
  print(' ')
  time.sleep(2)
  print("Nous allons commencer par choisir un nombre aléatoire. Ensuite, une boule 8. Après vous pouvez trouver la racine carrée d'un nombre. Enfin, trouvez la factorielle d'un nombre.")
  print(' ')
  time.sleep(2)
  #generate random number integer
  minNum = int(input('Avant de générer un nombre aléatoire, nous devons connaître la plage. Quel est le plus petit nombre que vous souhaitez autoriser ? '))
  maxNum = int(input('Quel est le plus grand nombre que vous souhaitez autoriser ? '))
  randomNum = random.randint(minNum, maxNum)
  print (f'Vous avez sélectionné la plage de {minNum} entre {maxNum}. {randomNum} est votre nombre aléatoire !')
  print(' ')
  #user asks question for magic 8ball
  ballQuestion = input('Quelle est votre question pour la boule 8 ? ')
  print(f'Je vais secouer la boule 8 maintenant et lui demander {ballQuestion}')
  print(' ')
  print('Laissez-moi voir ce que dit la boule 8. Juste une seconde...')
  print('.')
  time.sleep(1)
  print('.')
  time.sleep(1)
  print('.')
  time.sleep(1)
  print(f'En réponse à {ballQuestion}, la boule 8 dit que cest certain.')
  print('')
  #find squareroot of chosen number
  sqrtRequested = int(input('Entrez un nombre pour en trouver la racine carrée: '))
  sqrtAns = math.sqrt(sqrtRequested)
  print(f'La racine carrée de {sqrtRequested} est {sqrtAns}')
  #find factorial of number
  factorialNum = int(input('Entrez un nombre pour trouver la factorielle: '))
  factorialAns = math.factorial(factorialNum)
  print(f'La factorielle de {factorialNum} est {factorialAns}.')
  #final part of program, asking for user feedback.
  feedback = input('Enfin, comment évaluez-vous votre expérience ? Jaimerais entendre des commentaires.')
  print(f'Vos réactions: "{feedback}" est apprécié.')
  print(f'Merci pour utiliser cette program {name} :)')