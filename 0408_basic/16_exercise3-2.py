season = input("請輸入你喜愛的季節: ")

match season:
    case "春":
        print("春暖花開")
    case "夏":
        print("夏日炎炎")
    case "秋":
        print("秋高氣爽")
    case "冬":
        print("冬風凜冽")
    case _:
        print("您的輸入有誤")