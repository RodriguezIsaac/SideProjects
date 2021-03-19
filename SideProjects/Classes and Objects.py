#todo Code for creating a object within a class
"""
class Person:

    #Function to create an object/assign attributes (constructor)
    def __init__(self):
        self.name = "Mike"
        self.age = 25

person1 = Person()

print(person1.name)
print(person1.age)
"""

#todo Code for creating & editing multiple Objects within a class
'''
class Person:

    def __init__(self, name, age, height): #Parameters. Allows for diversity per Object
        self.name = name
        self.age = age
        self.height = height

#Object One
person1 = Person("Mike", 25, 5.7) #Name, Age, Height
print("Hi, my name is " + person1.name)
print("Age: " + str(person1.age))
print("Height: " + str(person1.height))

#Object 2
person2 = Person("Sera", 21, 5.4)
print(person2.name)
print(person2.age)
print(person2.height)

#Values for Objects can be Changed
person2.name = "Abby"
print(person2.name)
'''

#todo Code for the use of Different Functions/Methods within a class
class Person:

    population = 0 #Class variable. A value applied to all objects within the class

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.population += 1 #Adds 1 to the population if a object is created

    #Function that Determines what happens when trying to print an object. Ex: print(person1)
    def __str__(self):
        #Fills in the place holders with the stated info in the format
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    #Fuction that Determines what happens when an Object or value is deleted (destructor)
    def __del__(self):
        print("Object Deleted")
        Person.population -= 1 #Subtracts 1 from the population when an object is deleted


#Object One
person1 = Person("Mike", 25, 5.7) #Name, Age, Height

#Object 2
person2 = Person("Sera", 21, 5.4)

del person2 #Works with __del__ function

print(person1) #Works with __str__ Function

print(Person.population)