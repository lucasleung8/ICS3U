#Write a program that asks for a number 2 seperate times. After you have given it the numbers, it should print to screen "The result is x" where x will be the sum of the 2 numbers. Hint : Look at the built in functions here: https://docs.python.org/3.10/library/functions.html. Consider using int() and str()

#https://docs.python.org/3/library/stdtypes.html
num1 = input('Enter first number:')
num2 = input('Enter second number:')
sum1 = float(num1) + float(num2)
print(f'The result is {sum1}')

#2. Extend your program from 1 to take in 2 more numbers. Assuming the 4 numbers are labeled a,b,c,d have the program print: "Your result is x" where x is (a+b)/(c+d)
num3 = input('Enter third number:')
num4 = input('Enter fourth number:')
sum2 = float(num3) + float(num4)
x = (sum1)/(sum2)

print('Your result is', x)