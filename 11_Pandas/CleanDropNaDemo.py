from pathlib import Path
import pandas as pd


# 移除預設空值
def dropNa(path):
    # 原始資料如果沒有值，讀進來會轉成NaN
    # "skipinitialspace=True"代表忽略原始空白字元
    df = pd.read_csv(
        path,
        delimiter=",",
        engine="python",
        skipinitialspace=True
    )
    print(f"df:\n{df}")
    print("-----------------------------------")

    # 先列出哪些資料被視為空值
    print(f"df.isna():\n{df.isna()}")
    print("-----------------------------------")
    # 刪除帶有空值的該列資料
    print(f"df.dropna():\n{df.dropna()}")


# 移除自訂空值
def dropNaCustom(path):
    # 自訂哪些值視為空值
    naCustom = ["na", "--"]
    print(f"naCustom = {naCustom}")

    df = pd.read_csv(
        path,
        na_values=naCustom,
        delimiter=",",
        engine="python",
        skipinitialspace=True
    )
    print(f"df:\n{df}")
    print("-----------------------------------")
    print(f"df.dropna():\n{df.dropna()}")
    print("-----------------------------------")
    # 指定price欄位是空值者才drop
    print(f"df.dropna(subset=['price']):\n{df.dropna(subset=['price'])}")


def main():
    path = Path("11_Pandas", "read", "raw.csv")
    dropNa(path)
    print("===================================")
    dropNaCustom(path)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
