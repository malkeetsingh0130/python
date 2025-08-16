Classes allow to group data and infomration in one unit like variables or functions

Class features

Single file per class
Or
Multiple classes can be contained in one file

Inheritance: derived/child class can use attributes and methouds of parent class

Multiple inheritance: derived/child class can inherit attributes and methods from more than one class

Polymorphism: derived/child calsses can override class methods of parent class

All clases in python are objects

Class variables: for use by all the methods in the class

instance variables: for use by the specific method in which the variable is declared/created

__init__ method - which allows every instance of a class to be created with specific parameters predertermined at the creation



self variable - allows information to shared efficiently.


Inheritance-
using attributes and methouds from one class in another class

class Person():
   def __init__(self,attribute,attribute2)

class Enemy(Person):
   def __init__(self,new_attribute,attribute,attribute2)

Multiple inheritance-
 when one calss inherits from multiple classes and is also able to use attributes and methouds from both classes

 Polymorphism:
 method overriding
 method in child class overrides the methods of parent class