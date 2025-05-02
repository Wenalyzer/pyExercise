import pandas as pd
import yfinance as yf
from pathlib import Path
import matplotlib.pyplot as plt

def get_usd_twd_series(start: str, end: str):
    """
    下載每日美元兌台幣匯率
    Args:
        start (str): 起始日期，格式"YYYY-MM-DD"
        end (str): 結束日期，格式"YYYY-MM-DD"
    Returns:
        pd.Series: 每日收盤匯率
    """
    df = yf.download("USDTWD=X", start=start, end=end)
    return df["Close"]

def calc_daily_holding(trade_df: pd.DataFrame, asset_code: str):
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
    print(df.head())
    # 將 index 轉為 datetime，指定格式
    df.index = pd.to_datetime(df.index, format="%Y/%m/%d")
    # 按日期 groupby 並加總（同一天多筆會合併）
    daily = df.groupby(df.index)["淨買入"].sum()
    # 累積持有
    holding = daily.cumsum()
    return holding

def main():
    # 讀取交易紀錄，index_col=1 指定用第2欄（交易日期）作為索引
    path = Path.cwd() / "0430_Stock_tracker"
    trade_df = pd.read_csv(path/"data"/"trade_record_done.csv", index_col=1)
    print(trade_df.head())

    # 將 index 轉為 datetime 型態，指定 format，這裡根據你的csv格式是 "%Y/%m/%d"
    trade_df.index = pd.to_datetime(trade_df.index, format="%Y/%m/%d")

    # 定義資產分類
    stock_codes = ["VOO", "006208", "00919"]  # 股票類
    bond_codes = ["00687B"]                   # 債券類
    # 其餘皆視為crypto
    all_codes = trade_df["代號"].unique()
    crypto_codes = [c for c in all_codes if c not in stock_codes + bond_codes]

    # 計算分析期間（從最早交易日到今天）
    start = trade_df.index.min().strftime("%Y-%m-%d")
    end = pd.Timestamp.today().strftime("%Y-%m-%d")

    # 下載每日美元兌台幣匯率
    usd_twd = get_usd_twd_series(start, end)

    # 建立每日日期索引，確保每一天都有資料
    idx = pd.date_range(start, end)

    # 建立空的DataFrame儲存每日資產，三個欄位分別存股票、債券、加密貨幣
    df = pd.DataFrame(index=idx)
    df["stock"] = 0
    df["bond"] = 0
    df["crypto"] = 0

    # 處理股票類（VOO、006208、00919）
    for code in stock_codes:
        # 計算每日持有數量，reindex補齊所有日期，method="ffill"用前一天的數量填補空缺
        holding = calc_daily_holding(trade_df, code).reindex(idx, method="ffill").fillna(0)
        # 取得每日收盤價
        if code == "VOO":
            # VOO為美股，收盤價為美元，需乘每日匯率換算台幣
            price = yf.download(code, start=start, end=end)["Close"].reindex(idx, method="ffill").fillna(0)
            value = holding * price * usd_twd.reindex(idx, method="ffill").fillna(method="bfill")
        else:
            # 台股直接用台幣收盤價
            price = yf.download(code + ".TW", start=start, end=end)["Close"].reindex(idx, method="ffill").fillna(0)
            value = holding * price
        # 將該股票的每日市值加到df["stock"]
        df["stock"] += value

    # 處理債券類（00687B）
    for code in bond_codes:
        holding = calc_daily_holding(trade_df, code).reindex(idx, method="ffill").fillna(0)
        price = yf.download(code + ".TWO", start=start, end=end)["Close"].reindex(idx, method="ffill").fillna(0)
        value = holding * price
        df["bond"] += value

    # 處理加密貨幣類
    for code in crypto_codes:
        holding = calc_daily_holding(trade_df, code).reindex(idx, method="ffill").fillna(0)
        # 取得每日收盤價（以美金計價），ticker格式如 BTC-USD
        price = yf.download(code + "-USD", start=start, end=end)["Close"].reindex(idx, method="ffill").fillna(0)
        # 換算成台幣
        value = holding * price * usd_twd.reindex(idx, method="ffill").fillna(method="bfill")
        df["crypto"] += value

    # 計算每日總資產
    df["total"] = df["stock"] + df["bond"] + df["crypto"]

    # 畫總資產圖
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df["total"], label="Total Asset", color="black")
    plt.title("Total Portfolio Value (TWD)")
    plt.xlabel("Date")
    plt.ylabel("Total Value (TWD)")
    plt.legend()
    plt.grid()
    plt.show()

    # 畫分組資產圖
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df["stock"], label="Stock (VOO+006208+00919)")
    plt.plot(df.index, df["bond"], label="Bond (00687B)")
    plt.plot(df.index, df["crypto"], label="Crypto (Others)")
    plt.title("Asset Value by Category (TWD)")
    plt.xlabel("Date")
    plt.ylabel("Value (TWD)")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()