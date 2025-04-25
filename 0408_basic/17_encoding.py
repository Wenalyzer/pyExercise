text = "你好！"

# 使用
for char in text:
    print(f"{char}: {ord(char)}")

utf8_bytes = text.encode("utf-8")
print("UTF-8 編碼：", utf8_bytes)