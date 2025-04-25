import random
from collections import Counter

def simulate_lottery_special(draw_times):
    special_counter = Counter()

    for _ in range(draw_times):  

        # lottery_list = random.sample(range(1, 50), 7)
        # special_num = lottery_list.pop()

        lottery_set = set()
        while len(lottery_set) < 7:
            lottery_set.add(random.randint(1, 49))
        lottery_list = list(lottery_set)
        special_num = lottery_list.pop()

        special_counter[special_num] += 1

    return special_counter

def print_special_statistics(counter):
    print("特別號出現次數統計：")
    for num in sorted(counter):
        print(f"{num:2d} 號出現 {counter[num]:6d} 次")

def main():
    times = int(input("請輸入模擬開獎次數："))
    counter = simulate_lottery_special(times)
    print_special_statistics(counter)

if __name__ == "__main__":
    main()