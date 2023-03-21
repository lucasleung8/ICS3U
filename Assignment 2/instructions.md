# Instructions  

Write a program that asks for 2 names and a dice size (one of 4,6,8,10,12,20). If the names are not your name and "Marco" then print, "Please use {your name} and Marco for the names" (you MUST use AND here). If the dice size is valid (one of 4,6,8,10,12,20) print "Valid dice" else print "Invalid dice".

Only if names and dice are valid generate 2 random numbers from 1-dice size. If you win print "You win because x is bigger than y" where x is your roll and y is my roll. If you lose print "Mr. Marco wins because y is bigger than x" where x is your roll and y is my roll. If both rolls are tied print "Its a tie! Because x is equal to y" where x is your roll and y is my roll. If Mr. Marcos roll on the dice is the highest possible a 4 on 4 sided, 6 on a 6 sided, 8 on 8 sided... Then print "Mr Marco rolled a {number} he automatically wins."

You must use the following for full marks
* or
* and
* match/case
* String formating
* The random library
* if, elif and else
* Comments


If you feel like the assignment it not enough to hit all the requirements, add as much as you think is needed to mean the requirements.

Below are sample input and outputs assuming a student is named Tom

```
Give me a name Marco
Give me your name Tom
Dice size? 12
Valid dice
Tom rolled a 9, Marco rolled a 3. Tom wins!
```

```
Give me a name Justin
Give me your name Aryton
Dice size? 12
Valid dice
Please use Tom and Marco for the names
```

```
Give me a name Marco
Give me your name Tom
Dice size? 20
Valid dice
Tom rolled a 12, Mr Marco rolled a 17. Mr Marco wins!
```

```
Give me a name Marco 
Give me your name Miller
Dice size? 12
Valid dice
Please use Tom and Marco for the names
```

```
Give me a name Marco
Give me your name Tom
Dice size? 4
Valid dice
Tom rolled a 3, Marco rolled a 3. It's a tie!
```

```
Give me a name Marco 
Give me your name Tom
Dice size? 13
Invalid dice
```

```
Give me a name Marco 
Give me your name Tom
Dice size? 20
Valid dice
Mr Marco rolled a 20 he automatically wins.
```
