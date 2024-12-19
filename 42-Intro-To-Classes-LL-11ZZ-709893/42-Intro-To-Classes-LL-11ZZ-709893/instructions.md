# Instructions  

Today we look at our last complex data type, Classes. Classes in programming are a way for us to store a concept that a programming language does not understand. For python knows what integers, booleans, floats, etc are but it has no concept of a person. We know a person has a name, an age, height, eye color, and many more attributes but python knows none of this. However we can create the person data type by making it a class. Below is the base structure of a class in python.

```Python

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

```

This creates a class called person and allows us to do


```Python

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

p1 = Person('Bob', 18)

```

This creates a person with the name Bob and the age 18. The self parameter here is a reference to the object being created, and while is the first parameter in the __init__ function, it does not take the first position when you call the function. If we print this person we will see <__main__.Person object at 0x7f67faac9ba8>

```Python

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

p1 = Person('Bob', 18)
print(p1)
```


This is the memory address of the person created. In other words, where does this person exist in memory on your device. In order to have the class print something useful we will need to define the __str__ method

```Python

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def __str__(self):
        return "(" + self.name + "," + str(self.age) + ")"
      
p1 = Person('Bob', 18)
print(p1)
```

__str__ tells python how to print the class. Now you might have noticed how I said method and not function despite using the def keyword. That is because functions within a class are considered methods (think back to when we looked at string methods. They were not called functions). Methods allow us to access, use and update the class. In python you can access attributes (name and age in this example) however in other languages you cannot. You need to specifically create methods to access the values.

```Python

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def __str__(self):
        return "(" + self.name + "," + str(self.age) + ")"

    def getName(self):
      return self.name

    def setName(self, newName):
      self.name = newName

    def getAge(self):
      return self.age

    def setAge(self, val):
      self.age = val
      
p1 = Person('Bob', 18)

# this works but should not be done
print(p1.age)


# this is how it should be done
print(p1.getAge())
```


Methods can also access and change attributes in different ways

```Python

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def __str__(self):
        return "(" + self.name + "," + str(self.age) + ")"

    def getName(self):
      return self.name

    def setName(self, newName):
      self.name = newName

    def getAge(self):
      return self.age

    def setAge(self, val):
      self.age = val

    def birthday(self):
      self.age += 1
      
p1 = Person('Bob', 18)

print(p1)

# increases age by one
p1.birthday()

print(p1)
```

we can also compare objects

```Python

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def __str__(self):
        return "(" + self.name + "," + str(self.age) + ")"

    def getName(self):
      return self.name

    def setName(self, newName):
      self.name = newName

    def getAge(self):
      return self.age

    def setAge(self, val):
      self.age = val

    def birthday(self):
      self.age += 1

    def compareAge(self, other):
      if self.age > other.age:
        print(f'{self.name} is older than {other.name} by {self.age - other.age}')
      elif self.age < other.age:
        print(f'{other.name} is older than {self.name} by {other.age - self.age}')
      else:
        print(f'{self.name} and {other.name} are the same age!')
        
p1 = Person('Bob', 18)
p2 = Person('Tom', 20)
p3 = Person('Tod', 18)

p1.compareAge(p2)
p3.compareAge(p1)
```


Make sure all attributes are in the init funtion or else they will be shared among all people created. For example

```Python

class Person:

    pets = []
  
    def __init__(self, name, age):
        self.age = age
        self.name = name
      
    def __str__(self):
        return "(" + self.name + "," + str(self.age) + ")"

    def getPets(self):
      return self.pets
  
    def addPet(self, name):
      self.pets.append(name)

   
        
p1 = Person('Bob', 18)
p2 = Person('Tom', 20)
p3 = Person('Tod', 18)

p1.addPet('Buddy')

print(p1.getPets())

p2.addPet('Shadow')

print(p2.getPets())
print(p3.getPets())
```

by simply putting the pets list in the init we solve this problem

```Python

class Person:
  
    def __init__(self, name, age):
        self.age = age
        self.name = name
        # set to empty on creation as there is no pet parameter in the init
        self.pets = []
  
    def __str__(self):
        return "(" + self.name + "," + str(self.age) + ")"

    def getPets(self):
      return self.pets
  
    def addPet(self,name):
      self.pets.append(name)

   
        
p1 = Person('Bob', 18)
p2 = Person('Tom', 20)
p3 = Person('Tod', 18)

p1.addPet('Buddy')

print(p1.getPets())

p2.addPet('Shadow')

print(p2.getPets())
print(p3.getPets())
```

Lets look at an other class example

```Python


class Animal:
  def __init__(self, name, age, type, owner = ''):
        self.age = age
        self.name = name
        self.type = type
        self.owner = owner
        # 0 not hungry, 10 is starving
        self.hungerLevel = 0
        # 10 Super happy, 0 will run away
        if owner != '':
          self.happinessLevel = 10
        else:
          self.happinessLevel = 5
    

```

how might getters and setters look for this class? What could be a method look like for this animal? what could a fetch method look like? what about a feed method?


Consider the following code

```Python
class Animal:
  def __init__(self, name, age, type, owner = ''):
        self.age = age
        self.name = name
        self.type = type
        self.owner = owner
        # 0 not hungry, 10 is starving
        self.hungerLevel = 0
        # 10 Super happy, 0 will run away
        if owner != '':
          self.happinessLevel = 10
        else:
          self.happinessLevel = 5


animal1 = Animal('Bob', 3, 'dog')
animal2 = Animal('Tim', 8, 'cat', 'Alex')

print(animal1)
print(animal1.happinessLevel)
print(animal2.happinessLevel)
```

What would each print line give us? What is missing in the class? How could we write a method related to happiness?

I will go one step further and make happinessLevel a protected Attribute. Private attributes cannot be access outside of the class

```Python
class Animal:
  def __init__(self, name, age, type, owner = ''):
        self.age = age
        self.name = name
        self.type = type
        self.owner = owner
        # 0 not hungry, 10 is starving
        self.hungerLevel = 0
        # 10 Super happy, 0 will run away
        if owner != '':
          self.__happinessLevel = 10
        else:
          self.__happinessLevel = 5


animal1 = Animal('Bob', 3, 'dog')
animal2 = Animal('Tim', 8, 'cat', 'Alex')

print(animal1)
print(animal1.__happinessLevel)
print(animal2.__happinessLevel)
```

Python will still give you access to the attribute directly but it should be avoided. All protected attributes should never be accessed outside of methods. It is good practice to make all attributes private

```Python
class Animal:
  def __init__(self, name, age, type, owner = ''):
        self.__age = age
        self.__name = name
        self.__type = type
        self.__owner = owner
        # 0 not hungry, 10 is starving
        self.__hungerLevel = 0
        # 10 Super happy, 0 will run away
        if owner != '':
          self.__happinessLevel = 10
        else:
          self.__happinessLevel = 5

  def __str__(self):
    return f'{self.__name} is a {self.__type}. They are are {self.howHappy()}'

  def howHappy(self):
    if self.__happinessLevel == 10:
      state = 'amazing'
    elif self.__happinessLevel >= 7:
      state = 'happy'
    elif self.__happinessLevel >= 3:
      state = 'ok'
    elif self.__happinessLevel >= 0:
      state = 'sad'
    return state


animal1 = Animal('Bob', 3, 'dog')
animal2 = Animal('Tim', 8, 'cat', 'Alex')

print(animal1)
print(animal1.howHappy())
print(animal2.howHappy())
```