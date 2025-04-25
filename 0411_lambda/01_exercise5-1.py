def verify_user_input():
    while True:
        try:
            nums = list(map(int, input("請輸入整數數列(空白分隔): ").split()))
            if not nums: # 捕捉空 List
                print("沒有輸入，請輸入整數數列")
                continue
            return nums
        except ValueError:
            print("輸入格式錯誤，請輸入整數數列")

def calculate(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

def main():
    # num_seq = verify_user_input()
    num_seq = list(map(int, input("請輸入整數數列(空白分隔): ").split()))
    print("數列為:", *num_seq)
    total, avg = calculate(num_seq)
    print(f"總和 = {total}\n平均 = {avg}")

if __name__ == "__main__":
    main()