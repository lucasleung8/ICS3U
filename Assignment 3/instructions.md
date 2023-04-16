# Instructions  

1. Write a function called calculatePay(hourlyRate, hoursPerWeek, numWeeks) that takes in your hourly pay rate, the number of hours per week that you work and number of weeks that you have worked and returns your total pay before tax. If you enter a negative number for any of the 3 parameters it should print 'parameter-name cannot be negative' and return -1. otherwise the function should print 'You got paid ${x} for working {y} hours/week for {z} weeks' and return the total amount of money earned.

ex:
```
calculatePay(10, 40, 50) # returns 20000
'You got paid $20000 for working 40 hrs/week for 50 weeks'

calculatePay(100, 2, 3) # returns 600
'You got paid $600 for working 2 hrs/week for 3 weeks'

calculatePay(-10, 40, 50) # returns -1
'hourlyRate cannot be negative'

calculatePay(10, -40, 50) # returns -1
'hoursPerWeek cannot be negative'
```

2. Write a function called calculatePayVersion2(hourlyRate, hoursPerWeek) where hoursPerWeek is a list of numbers representing the hours you worked in individual weeks. For examples [20, 30, 25] would represent working 20 hours in week 1, 30 hours in week 2 and 25 hours in week 3. The function should print the following

'You earned ${x} over {y} hours of work during a {z} week period. In that time you worked an average of {n} hours per week'

Were x is the total money earned, y is the total number of hours, z is the number of weeks and n is the average hours per week. Use appropriate varables names instead of x, y, z, and n.

Your function should return the total money earned.

If any number is negative, print "Invalid numbers, all numbers must be greater than 0" and return -1.

ex:
```
calculatePayVersion2(10, [20,20,20,20,20]) # returns 1000
'You earned $1000 over 100 hours of work during a 5 week period. In that time you worked an average of 20 hours per week'

calculatePayVersion2(5, [30, 50, 10]) # returns 450
'You earned $450 over 90 hours of work during a 3 week period. In that time you worked an average of 30 hours per week'

calculatePayVersion2(10, [20,20,-20,20,20]) # returns -1
'Invalid numbers, all numbers must be greater than 0'

```

3. For this question you must ask the user for input. The input must be a number between 0 and 100. Use a while loop to ensure a valid input has been entered. Once the number is validated pass it to a function called createRandomList(num). This function will create a list where each number is a random integer and the list size is equal to the input number. The function should print and return the list sorted.

```
Give me a number 130
Invalid number please give me a number 10
[2,2,2,3,4,6,6,7,8,10]

Give me a number 3
[1,1,3]

Give me a number 5
[3,3,3,5,5]

```


For full marks you must use:
* for loop yes
* while loop yes
* comments yes
* At leaset 3 tests for Q1 and Q2 yes
* conditionals (if/else) yes
* print statements that match the format in the questions yes
* the return keyword yes
* function definitions yes 
* the random library yes
* meaningful variables names yes

For this assignment you will get a mark out of 10 for the above and a mark out of 12 from tests I will add (4 test per function). Your overall mark will be the average of these two marks.

  