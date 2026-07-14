"""
Write a python program to implement a class name demo with the folllowing specifications:
- the class should contains  two instance variable : no1 and no2
- the class should contains one class variable named Value
- Define  a constructor (__init___) that accept two parameters and initializes instance variables.
- Impliment two instance methods.
    - Fin() - Displays values of instance variable no1  and no2
    - Gun() - Displays values of instance variables no1 and no2.
Create two objects of demo class  as follows :
oBj1 = Demo(11,21)
oBj2 = Demo(51,101)

Call that instance mehthods in the given  sequence 
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
"""


class Demo:
    Value = 10
    def __init__(self,Value1,Value2):
        self.no1 = Value1
        self.no2 = Value2

    def Fun(self):
        print(self.no1)
        print(self.no2)

    def Gun(self):
        print(self.no1)
        print(self.no2)


obj1 = Demo(11,21)
obj2 = Demo(51,101)
obj1.Fun()
obj1.Gun()
obj2.Fun()
obj2.Gun()
     

        