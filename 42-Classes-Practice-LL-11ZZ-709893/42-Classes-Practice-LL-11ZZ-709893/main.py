class Student:
  def __init__(self, firstName, lastName, age, grades, studentNumber):
    self.__firstName = firstName
    self.__lastName = lastName
    self.__age = age
    self.__grades = grades
    self.__studentNumber = studentNumber

  def __str__(self):
    return str(self.__lastName) + ", " + str(self.__firstName) + ': ' + str(self.__studentNumber)

  #setters and getters
  def setFirstName(self, newName):
    self.__firstName = newName

  def getFirstName(self):
    return self.__firstName
  
  #calculate aveage of student
  def average(self):
    count = 0
    for i in self.__grades.values():
      count += 1
    avg = round(sum(self.__grades.values()) / count)
    return avg

  #my custom method
  def legalToDrink(self):
    if self.__age >= 19:
      return (f"{self.__firstName} is old enough to drink, they are {self.__age} years old.")
    else:
      self.__reqYears = 19 - self.__age
      return (f"{self.__firstName} is not old enough to drink, they are just {self.__age} years old. They have {self.__reqYears} years left until being able to do so.")
      
#compare highest average of 2 students and return highest
  def compareAverage(self, other):
    a = self.average()
    b = other.average()
    if a > b:
      return str(self.__firstName) + " " + str(self.__lastName) + ' has the highest average: ' + str(a)
    elif a < b:
      return str(other.__firstName) + " " + str(other.__lastName) + ' has the highest average: ' + str(b)
    else:
      return str(self.__firstName) + " " + str(self.__lastName) + " & " + str(other.__firstName) + " " + str(other.__lastName) + ' have the same average: ' + str(a)

  #return if student hasx passing mark
  def isPassing(self):
    if self.average() >= 50:
      return True
    else:
      return False

#student grades as dictionaries 
billNyeGrades = {
  'Functions' : 0,
  'Science' : 100,
  'English' : 10,
  'Geography' : 0,
}

abdulGrades = {
  'Functions' : 50,
  'Computer Science' : 100,
  'English' : 60,
  'Calculus' : 5,
}

leeGrades = {
  'Functions' : 100,
  'Computer Science' : 100,
  'English' : 100,
  'Geography' : 100,
}

einsteinGrades = {
  'Physics' : 9000,
  'Computer Science' : 70,
  'English' : 91,
  'Adanced Functions' : 800,
}

#objects/instances of students
p1 = Student('Bill', 'Nye', 55, billNyeGrades, 238944)
p2 = Student('Abdul', 'Ajibodu', 16, abdulGrades, 982783)
p3 = Student('Lee', 'Xiu', 21, leeGrades, 123089)
p4 = Student('Albert', 'Einstein', 146, einsteinGrades, 000000)

print(p1)
print(p1.average())

print(p2)
print(p2.average())

print(p3)
print(p3.average())

print(p4)
print(p4.average())

print('')

print(p1.compareAverage(p2))
print(p2.compareAverage(p3))
print(p3.compareAverage(p4))

print(p1.isPassing())
print(p2.isPassing())
print(p4.legalToDrink())
print(p2.legalToDrink())