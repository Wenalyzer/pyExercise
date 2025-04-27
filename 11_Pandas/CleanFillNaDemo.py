from pathlib import Path
import pandas as pd


# 填補空值
def fillNa(path):
    df = pd.read_csv(
        path,
        delimiter=",",
        engine="python",
        skipinitialspace=True
    )
    print(f"df:\n{df}")
    print("-----------------------------------")
    print("將price欄位內的空值填入0")
    df["price"] = df["price"].fillna(0)
    print(f"df:\n{df}")


def main():
    path = Path("11_Pandas", "read", "raw.csv")
    fillNa(path)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
