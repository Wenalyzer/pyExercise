import pandas as pd
import yfinance as yf
from pathlib import Path

DATA_PATH = Path.cwd() / "Portfolio_tracker" / "data"

def get_usd_twd(start: str, end: str) -> pd.DataFrame:
    """
    下載每日美元兌台幣匯率
    Args:
        start (str): 起始日期，格式"YYYY-MM-DD"
        end (str): 結束日期，格式"YYYY-MM-DD"
    Returns:
        pd.Series: 每日收盤匯率
    """
    df = yf.download("USDTWD=X", start=start, end=end)
    df.to_csv(DATA_PATH/"usd_twd_noheader.csv", index=True, header=False)
    return df["Close"]

def calc_daily_holding(trade_df: pd.DataFrame, asset_code: str) -> pd.Series:
    """
    計算每日持有數量（同一天多筆會自動加總）
    Args:
        trade_df: 交易紀錄DataFrame
        asset_code: 資產代號（如"VOO"、"006208"等）
    Returns:
        pd.Series: 每日累積持有數量，index為日期
    """
    # 選出指定資產的所有交易
    df = trade_df[trade_df["代號"] == asset_code].copy()
    # 買入股數 - 賣出股數
    df["淨買入"] = df["買入股數"] - df["賣出股數"]
    
    # 按日期 groupby 並加總（同一天多筆會合併）
    daily = df.groupby(df.index)["淨買入"].sum()

    # 累積持有
    holding = daily.cumsum() # cumulative sum
    return holding

def create_asset_value_csv(
        data_dir: Path = DATA_PATH, 
        output_file: str = "asset_value.csv"
    ) -> None:
    """
    計算每日資產價值並儲存為 CSV。
    """
    trade_df = pd.read_csv(data_dir/"trade_record_done.csv", index_col=1)

    # 將 index 轉為 datetime 型態，指定 format，這裡根據csv格式是 "%Y/%m/%d"
    trade_df.index = pd.to_datetime(trade_df.index, format="%Y/%m/%d")

    # 計算分析期間（從最早交易日到今天）
    start = trade_df.index.min().strftime("%Y-%m-%d")
    end = pd.Timestamp.today().strftime("%Y-%m-%d")
    
    # 定義資產分類
    asset_codes = ["VOO", "006208", "00687B", "00919", "BTC", "WBETH", "BNB", "BCH"]
    idx = pd.date_range(start, end)
    df = pd.DataFrame(index=idx, columns=asset_codes, dtype=int).fillna(0)

    usd_twd = get_usd_twd(start, end)
    ex_rate = usd_twd.reindex(idx, method="ffill").squeeze()

    btc_holding = calc_daily_holding(trade_df, "BTC").reindex(idx, method="ffill").fillna(0)
    mbtc_holding = calc_daily_holding(trade_df, "M-BTC").reindex(idx, method="ffill").fillna(0)
    total_btc_holding = btc_holding + mbtc_holding

    for code in asset_codes:    
        holding = calc_daily_holding(trade_df, code).reindex(idx, method="ffill").fillna(0)

        if code == "VOO":
            price = yf.download(code, start=start, end=end)["Close"].reindex(idx, method="ffill").squeeze()

            df[code] = round(holding * price * ex_rate)

        elif code in ["006208", "00919"]:
            price = yf.download(code+".TW", start=start, end=end)["Close"].reindex(idx, method="ffill").squeeze()

            df[code] = round(holding * price)

        elif code == "00687B":
            price = yf.download(code+".TWO", start=start, end=end)["Close"].reindex(idx, method="ffill").squeeze()

            df[code] = round(holding * price)

        elif code == "BTC":
            price = yf.download(code+"-USD", start=start, end=end)["Close"].reindex(idx, method="ffill").squeeze()

            df[code] += round(total_btc_holding * price * ex_rate)
        
        elif code in ["WBETH", "BNB", "BCH"]:
            price = yf.download(code+"-USD", start=start, end=end)["Close"].reindex(idx, method="ffill").squeeze()

            df[code] = round(holding * price * ex_rate)
        
    df.fillna(0, inplace=True)
    df = df.astype("int")
    df.to_csv(data_dir/output_file, index=True, header=True)