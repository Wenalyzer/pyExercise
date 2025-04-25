import numpy as np

stu_num = int(input("請問有幾個學生? "))

stu_list = []
for i in range(stu_num):
    tmp_data = input(f"請輸入第{i+1}位學生名與國、英、數成績: ").split()
    stu_list.append(tmp_data)

print("輸入完畢！")

stu_array = np.array(stu_list)

search_str = input("請輸入欲查詢的學生名: ").lower()

found = False
for s in stu_array:
    if search_str in s[0].lower():
        found = True
        print(s[0], s[1], s[2], s[3])
if not found:
    print("查無此學生！")