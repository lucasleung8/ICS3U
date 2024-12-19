# Instructions  

Think of a concept you would like to create as a class. In class, we did a person, an animal, and then in the tasks, you created a student. For this assignment, you will create a class of your choice (ex., vehicle, furniture, bank account, game character, hardware component, fruit, vegetable, item, etc.). **For obvious reasons, your class cannot be Person, Animal, or Student and must be distinct from classmates near where you sit.**


- For this class, you will need to define 5 attributes and 5 methods of your choice. DONE

- Your class should have a useful print. Done 

- At least one of these attributes must be a dictionary, and at least one of the methods must LOOP over the KEYS of that dictionary.  done

- All attributes must be private and have defined getters and setters (these do not count toward the 5 methods you must write). 

- At least one of your attributes should be a string value, and you must use at least 2 string methods in your code. 

- Write 3 tests for each method. Write them as asserts outside your function. The following code is an example of how to write your tests. It is not a complete solution:

```Python

class Student:
  def __init__(self, name, grades):
    self.__name = name
    self.__grades = grades

  # returns the average of the values in self.__grades
  def average(self):
    values = self.__grades.values()
    count = 0
    for val in values:
      count += val
    return round(count/len(values), 0)

  # returns the grade of the class with the highest mark. If multiple are tied, return the first seen.
  def highestMarkGrade(self):
    values = self.__grades.values()
    return max(values)

  # returns the string of the class with the highest mark. If multiple are tied, return the first seen.
  def highestMarkClass(self):
    grades = self.__grades
    keys = grades.keys()
    highestClass = list(grades.keys())[0]
    for key in keys:
      if grades[key] > grades[highestClass]:
        highestClass = key
    return highestClass

# objects for testing
s1 = Student('Marco', {'Math': 100, 'Science': 100, 'Art': 60, 'Gym': 100})
s2 = Student('Tom', {'Math': 44, 'Science': 51, 'Art': 55, 'Gym': 98})
s3 = Student('Bob', {'Math': 65, 'Science': 30, 'Art': 100, 'Gym': 75})

# tests for average method
assert s1.average() == 90.0
assert s2.average() == 62.0
assert s3.average() == 68.0

# tests for highestMarkGrade method
assert s1.highestMarkGrade() == 100
assert s2.highestMarkGrade() == 98
assert s3.highestMarkGrade() == 100

# tests for highestMarkClass method
assert s1.highestMarkClass() == 'Math'
assert s2.highestMarkClass() == 'Gym'
assert s3.highestMarkClass() == 'Art'

```

For full marks, I need to see the following.

* 15 tests cases (3 per method)
* 5 useful methods
* proper getters and setters 
* Useful comments
* Useful attribute and variable names 
* Proper conditional statements (if/elif/else)
* Good use of a dictionary 
* The use of a for or while loop that interacts with a dictionary 
* Private attributes 
* A meaningful print statement for the class
* 2 used String methods 
* Proper and consistent naming convention used
* properly used return statements.






  