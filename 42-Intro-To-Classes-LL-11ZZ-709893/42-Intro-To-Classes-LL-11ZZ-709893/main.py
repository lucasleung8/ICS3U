# Intro to Classes

# class Person:
#     def __init__(self, age, name, hairColor, socialSecurityNumber):
#         self.age = age
#         self.name = name
#         self.hairColor = hairColor
#         self.socialSecurityNumber = socialSecurityNumber
#         self.pets = []

#     def __str__(self):
#       return f'{self.name} is {self.age} years old'

#     def getAge(self):
#       return self.age

#     def getName(self):
#       return self.name

#     def getSocialSecurityNumber(self):
#       return self.socialSecurityNumber

#     def setAge(self, newAge):
#       self.age = newAge

#     def setName(self, newName):
#       self.name = newName

#     def addPet(self, petName):
#       self.pets.append(petName)

#     def listPets(self):
#       for pet in self.pets:
#         print(pet)

#     def birthday(self):
#       self.age += 1


# p1 = Person(18, 'Bob', 'Brown', 56413513)

# p1.addPet('Tom')
# p1.addPet('Shadow')
# print(p1)
# p1.birthday()
# p1.birthday()
# p1.birthday()
# print(p1)


# p2 = Person(25, 'Bob', 'Red', 6548645132)

# # p1.listPets()


# p2.listPets()


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
          self.__happinessLevel = 1
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

print(animal2)
print(animal1)
