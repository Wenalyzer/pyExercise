from pathlib import Path
import pandas as pd


# 轉換成日期時間格式
def toDatetime(path):
    df = pd.read_csv(
        path,
        delimiter=",",
        engine="python",
        skipinitialspace=True
    )
    print(f"df:\n{df}")
    print("-----------------------------------")

    try:
        # format='ISO8601' if your strings are all ISO8601 but not necessarily in exactly the same format;
        # format='mixed', the format will be inferred for each element individually.
        # 日期格式不正確會產生執行錯誤；但errors='coerce'，會將錯誤的日期格式轉換成NaT(時間空值)，就不會產生錯誤
        print("pd.to_datetime(df['date'], format='mixed', errors='coerce'):")
        print(pd.to_datetime(df["date"], format="mixed", errors="coerce"))
        print("-----------------------------------")

        # 將轉成日期格式的值存入date欄位
        df["date"] = pd.to_datetime(
            df["date"], format="mixed", errors="coerce")
        print(f"df:\n{df}")
        print("-----------------------------------")

        # NaT是時間空值，跟NaN一樣會被dropna()移除
        print(f"df.dropna():\n{df.dropna(subset=['date'])}")
    except Exception as err:
        print(f"Exception: {err}")


def main():
    path = Path("11_Pandas", "read", "raw.csv")
    toDatetime(path)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
