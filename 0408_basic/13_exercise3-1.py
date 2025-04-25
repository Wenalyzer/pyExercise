money = eval(input("身上的錢: "))
holiday = eval(input("放假天數: "))

# 使用 if elseif 結構篩選條件
if money >= 20000 and holiday >= 5:
    print("可以去泰國玩")
elif money >= 20000:
    print("有錢沒閒")
elif holiday >= 5:
    print("有閒沒錢")
else:
    print("沒錢沒閒，真可憐")