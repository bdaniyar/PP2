class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Example 2
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

#Example 3
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
  
#Example 4
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
