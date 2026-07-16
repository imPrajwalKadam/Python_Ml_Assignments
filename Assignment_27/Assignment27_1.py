"""
Write a python program to impliment a class named  bookstore  with the  following specification 
- The class should contain two instance variables :
    -Named(Book Name)
    -Author(Book Author)

- The Class Should Contain one class variable:
    - noofBook(initializw to 0)
- Define a constructor (__init__) that accept Name and Author and initializes instance variables.
- Inside the constructor increment the class variable NoOfBooks by 1 when ever the new object created
- Impliment an instance method .
    - Display()- should display the books detail in the format:
    <BookName> by <Author> . No of books <NoOfBooks> 

Example usage :
    obj1= BookStore("Linux system progreamming ","Robert love")
    obj1.Display() #Linux system progreamming Robert love, No Of books :1
    
    obj2= BookStore("C Progrmming","Dannis Ritchi")
    obj2.Display() # C Progrmming,Dannis Ritchi, No Of books :2
"""
class BookStore:
    noOfBooks = 0
    def __init__(self,Name,Author):
        self.name = Name
        self.author = Author
        BookStore.noOfBooks +=1

    def Display(self):
        print(f"{self.name} by {self.author}, No of books {BookStore.noOfBooks}")

obj1 = BookStore("Linux system Programming","Robert Love")
obj1.Display()

obj2 = BookStore("C Programming","Dennis Ritchi")
obj2.Display()
