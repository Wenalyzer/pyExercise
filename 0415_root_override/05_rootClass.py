class Book(object):
    def __init__(self, name="", price=0.0, author=""):
        self.name = name
        self.price = price
        self.author = author

    # Book類別若沒覆寫__str__()，會列印object.__str__()結果
    # def __str__(self):
    #     return f"name: {self.name}\nprice: {self.price}\nauthor: {self.author}"

def main():
    book = Book("Python", 500, "Paul")
    # 會自動呼叫__str__()
    print(book)

if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
