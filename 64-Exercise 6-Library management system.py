class library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)

    def showinfo(self):
        print('library have',self.no_of_books,"books")

        for i in self.books:
            print(i)

l1=library()
l1.addbook("Harry Potter")
l1.addbook("Harry barber")
l1.addbook("Harry cleaner")
l1.addbook("Harry coder")
l1.addbook("Harry shooter")
l1.showinfo()


