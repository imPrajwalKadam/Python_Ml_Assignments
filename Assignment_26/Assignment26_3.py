"""
Write a Python Program to impliment a class named Arthmatic with the following
characteristics 
- The class should contain two instance viable: valie1and value2
- Define constructor (__init__)that initializes all instance variables to 0.
- Impliment the following instance method.
    - Accept() - accept values for value1 and value2 from the user .
    - Addition() - returns the addition  of value1 and value2.
    - Substraction() - returns the substractionsof value1 and value2.
    - Multiplication() - return multiplication of value1 and value2.
    - Division() - return division of value1 and value2 (handel division by 
        zero properly).
    - Create multiple objects of the Arithmetic  class and invoke all the 
        instance method . 
"""

class Arithmatic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        no1 = int(input("Enter a first number : "))
        no2 = int(input("Enter a second number : "))
        self.value1 = no1
        self.value2 = no2
    
    def additionVal(self): 
            return self.value1+self.value2

    def substractionVal(self):
            return self.value1 - self.value2

    def multiplicationVal(self):
         return self.value1 * self.value2

    def divisionVal(self):
        return self.value1 / self.value2

    
aObj = Arithmatic()
aObj.Accept()


aAdd = aObj.additionVal()
print(f"Addition is {aAdd}")


aSub = aObj.substractionVal()
print(f"substraction is {aSub}")

aMult = aObj.multiplicationVal()
print(f"multiplication is {aMult}")

aDiv = aObj.divisionVal()
print(f"Division is {aDiv}")
