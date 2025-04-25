import sys

a = 1
b = 2.0
c = "3"
d = (1, 2.0, "3")
e = [1, 2.0, "3"]
f = {1, 2.0, "3"}
g = {
    "0": 1,
    "1": 2.0,
    "2": "3" 
}

# 確認變數類型
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), sep=",\n")

# 確認變數所占記憶體空間
print(sys.getsizeof(a), sys.getsizeof(b), sys.getsizeof(c), sys.getsizeof(d), sys.getsizeof(e), sys.getsizeof(f), sys.getsizeof(g), sep=",\n")