import random

lottery_set = set()
while len(lottery_set) < 7:
    lottery_set.add(random.randint(1, 49))
# print(lottery_set)
lottery_list = list(lottery_set)
# print(lottery_list)
special_num = lottery_list.pop()


# lottery = random.sample(range(1, 50), 7)
# special_num = lottery.pop()

# print("開獎，大樂透號碼為: ")
# for i in lottery:
#     print(i, end=" ")
# print(f"特別號: {special_num}")

print("開獎，大樂透號碼為:\n" + " ".join(map(str, lottery_list)), f"特別號: {special_num}")

lottery_list.sort()

# print("由小到大排列: ")
# for i in lottery:
#     print(i, end=" ")
# print(f"特別號: {special_num}")

print("由小到大排列:\n" + " ".join(map(str, lottery_list)), f"特別號: {special_num}")