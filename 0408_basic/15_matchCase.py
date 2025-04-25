rating = 5

# 使用match case語法，根據輸入值決定輸出
match rating:
    case 1:
        print("你得了MVP！")
    case 2:
        print("沒問題我們的雙子星")
    case 3:
        print("你那麼認那個評分做什麼嘛")
    case 4 | 5 as number:
        print(f"第{number}名，躺贏狗！")
    case _:
        print("把我送哪來啦，這還是LOL嗎？")

# 也可以把Tuple作為值輸入
niceSeasons = ("Spring", "Fall")
match niceSeasons:
    case ("Summer", "Winter"):
        print("冷熱分明季節")
    case ("Spring", "Fall"):
        print("溫和季節")
    case _:
        print("季節比對失敗")