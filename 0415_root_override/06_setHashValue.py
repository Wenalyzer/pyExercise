class Book:
    def __init__(self, isbn, name="", price=0.0):
        self.isbn = isbn
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __hash__(self):
        return hash(self.isbn)

    def show(self):
        print(f"ISBN: {self.isbn}")
        print(f"name: {self.name}")
        print(f"price: {self.price}")

    @staticmethod
    def showAll(books):
        for book in books:
            book.show()
            print()

def main():
    myBooks = set()
    myBooks.add(Book("123456", "Python", 500))
    myBooks.add(Book("789012", "C++", 400))
    myBooks.add(Book("789012", "C++", 400))
    Book.showAll(myBooks)

if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")