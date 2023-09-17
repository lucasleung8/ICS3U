# do not delete this line
import mrMarcoMathHelp as help
# do not delete above this line

# this checks if  a number is prime
#print(help.isPrime(9))

# this will check if a number is a perfect square or not
#print(help.isSquare(16))

# ask for a number
number = int(input('Give me a number: '))

#part 1 - check if chosen number is even, a perfect square, <20, <1000, and if it is a prime number
if number % 2 == 0:
  print(f'{number} is even')
  if help.isSquare(number) == True:
    print(f'{number} is a perfect square')
    if number < 20:
      print(f'{number} is less than 20')
      if number < 1000:
        print(f'{number} is less than 1000')
      else:
        print(f'{number} is not less than 1000')
    else:
      print(f'{number} is not less than 20')
      if number < 1000:
        print(f'{number} is less than 1000')
        if help.isPrime(number) == True:
          print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
      else:
        print(f'{number} is not less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
  else:
    print (f'{number} is not a perfect square')
    if number < 20:
      print(f'{number} is less than 20')
      if number < 1000:
        print(f'{number} is less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
      else:
        print(f'{number} is not less than 1000')
    else:
      print(f'{number} is not less than 20')
      if number < 1000:
        print(f'{number} is less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
      else:
        print(f'{number} is not less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
else:
  print(f'{number} is uneven')
  if help.isSquare(number) == True:
    print(f'{number} is a perfect square')
    if number < 20:
      print(f'{number} is less than 20')
      if number < 1000:
        print(f'{number} is less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
      else:
        print(f'{number} is not less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
    else:
      print(f'{number} is not less than 20')
      if number < 1000:
        print(f'{number} is less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
      else:
        print(f'{number} is not less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
  else:
    print (f'{number} is not a perfect square')
    if number < 20:
      print(f'{number} is less than 20')
      if number < 1000:
        print(f'{number} is less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
      else:
        print(f'{number} is not less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
    else:
      print(f'{number} is not less than 20')
      if number < 1000:
        print(f'{number} is less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')
      else:
        print(f'{number} is not less than 1000')
        if help.isPrime(number) == True:
         print(f'{number} is a prime number')
        else:
          print(f'{number} is not a prime number')


#part 2 - ask for input 2 or more times, but the second input should only happen if the first passes some check

#check if user wants to access the banking system

validUsername = 'GCCA'
validPassword = 'password'
money = '1,000,000,000'

print('Hello! Connect to the SWIFT Banking System? (Y/N)')
connect = input('')
#only run if user selects yes
if connect == 'Y' or connect == 'y' or connect == 'YES' or connect == 'yes' or connect == 'yeah':
  username = input('Enter your username: ')
  #only run if username is correct
  if username == validUsername:
    print(f'{username} is correct. Enter your password: ')
    password = input('Enter your password: ')
    if password == validPassword:
      #only retrieve balance if password is correct
        print('Password correct')
        print(f'${money} is available. Sorry for the inconvenience but withdraws or deposits are currently unavailable.')
    else:
        print('Password incorrect')
  else:
    #run if username is incorrect
    print(f'{username} is incorrect')
elif connect == 'N' or connect == 'n' or connect == 'No' or connect == 'no' or connect == 'nope':
  #run if user selects no
  print('Disconnected from SWIFT Banking System. Have a good rest of your day!')
else:
  #input was not y or n
  print('Error')