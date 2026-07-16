"""
Write a python program to impliment a class named BankAccount With the following requirements.
    
    -The class should contain two instance variables
        Name (Account Holder name)
        Amount (Account banalce)
    
    -The class should contain one class variable 
        ROI(Rate Of Intrest). initialize to 10.5
    
    -Define Constructor (__init__) function that accepts name and initial amount.
    
    -Impliment the following instance methods:
        -Display() - Display Account Holder name and current balance

        -Deposit() - accept an amount from user and add it to balance 
        
        -Withdraw() - Accept an amount from the user and substract it from balance (Insure withdrawal 
            is allowed only if sufficient balance exists)

        -calculateIntrest() - calculate and return intrest using formula
            Intreast = (Amount * ROI) / 100
            
        - create multiple objects and demonstrates all methods
"""

class BankAccount:
    ROI = 10.5
    def __init__(self,Name,Initial_Amount):
        self.name = Name
        self.initial_amount = Initial_Amount
    
    def Display(self):
        print(f"Account Holder Name : {self.name} , Balance : {self.initial_amount}")

    def Deposit(self):
        amount = int(input("Enter deposit amount :"))
        self.initial_amount += amount

    def Withdraw(self):
        if self.initial_amount <= 0:
            print("Insufficieant balance..")
        else:
            withDrawAmt = int(input("Enter Withdraw Amount:"))
            self.initial_amount = self.initial_amount - withDrawAmt
    def calculateIntreast(self):
        Intreast = (self.initial_amount * BankAccount.ROI)/100
        return Intreast
    

try :
    bObj = BankAccount("Prajwal",11000)
    bObj.Display()

    bObj.Deposit()
    bObj.Display()

    bObj.Withdraw()
    bObj.Display()

    intreast = bObj.calculateIntreast()
    print(f"Intreast is : {intreast}")


    bObj = BankAccount("Atharva",0)
    bObj.Display()

    bObj.Deposit()
    bObj.Display()

    bObj.Withdraw()
    bObj.Display()

    intreast = bObj.calculateIntreast()
    print(f"Intreast is : {intreast}")

except ValueError as vObj:
    print("Exception occured :",vObj )