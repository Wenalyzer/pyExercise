# 將 input string 分割後儲存
def get_splitted_str():
    prompt = "請輸入整數數列(空白分隔): "
    splitted_str = input(prompt).split()
    return splitted_str

# 自己造輪子，協助理解 map(func, iterable) 的功能
def my_map(func, iterable):
        for item in iterable:
            yield func(item)

# 計算並回傳數列的總和與平均
def calculate_sum_and_mean(num_list):
    total = sum(num_list)
    avg = total / len(num_list)
    return total, avg

def main():
    num_str = get_splitted_str()
    
    num_seq = list(my_map(int, num_str))

    total, avg = calculate_sum_and_mean(num_seq)

    print(f"總和 = {total}\n平均 = {avg}")

if __name__ == "__main__":
    main()