from pathlib import Path
import pandas as pd

DATA_PATH = Path.cwd() / "Portfolio_tracker" / "data"

def load_trade_record(read_dir: Path = DATA_PATH) -> pd.DataFrame:
    """
    讀取原始交易紀錄 CSV，回傳處理後的 DataFrame。
    """
    usecols = [0, 2, 5, 6, 7, 8, 13]
    df = pd.read_csv(
        read_dir/"trade_record_raw.csv",
        delimiter=",",
        usecols=usecols,
        engine="python"
    )
    
    # 設定第2欄為index
    df.set_index(df.columns[1], inplace=True)
    # 先把index為NaN的row移除
    df = df[~df.index.isna()]
    # 其餘NaN值填0
    df = df.fillna(0)

    # # 顯示前5列
    # print(df.head())
    # print("-----------------------------------")
    # # 顯示欄位資訊與型態
    # print(df.info())
    # print("-----------------------------------")
    # # 顯示數值型欄位的統計摘要
    # print(df.describe())
    # print("-----------------------------------")

    return df

def save_trade_record(df: pd.DataFrame, write_dir: Path = DATA_PATH) -> None:
    """
    儲存處理後的交易紀錄 DataFrame 為 CSV。
    """
    write_dir.mkdir(exist_ok=True)
    df.to_csv(write_dir/"trade_record_done.csv", header=True, index=True)

    print("已儲存csv檔")