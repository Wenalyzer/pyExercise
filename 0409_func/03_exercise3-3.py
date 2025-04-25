val1 = int(input("起始值: "))
val2 = int(input("終止值: "))
count = 0

# 不允許print以0開頭的十進位數字，print字串代替
for count in range(val2-val1+1):
    print(f"{count+val1:02d}", end=" ")
    count += 1
    if count % 10 == 0: #每十個值換行
        print()

# 使用等差數列和公式
print(f"\n總和: {int((val1+val2)*(val2+1-val1)/2)}")