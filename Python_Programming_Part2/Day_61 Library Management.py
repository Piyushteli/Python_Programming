"""
Library Management using python
"""

class Library:
    def __init__(self):
        self.nobooks=0
        self.books=[]

    def addbooks(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def showinfo(self):
        print(f"The library has {self.nobooks} books.\nThe Books are")
        for book in self.books:
            print(book)

obj=Library()
obj.addbooks("Harrypotter1")
obj.addbooks("Harrypotter2")
obj.addbooks("Harrypotter3")
obj.addbooks("Harrypotter4")
obj.showinfo()