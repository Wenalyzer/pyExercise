# 檢查使用者輸入是否合乎規則，若正確則回傳輸入值
def input_in_range():
    prompt="不吉利數字 (1 ~ 9): "
    err_msg="輸入錯誤，請再輸入一次"

    # 如果使用者輸入 範圍外的整數 or 非整數(ValueError), 輸出錯誤訊息
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 9:
                return value
            else:
                print(err_msg)
        except ValueError:
            print(err_msg)

# 去除不吉利數字後print出來，同時統計數字個數
def print_filtered_numbers(unlucky_digit):
    lottrery_numbers = 49
    numbers_per_row = 10
    count = 0
    for i in range(1, lottrery_numbers+1):
        if str(unlucky_digit) not in str(i): # 轉換成字串後比對
            print(f"{i:02d}", end=" ")
            count += 1
            if count % numbers_per_row == 0: # 每十個值換行
                print()
    print(f"\n總個數: {count}")

def main():
    unlucky = input_in_range()
    print_filtered_numbers(unlucky)

if __name__ == "__main__":
    main()