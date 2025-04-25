nums = [1, 2, 3, 4, 5]
result1 = list(map(lambda x: x**2, nums))
print(result1)

# filter(func, iterable)
result2 =  list(filter(lambda x: x % 2 == 0, nums))
print(result2)

people = [("Amy", 25), ("Bob", 20), ("Cathy", 23)]

for i in people:
    print(i[1])

# sorted(iterable, key=None, reverse=False)
sorted_people = sorted(people, key=lambda x: x[1])

print(sorted_people) 