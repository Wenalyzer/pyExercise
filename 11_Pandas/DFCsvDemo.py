from pathlib import Path
import pandas as pd
from pandas import DataFrame


def load_df_csv(read_dir):
    # 載入CSV檔案，預設分隔符號為","，可使用正規表示式設定分隔符號
    # 建議設定engine="python"；因為預設為engine="c"，沒有支援正規表示式
    df_csv = pd.read_csv(
        read_dir/"books.csv",
        delimiter=r"\s*,\s*",
        # 如果CSV內容沒有欄位列，加上header=None即可
        # header=None,
        engine="python"
    )
    print(f"載入books.csv內容如下:\n{df_csv}")
    return df_csv


def save_df_csv(df, write_dir):
    # 存成CSV檔案，header=True會有欄位名稱，index=True會有index；預設皆為True
    df.to_csv(
        write_dir/"df_header_index.csv",
        header=True,
        index=True
    )
    print("已儲存DataFrame為df_header_index.csv檔")

    # 存成CSV檔案，header=False不會有欄位名稱，index=False不會有index
    df.to_csv(
        write_dir/"df_header_index_none.csv",
        header=False,
        index=False
    )

    print("已儲存DataFrame為df_header_index_none.csv檔")


def main():
    # 指定載入目錄
    read_dir = Path("11_Pandas", "read")
    df_csv = load_df_csv(read_dir)
    print("-----------------------------------")

    # 指定存檔目錄，不存在就建立
    write_dir = Path("11_Pandas", "write")
    write_dir.mkdir(exist_ok=True)
    save_df_csv(df_csv, write_dir)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
