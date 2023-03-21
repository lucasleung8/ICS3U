import random

#initliaze variables
replay = 1

while replay == 1: #allows game to be replayed
  #start game if user chooses y. ends game if n is chosen
  playChoice = input('Do you want to play, y/n: ')
  if playChoice == ('y') or playChoice == ('Y'):
    teacherName = input('Enter a name: ').capitalize()
    myName = input('Enter your name: ').capitalize()
    diceSize = int(input('Choose a dice size (one of 4,6,8,10,12,20): '))
    #check if selected dice size is correct, return error if invalid
    match diceSize:
      case 4:
        if (myName == 'Lucas') and (teacherName == 'Marco'):
          #dice size & both names are correct. roll 4-sided dice & determine game outcome
          teacherDiceRoll = random.randint(1,4)
          myNameDiceRoll = random.randint(1,4)
          print('Valid dice size')
          if (teacherDiceRoll > myNameDiceRoll) and (teacherDiceRoll != myNameDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {teacherName} won!')
            replay = 1
          elif (myNameDiceRoll == teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. Its a tie!')
            replay = 1
          elif (myNameDiceRoll > teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {myName} won!')
            replay = 1
          elif (teacherDiceRoll == 4):
            print(f'{teacherName} rolled {teacherDiceRoll}, he automatically wins!')
            replay = 1
        
        #if both names are not Lucas and Marco, return error
        elif (myName != 'Lucas') and (teacherName == 'Marco'):
            print(f'Please use Lucas. {teacherName} is correct.\n')
            replay = 1
        elif (myName == 'Lucas') and (teacherName != 'Marco'):
            print(f'Please use Marco. {myName} is correct.\n')
            replay = 1
        else:
          print(f'Please use Lucas and Marco for the names\n')
          replay = 1
          
      case 6:
        print('Valid dice size')
        if (myName == 'Lucas') and (teacherName == 'Marco'):
         #roll 6-sided dice & determine game outcome
          teacherDiceRoll = random.randint(1,6)
          myNameDiceRoll = random.randint(1,6)
          if (teacherDiceRoll > myNameDiceRoll) and (teacherDiceRoll != myNameDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {teacherName} won!')
            replay = 1
          elif (myNameDiceRoll == teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. Its a tie!')
            replay = 1
          elif (myNameDiceRoll > teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {myName} won!')
            replay = 1
          elif (teacherDiceRoll == 6):
            print(f'{teacherName} rolled {teacherDiceRoll}, he automatically wins!')
        
        #if two chosen names are incorect, print error
        elif (myName != 'Lucas') and (teacherName == 'Marco'):
          print(f'Please use Lucas. {teacherName} is correct.\n')
          replay = 1
        elif (myName == 'Lucas') and (teacherName != 'Marco'):
          print(f'Please use Marco. {myName} is correct.\n')
          replay = 1
        else:
          print(f'Please use Lucas and Marco for the names\n')
          replay = 1
      
      case 8:
        print('Valid dice size')
        if (myName == 'Lucas') and (teacherName == 'Marco'):
          #roll 8-sided dice & determine game outcome
          teacherDiceRoll = random.randint(1,8)
          myNameDiceRoll = random.randint(1,8)
          if (teacherDiceRoll > myNameDiceRoll) and (teacherDiceRoll != myNameDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {teacherName} won!')
            replay = 1
          elif (myNameDiceRoll == teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. Its a tie!')
            replay = 1
          elif (myNameDiceRoll > teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {myName} won!')
            replay = 1
          elif (teacherDiceRoll == 4):
            print(f'{teacherName} rolled {teacherDiceRoll}, he automatically wins!')
            replay = 1
            
        #if two chosen names are incorect, print error
        elif (myName != 'Lucas') and (teacherName == 'Marco'):
          print(f'Please use Lucas. {teacherName} is correct.\n')
          replay = 1
        elif (myName == 'Lucas') and (teacherName != 'Marco'):
          print(f'Please use Marco. {myName} is correct.\n')
          replay = 1
        else:
          print(f'Please use Lucas and Marco for the names\n')
          replay = 1
      
      case 10:
        print('Valid dice size')
        if (myName == 'Lucas') and (teacherName == 'Marco'):
          #roll 10-sided dice & determine game outcome
          teacherDiceRoll = random.randint(1,10)
          myNameDiceRoll = random.randint(1,10)
          if (teacherDiceRoll > myNameDiceRoll) and (teacherDiceRoll != myNameDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {teacherName} won!')
            replay = 1
          elif (myNameDiceRoll == teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. Its a tie!')
            replay = 1
          elif (myNameDiceRoll > teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {myName} won!')
            replay = 1
          elif (teacherDiceRoll == 10):
            print(f'{teacherName} rolled {teacherDiceRoll}, he automatically wins!')
            replay = 1
        
        #if two chosen names are incorect, print error
        elif (myName != 'Lucas') and (teacherName == 'Marco'):
          print(f'Please use Lucas. {teacherName} is correct.\n')
          replay = 1
        elif (myName == 'Lucas') and (teacherName != 'Marco'):
          print(f'Please use Marco. {myName} is correct.\n')
          replay = 1
        else:
          print(f'Please use Lucas and Marco for the names\n')
          replay = 1
      
      case 12:
        print('Valid dice size')
        if (myName == 'Lucas') and (teacherName == 'Marco'):
          #roll 12-sided dice & determine game outcome
          teacherDiceRoll = random.randint(1,12)
          myNameDiceRoll = random.randint(1,12)
          if (teacherDiceRoll > myNameDiceRoll) and (teacherDiceRoll != myNameDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {teacherName} won!')
            replay = 1
          elif (myNameDiceRoll == teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. Its a tie!')
            replay = 1
          elif (myNameDiceRoll > teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {myName} won!')
            replay = 1
          elif (teacherDiceRoll == 12):
            print(f'{teacherName} rolled {teacherDiceRoll}, he automatically wins!')
            replay = 1
        
        #if names are incorect, print error
        elif (myName != 'Lucas') and (teacherName == 'Marco'):
          print(f'Please use Lucas. Marco is correct.\n')
          replay = 1
        elif (myName == 'Lucas') and (teacherName != 'Marco'):
          print(f'Please use Marco. {myName} is correct.\n')
          replay = 1
        else:
          print(f'Please use Lucas and Marco for the names\n')
          replay = 1
      
      case 20:
        print('Valid dice size')
        if (myName == 'Lucas') and (teacherName == 'Marco'):
          #roll 20-sided dice & determine game outcome
          teacherDiceRoll = random.randint(1,20)
          myNameDiceRoll = random.randint(1,20)
          if (teacherDiceRoll > myNameDiceRoll) and (teacherDiceRoll != myNameDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {teacherName} won!')
            replay = 1
          elif (myNameDiceRoll == teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. Its a tie!')
            replay = 1
          elif (myNameDiceRoll > teacherDiceRoll):
            print(f'{teacherName} rolled {teacherDiceRoll}, {myName} rolled {myNameDiceRoll}. {myName} won!')
            replay = 1
          elif (teacherDiceRoll == 20):
            print(f'{teacherName} rolled {teacherDiceRoll}, he automatically wins!')
            replay = 1
        
        #print error if chosen names are incorrect
        elif (myName != 'Lucas') and (teacherName == 'Marco'):
          print(f'Please use Lucas. {teacherName} is correct.\n')
          replay = 1
        elif (myName == 'Lucas') and (teacherName != 'Marco'):
          print(f'Please use Marco. {myName} is correct.\n')
          replay = 1
        else:
          print(f'Please use Lucas and Marco for the names\n')
          replay = 1
      case _:
        print('Invalid dice. Please retry.\n')
        replay = 1
  #stop program if user chooses n when asked "Do you want to play"
  else:
    print('Got it. Quitting game')
    exit()