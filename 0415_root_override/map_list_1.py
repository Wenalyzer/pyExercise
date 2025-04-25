import timeit

class Book:
    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author

books = [
    Book("Python", 500, "Paul"),
    Book("C++", 400, "Cindy"),
    Book("Java", 450, "John"),
    Book("Rust", 550, "Rebecca"),
    Book("Go", 420, "George")
] * 10000  # 模擬大量資料


# 方法一：list comprehension
def comprehension_version():
    return [vars(b) for b in books]

# 方法二：map + vars
def map_version():
    return list(map(vars, books))

# 計時比較
comprehension_time = timeit.timeit(comprehension_version, number=100)
map_time = timeit.timeit(map_version, number=100)

comprehension_time, map_time

print(comprehension_time)
print(map_time)