class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lenderDict= {}
        
    def displaybook(self):
        sno = 1
        for book in self.booklist:
            print(f"{sno}:{book}")
            sno+=1
    
    def lendbook(self,book,lenName):
        self.lenName = lenName
        if book in self.booklist:
            if book not in self.lenderDict:
                self.lenderDict.update({book:self.lenName})
                print("lender database updated, you can collect the book now")
            else:
                print("the book is already borrowed by: ",self.lenderDict[book])
        else:
            print("This book is not available in Library")        
            
    def addBook(self,book):
        if book not in self.booklist:
            self.booklist.append(book)
            print("Book added to library")
        else:
            print("Book already exist in library")
            
    def returnBook(self,book):
        if book in self.booklist:
            if book in self.lenderDict:
                self.lenderDict.pop(book)
                print(f"Book {book} returned ")
            else:
                print(f"This book {book} is not in use")
        else:
            print("The book is not available in the library")
    
    def viewlendedlist(self):
        print("Books currently lended:")
        print(self.lenderDict)
            

# print(shubhLib.__dict__)

# shubhLib.displaybook()

# shubhLib.lendbook("python","shubh")

if __name__ == '__main__':
    shubhLib = Library(["python","Java","C++","Ruby"],"Shubham")
    
    while(True):
        print("Hello werlcome to our Library, Enter Your Choice to continue")
        print("1: Display books")
        print("2: Lend a book")
        print("3: Add a book")        
        print("4: Return a book")
        print("5: View lended list")
        
        userChoice = input()
        if userChoice not in ['1','2','3','4','5']:
            print("please enter valid choice")
            continue
        else:
            userChoice = int(userChoice)
            
        if userChoice == 1:
            shubhLib.displaybook()
            
        elif userChoice == 2:
            book = input("Enter book name to lend")
            lenName= input("Enter Lended name")
            shubhLib.lendbook(book,lenName)
            
        elif userChoice == 3:
            book = input("Enter book name to add to library")
            shubhLib.addBook(book)
            
        elif userChoice == 4:
            book = input("Enter book name to Return to library")
            shubhLib.returnBook(book)
            
        elif userChoice == 5:
            shubhLib.viewlendedlist()
            
        else:
            print("enter a valid option")
            
        print("Print q to quit or c to continue")
        userchoice2=""
        while userchoice2!="c" and userchoice2!="q":
            userchoice2= input()
            
            if userchoice2 == "q":
                exit()
            elif userchoice2 == "c":
                continue