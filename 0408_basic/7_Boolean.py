a = True

# 確認 a 的類型
print(type(a))

print("------------------------------")

i = 1
j = 1

# 確認 i 是否大於 j 
print(f"{i} > {j}: {i > j}")
print(f"{i} >= {j}: {i >= j}")
print(f"{i} < {j}: {i < j}")
print(f"{i} <= {j}: {i <= j}")
print(f"{i} == {j}: {i == j}")
print(f"{i} != {j}: {i != j}")

print("------------------------------")

# 檢測 除法 浮點數精度
a = 100.0
b = 11.11 / 0.1111
print(f"a == b: {a == b}")
print(f"b: {b}")

print("------------------------------")


# 檢測 加法 浮點數精度
k= 0.3
l= 2.4
m= 2.7

print(f"{k} + {l} == {m}: {k+l == m}")
print("{} + {} == {}: {}".format(k, l, m, k+l==m))

print("------------------------------")

# 檢測 乘法 浮點數精度
n= 0.53
o= 100.0
p= 53.0

print(f"{n} * {o} == {p}: {n*o == p}")
print("{} * {} == {}: {}".format(n, o, p, n*o==p))