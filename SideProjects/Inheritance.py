#todo Code for demonstrating Inheritance from parent classes
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

#Inherits attributes from parent class (class Person)
class Worker(Person):

    def __init__(self, name, age, height, salary):
        # Inherits the constructor function from the Parent class
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        # Inherits __str__ function from class Person
        text = super(Worker, self).__str__()
        #Adds the following text to the string format
        text += ", Salary: {}".format(self.salary)
        return text

    def calc_yearly_salary(self):
        return self.salary * 12

worker1 = Worker("Henry", 40, 6.0, 3000)
print(worker1)
print(worker1.calc_yearly_salary())

# Inherits attributes from parent class (in this case: class Worker)
class Programmer(Worker):

    def __init__(self, name, age, height, salary, fav_code_language):
        super(Programmer, self).__init__(name, age, height, salary)
        self.fav_code_language = fav_code_language

programmer1 = Programmer("Isaac", 17, 5.11, 10000, "Python")
print(programmer1)
print(programmer1.calc_yearly_salary())

#todo Code for Operator Overloading demonstrated using Vectors
"""
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): #other being the answer to said equation/operations
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "X: {} Y: {}".format(self.x, self.y)

v1 = Vector(2, 5)
v2 = Vector(6, 3)

print(v1)
print(v2)

v3 = (v1 + v2)
v4 = (v1 - v2)

print("Addition Result: " + str(v3))
print("Subtraction Result: " + str(v4))
"""