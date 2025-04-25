# 使用 < 對齊 左邊，使用 > 對齊 右邊，使用 10 補齊 10個字元
str1 = f"{"Name":<10}{"BMI":>7}{"Weight":>10}"

print(str1)

# 使用 f-strings 
print(f"{'John':10}{24.123:7.1f}{72.355:10.1f}")
print(f"{'Allen':10}{40.673:7.1f}{106.345:10.1f}")
print(f"{'Sue':10}{19.543:7.1f}{45.235:10.1f}")

print("------------------------------------")

str2 = "{:<10}{:>7}{:>10}".format("Name", "BMI", "Weight")

print(str2)

# 使用 str.format()
print("{:10}{:7.1f}{:10.1f}".format("John", 24.123, 72.355))
print("{:10}{:7.1f}{:10.1f}".format("Allen", 40.673, 106.345))
print("{:10}{:7.1f}{:10.1f}".format("Sue", 19.543, 45.235))