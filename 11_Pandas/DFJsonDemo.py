from pathlib import Path
import pandas as pd
from pandas import DataFrame


# 載入JSON檔案
def load_df_json(read_dir: Path):
    df_json = pd.read_json(read_dir/"books.json")
    print(f"載入books.josn內容如下:\n{df_json}")
    return df_json


# 存成JSON檔案
def save_df_json(df: DataFrame, write_dir: Path):
    # orient="records"，格式為list-dict
    df.to_json(
        write_dir/"df_records.json",
        orient="records"
    )
    print("已儲存DataFrame為df_records.json檔")

    # 存成JSON檔案，預設orient="columns"，格式為dict-dict
    df.to_json(
        write_dir/"df_columns.json",
        orient="columns"
    )
    print("已儲存DataFrame為df_columns.json檔")


def main():
    # 指定載入目錄
    read_dir = Path("11_Pandas", "read")
    df_json = load_df_json(read_dir)
    print("-----------------------------------")

    # 指定存檔目錄，不存在就建立
    write_dir = Path("11_Pandas", "write")
    write_dir.mkdir(exist_ok=True)
    save_df_json(df_json, write_dir)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
