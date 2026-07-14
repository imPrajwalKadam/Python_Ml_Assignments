"""
Write a python program to impliment a class named Circle  with the following reqirements :
- The class should contain three instance variables:Radius, area and circumfereance.
- The class should contains one class variable named PI. initialized to 3.14.
- Define a constructor (__init__) that initialized  all instance variables to 0.0.
- Impliment the following Instance methods:
    Accept() - accept the radius of the circle from the user .
    CalculateArea() - calculate the area of the circle and store it in area variable.
    CalculateCircumference() - calculate the circumfereance of the circle and store it in circumfereance variable
    Display() - Display the values of radius ,area and circumference
- create multiple object of the Cirle class  and invoke all instance method for each object .
"""

class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.area = 0.0
        self.circufereance = 0.0

    def Accept(self):
        r = int(input("Enter Raidus : "))
        self.Radius = r
        return self.Radius

    def CalculateArea(self):
        self.area = self.PI * self.Radius * self.Radius
        return self.area

    def CalculateCircumference(self):
        self.circufereance = 2 * self.PI * self.Radius
        return self.circufereance
    
    def Display(self):
        print("Radius is : ",self.Radius)
        print("Area of circle is :",self.area)
        print("circufereance of circle is : ",self.circufereance)
    

cobj = Circle()
r = cobj.Accept()
cobj.CalculateArea()
cobj.CalculateCircumference()
cobj.Display()
