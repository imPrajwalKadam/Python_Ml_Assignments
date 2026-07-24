""" 
Write a python program to impliment class named Numbers with the following  specifications:
- The class should contain one class instance variable
    - Value

- Define a constructor (__init__) the accept the number from user and initializes Value.
-Impliment the following instance methods :
    - ChkPrime() - Return True if the numbers is prime ,otherwise retrurn False
    - ChkPerfect() - return True if number is Prfect , otherwise return False
    - Factors() - Display all factors of the number .
    - Sumfactors() - return sum of all factors of numbers .

- Create miltiple objects and call all methods .

"""

class Value:
    value = 0
    def __init__(self):
        no = int(input("Enter a number:"))
        Value.value = no

    def ChkPrime(self):
        cnt = 2
        while cnt <= Value.value//2:
            if Value.value % cnt   == 0:
                break
            cnt+=1

        if cnt== (Value.value //2)+1:
            return True
        else:
            return False
    
    def ChkPerfect(self):
        iAdd = 0
        for i in range(1,Value.value):
            if Value.value % i  == 0:
                iAdd = iAdd + i

        print(iAdd)
        if iAdd == Value.value:
            return True
        else:
            return False
        
    def Factors(self):
        print("Factors of number is ")
        for i in range(1,Value.value+1):
            if Value.value % i == 0:
                print(i)

    def Sumfactors(self):
        iSum = 0
        for i in range(1,Value.value+1):
            if Value.value % i == 0:
                iSum = iSum + i

        return iSum

    
try:
    chkPrimeObj = Value()
    bRet = chkPrimeObj.ChkPrime()

    if bRet == True:
        print("prime number ")
    else:
        print("Not Prime")

    # chkPerfectObj = Value()
    # Ret = chkPerfectObj.ChkPerfect()

    # if Ret == True:
    #     print("Perfect number")
    # else:
    #     print("Not Perfect")


    # factorObj = Value()
    # factorObj.Factors()


    # sumFactObj = Value()

    # sumFact = sumFactObj.Sumfactors()
    # print(f"Summation of factors is: {sumFact}")

except ValueError as vObj:
    print("Exception occured :",vObj )