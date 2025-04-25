dividend = eval(input("請輸入被除數: "))
divisor = eval(input("請輸入除數: "))

# 使用f-string 和 str.format()，以及 // 和 % 兩種運算子
print(f"{dividend} // {divisor} = {dividend//divisor} ... {dividend%divisor}")
print("{} // {} = {} ... {}".format(dividend, divisor, divisor//divisor, dividend%divisor))