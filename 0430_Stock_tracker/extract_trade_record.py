from pathlib import Path
import pandas as pd

path = Path.cwd() / "0430_Stock_tracker" / "data"

def load_df_csv(read_dir):
    usecols = [0, 2, 5, 6, 7, 8, 13]
    df_csv = pd.read_csv(
        read_dir/"trade_record_raw.csv",
        delimiter=",",
        usecols=usecols,
        engine="python"
    )
    
    # 設定第2欄為index
    df_csv.set_index(df_csv.columns[1], inplace=True)
    # 先把index為NaN的row移除
    df_csv = df_csv[~df_csv.index.isna()]
    # 其餘NaN值填0
    df_csv = df_csv.fillna(0)

    # 顯示前5列
    print(df_csv.head())
    print("-----------------------------------")
    # 顯示欄位資訊與型態
    print(df_csv.info())
    print("-----------------------------------")
    # 顯示數值型欄位的統計摘要
    print(df_csv.describe())
    print("-----------------------------------")
    return df_csv

def save_df_csv(df, write_dir):

    df.to_csv(write_dir/"trade_record_done.csv", header=True, index=True)

    print("已儲存csv檔")

def main():
    # 指定載入目錄
    df_csv = load_df_csv(path)

    # 指定存檔目錄，不存在就建立
    path.mkdir(exist_ok=True)
    save_df_csv(df_csv, path)

if __name__ == "__main__":
    main()