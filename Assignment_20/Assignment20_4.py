"""
Design a python application that creates three threads named small, capital and Digits

- all thread should accept a string as input

- The Small Thread should count and display the number of lowercase characters.

- The Capital Thread should count and display the number of upper characters.

- The Digits Thread should count and display the number of numaric digits.

- Each thread  must also display .
    Thread Id
    Thread Name

"""
import threading
import time

def Small(myStr):
    print("Thread id  :",threading.get_ident())
    print("Thread Name : Small")

    iCnt = 0
    for ch in myStr:
        if ch == ch.lower():
            iCnt +=1
            print(ch)

    print("small count is: ",iCnt)

def Capital(myStr):
    print("Thread id  :",threading.get_ident())
    print("Thread Name : Capital")

    iCnt = 0
    for ch in myStr:
        if ch == ch.upper():
            iCnt +=1
            print(ch)

    print("capital count is: ",iCnt)


def Digits(myStr):
    print("Thread id  :",threading.get_ident())
    print("Thread Name : Digits")

    iCnt = 0
    for ch in myStr:
        if ch.isdigit():  
            iCnt +=1
            print(ch)

    print("number of digits are: ",iCnt)


    
    

def main():


    start_time = time.perf_counter()

    t1 = threading.Thread(target=Small,args=("PrajwalKadam",))

    t2 = threading.Thread(target=Capital,args=("PrajwalKadam",))
    t3 = threading.Thread(target=Digits,args=("PrajwalKadam1",))

    t1.start()
    t2.start()
    t3.start()

    t1.join()    
    t2.join()   
    t3.join()   

    print("Exit from main...")    

    end_time = time.perf_counter()
    print(f"Time required is :{end_time - start_time:.4f} seconds ")

if __name__ == "__main__":
    main()