from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf  # Yahoo Finance 下載股價資料


# 下載台積電(股票代號2330.TW)近5年的股價資料
def download_data():
    ticker = "2330.TW"
    df = yf.download(ticker, period="5y")
    print(df.head())
    return df


# 繪製股價時間序列圖
def time_series_line_chart(df: DataFrame):
    # 股價時間序列圖，就是折線圖，可顯示TSMC股價隨時間變化的趨勢，以觀察上升趨勢或波動區間
    plt.figure(figsize=(10, 6))
    # 只取日期(Date，目前為index)與收盤價(Close)來繪製line chart
    plt.plot(df.index, df['Close'], label='TSMC Close Price',
             color='blue', linewidth=1.5)
    # 設置圖表標題和標籤
    plt.title('TSMC Stock Price - Last 5 Years')
    plt.xlabel('Date')
    plt.ylabel('Close Price (TWD)')
    # 顯示圖例和網格
    plt.legend()
    plt.grid()
    # 調整X軸標籤角度以避免重疊
    plt.xticks(rotation=45)
    plt.show()


# 加入移動平均線 (Moving Average)
def moving_average_line_chart(df: DataFrame):
    # 計算50日和200日移動平均
    df["50_MA"] = df["Close"].rolling(window=50).mean()
    df["200_MA"] = df["Close"].rolling(window=200).mean()

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df["Close"], label="TSMC Close Price", color="blue")
    # 加入移動平均線 可用來平滑資料，幫助分析趨勢
    plt.plot(df.index, df["50_MA"], label="50-Day Moving Average",
             color="orange", linestyle="--", linewidth=2)
    plt.plot(df.index, df["200_MA"], label="200-Day Moving Average",
             color="green", linestyle="--", linewidth=2)

    # 設置圖表標題和標籤
    plt.title("TSMC Stock Price with Moving Averages - Last 5 Years")
    plt.xlabel("Date")
    plt.ylabel("Close Price (TWD)")
    # 顯示圖例和網格
    plt.legend()
    plt.grid()
    # 調整X軸標籤角度以避免重疊
    plt.xticks(rotation=45)
    plt.show()


# 繪製每日漲跌幅的分佈圖
def pct_change_histogram(df: DataFrame):
    # pct_change()計算每日變化率(每日報酬率)
    # 因為單位為%，需要乘以100，所以mul(100)
    df["returns"] = df["Close"].pct_change().mul(100)
    # return = (today's price - yesterday's price) / yesterday's price

    # 繪製直方圖 + KDE曲線，可以看到TSMC的報酬率分佈
    # 若呈現鐘形分佈，代表報酬率接近常態分佈
    plt.figure(figsize=(8, 4))
    sns.histplot(df["returns"].dropna(), kde=True, bins=50, color="green")
    plt.xlabel("Daily Return (%)")
    plt.ylabel("Frequency")
    plt.title("TSMC Daily Return Distribution")
    plt.show()


def main():
    df = download_data()
    time_series_line_chart(df)
    moving_average_line_chart(df)
    pct_change_histogram(df)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
