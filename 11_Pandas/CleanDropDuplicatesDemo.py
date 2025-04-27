from pathlib import Path
import pandas as pd


# 移除重複資料
def dropDuplicates(path):
    df = pd.read_csv(
        path,
        delimiter=",",
        engine="python",
        skipinitialspace=True
    )
    print(f"df:\n{df}")
    print("-----------------------------------")

    # 檢查是否有重複資料
    # keep='first'(預設)代表值重複時保留第一筆，其餘刪除
    print(f"df.duplicated():\n{df.duplicated(keep='first')}")
    print("-----------------------------------")

    # subset參數可以設定哪些欄位值相同就直接視為重複資料
    print("df.duplicated(subset=['name']):")
    print(df.duplicated(subset=["name"]))
    print("-----------------------------------")

    # 移除重複資料(所有欄位值相同才會被視為重複資料)
    # keep參數預設為'first'，代表值重複時保留第一筆，其餘刪除
    print(f"df.drop_duplicates():\n{df.drop_duplicates()}")
    print("-----------------------------------")

    # subset參數可設定哪些欄位值相同就直接視為重複資料，可節省比對時間
    print("df.drop_duplicates(subset=['name']):")
    print(df.drop_duplicates(subset=["name"]))


def main():
    path = Path("11_Pandas", "read", "raw.csv")
    dropDuplicates(path)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
