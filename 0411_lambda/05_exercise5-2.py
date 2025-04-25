def calculate(numbers, myFunction):
    myFunction(numbers)

def verify_user_input():
    prompt = "請輸入整數數列(空白分隔): "
    err_msg = "輸入不可為空，請再試一次"
    err_msg2 = "輸入格式錯誤，請再試一次"
    while True:
        try:
            input_string = input(prompt)
            print(f"數列為: {input_string}")
            nums = list(map(int, input_string.split()))
            if not nums:
                print(err_msg)
                continue
            return nums
        except ValueError:
            print(err_msg2)

def myAverage(numbers):
        result = sum(numbers) / len(numbers)
        print(f"平均 = {result}")

def mySum(numbers):
        result = sum(numbers)
        print(f"總和 = {result}")

def main():
    # num_seq = verify_user_input()
    num_seq = list(map(int, input("請輸入整數數列(空白分隔): ").split()))
    calculate(num_seq, myAverage)
    calculate(num_seq, mySum)

if __name__ == "__main__":
    main()