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
    
    def lendbook(self,book, name):
        if book in self.booklist:
            if book not in self.lenderDict:
                self.lenderDict.update({book:self.name})
                print("lender database updated, you can collect the book now")
            else:
                print("the book is already borrowed by: ",self.lenderDict[book])
                
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
        else:
            print("The book is not available in the library")
            
shubhLib = Library(["python","Java","C++","Ruby"],"Shubham")

print(shubhLib.__dict__)

shubhLib.displaybook()