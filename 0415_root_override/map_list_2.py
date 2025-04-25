import timeit

class Book:
    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author

dictionaries = [{'name': 'Python', 'price': 500, 'author': 'Paul'}] * 10000

# 方法一：list comprehension
def comprehension_version():
    return [Book(**dictionary) for dictionary in dictionaries]

# 方法二：map + lambda
def map_version():
    return list(map(lambda dictionary: Book(**dictionary), dictionaries))

# 計時比較
comprehension_time = timeit.timeit(comprehension_version, number=100)
map_time = timeit.timeit(map_version, number=100)

comprehension_time, map_time

print(comprehension_time)
print(map_time)