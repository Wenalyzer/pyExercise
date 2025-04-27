from pathlib import Path
import pandas as pd


# 移除錯誤資料
def dropCondition(path):
    df = pd.read_csv(
        path,
        delimiter=",",
        engine="python",
        skipinitialspace=True
    )
    print(f"df:\n{df}")
    print("-----------------------------------")

    # 自訂錯誤條件當作移除依據
    print("df[df['price'] < 0].index:")
    print(df[df['price'] < 0].index)
    print("-----------------------------------")

    print("df.drop(df[df['price'] < 0].index):")
    print(df.drop(df[df['price'] < 0].index))

    # 也可使用迴圈
    # print("將「price < 0」的資料移除: ")
    # for i in df.index:
    #     if df.loc[i, "price"] < 0:
    #         df.drop(i, inplace=True)
    # print(f"df:\n{df}")


def main():
    path = Path("11_Pandas", "read", "raw.csv")
    dropCondition(path)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")