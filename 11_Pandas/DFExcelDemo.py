from pathlib import Path
import pandas as pd
from pandas import DataFrame


# 需要先安裝openpyxl套件: conda install openpyxl
def load_df_excel(read_dir: Path):
    # 載入Excel檔案
    # 使用 read_excel() 需要安裝 openpyxl 套件
    df_excel = pd.read_excel(read_dir/"books.xlsx")
    print(f"載入books.xlsx內容如下:\n{df_excel}")
    return df_excel


def save_df_excel(df: DataFrame, write_dir: Path):
    # 存成Excel檔案
    # index=False避免將index存入，預設True
    # sheet_name預設"Sheet1"
    df.to_excel(
        write_dir/"df.xlsx",
        index=False,
    )
    print("已儲存DataFrame為df.xlsx檔")

    # 存成Excel檔案
    # index=False避免將index存入，預設True
    # sheet_name="BookList"指定sheet name為"BookList"
    df.to_excel(
        write_dir/"df_booklist.xlsx",
        index=False,
        sheet_name="BookList"
    )
    print("已儲存DataFrame為df_booklist.xlsx檔")


def main():
    # 指定載入目錄
    read_dir = Path("11_Pandas", "read")
    df_excel = load_df_excel(read_dir)
    print("-----------------------------------")

    # 指定存檔目錄，不存在就建立
    write_dir = Path("11_Pandas", "write")
    write_dir.mkdir(exist_ok=True)
    save_df_excel(df_excel, write_dir)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
