def get_people_num():
    while True:
        try:
            num = int(input("請問有幾個好友? "))
            if num <= 0: # 輸入的整數非自然數
                print("請輸入正整數")
                continue
            return num
        except ValueError: # 輸入造成 ValueError
            print("請輸入有效數字")  

def yield_name_cash_pairs(number):
    for i in range(number):
        while True:
            try:
                name, cash = input(f"請輸入第{i+1}個好友名與身上現金: ").split()
                break 
            except ValueError: # 輸入的現金造成ValueError
                print("格式錯誤，請輸入名字 數字(以空格分開)")
        yield {"name": name, "cash": int(cash)}

def friends_with_enough_cash(friends_list):
    while True:
        try:
            target = int(input("請輸入欲借現金: "))
            if target <= 0: # 輸入的整數非自然數
                print("請輸入正整數") 
                continue 
            break 
        except ValueError: # 輸入的現金造成ValueError
            print("請輸入有效數字")
        
    rich_names = [f["name"] for f in friends_list if f["cash"] >= target]
    return rich_names

def main():
    people_num = get_people_num()
    friends_cash = list(yield_name_cash_pairs(people_num))
    # print(friends_cash)
    print("--------------------------------------------------")
    eligible_friends = friends_with_enough_cash(friends_cash)
    # print(eligible_friends)
    joined_names = ", ".join(eligible_friends)
    
    print(f"可借錢的好友: {joined_names}, 共{len(eligible_friends)}人")

if __name__ == "__main__":
    main()