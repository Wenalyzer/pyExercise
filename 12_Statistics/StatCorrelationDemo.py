from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 計算相關係數
def correlation():
    # Apple(AAPL)、Microsoft(MSFT)和Alphabet(GOOGL) 10天的真實股價
    df = DataFrame({
        "Date": ["2025-01-22", "2025-01-23", "2025-01-24", "2025-01-25", "2025-01-26",
                 "2025-01-27", "2025-01-28", "2025-01-29", "2025-01-30", "2025-01-31"],
        "AAPL": [240.50, 242.00, 241.00, 243.50, 245.00, 244.00, 246.50, 247.00, 248.50, 236.00],
        "MSFT": [420.00, 422.50, 421.00, 423.00, 425.50, 424.00, 426.50, 427.00, 428.50, 415.06],
        "GOOGL": [200.00, 202.50, 201.00, 203.00, 205.50, 204.00, 206.50, 207.00, 208.50, 204.02]
    })
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    # print(f"df:\n{df}\n")

    # 計算相關係數，並取小數3位
    print(f"Correlation Matrix:\n{df.corr().round(3)}")
    # 相關係數 (Correlation coefficient) 顯示資料之間的相關性，數值範圍 -1 到 1：
    # corr() = 1.0：完全正相關 (例如股價同步變動)
    # corr() = 0.0：無相關
    # corr() = -1.0：完全負相關 (例如股價反向變動)
    # 不受數值單位影響，所以可以評估不同類型的資料
    # -----------------------------------
    # 輸出結果說明：
    # 1. AAPL 與 MSFT (0.996)
    # 相關性接近 1.0，表示 AAPL 和 MSFT 股價變動趨勢極為相似。
    # 這可能是因為兩家公司提供的商品或服務類似，所以市場波動趨勢相近。
    # 2. AAPL 與 GOOGL (0.720)
    # 相關性約 0.72，代表中等程度的正相關；可能因為 AAPL 與 GOOGL 都屬於科技業，所以市場波動仍有一定的相似程度。
    # 變動方向大致相同，但同步性不如 AAPL-MSFT。
    # 3. MSFT 與 GOOGL (0.699)
    # 相關性約 0.70，表示 MSFT 與 GOOGL 也有一定程度的正相關。
    # 但與 AAPL-MSFT 的高度相關相比，MSFT-GOOGL 的聯動性較低。
    # 總結：AAPL 和 MSFT 相關性最高，表示這兩間公司的股價變動幾乎同步，而 GOOGL 與它們的相關性稍微較低，可能因為商業模式或市場影響因素不同。


# 計算共變異數
def covariance():
    # Apple(AAPL)、Microsoft(MSFT)和Alphabet(GOOGL) 10天的真實股價
    df = DataFrame({
        "Date": ["2025-01-22", "2025-01-23", "2025-01-24", "2025-01-25", "2025-01-26",
                 "2025-01-27", "2025-01-28", "2025-01-29", "2025-01-30", "2025-01-31"],
        "AAPL": [240.50, 242.00, 241.00, 243.50, 245.00, 244.00, 246.50, 247.00, 248.50, 236.00],
        "MSFT": [420.00, 422.50, 421.00, 423.00, 425.50, 424.00, 426.50, 427.00, 428.50, 415.06],
        "GOOGL": [200.00, 202.50, 201.00, 203.00, 205.50, 204.00, 206.50, 207.00, 208.50, 204.02]
    })
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    # 計算共變異數，並取小數3位
    print(f"Covariance Matrix:\n{df.cov().round(3)}")
    # 共變異數 (Covariance) 顯示資料共同變動程度，但這個值沒有標準範圍，因為它受到單位影響，不適合比較不同單位的數值
    # 如果想要衡量「變數之間的關聯強度」，建議使用 corr() (相關係數) 而不是 cov() (共變異數)。
    # 1. cov() > 0：
    # 正相關，即當 A 增加，B 也傾向增加，反之亦然。
    # 數值越大，表示變動的幅度越大，兩者的變化趨勢更一致。
    # 2. cov() < 0：
    # 負相關，即當 A 增加，B 傾向減少，反之亦然。
    # 負的越多，表示變動方向越相反。
    # 3. cov() ≈ 0：
    # 幾乎沒有線性關係，即 A 的變化與 B 沒有固定的趨勢。
    # -----------------------------------
    # 輸出結果說明：
    # 1. AAPL 和 MSFT 共變異數較大 (14.540)
    # 代表這兩隻股票的股價起伏幅度相似，當 AAPL 漲跌時，MSFT 也會有類似變動。
    # 2. GOOGL 與其他股票的共變異數較小 (7.172 - 7.469)
    # 這表示 GOOGL 的股價變動與 AAPL/MSFT 相比，波動程度較低。
    # 換句話說，GOOGL 不會像 AAPL 和 MSFT 那麼同步變動。
    # 3. AAPL、MSFT 的自變異數 (Variance) 高於 GOOGL
    # AAPL (13.600) 和 MSFT (15.679) 的波動性較高，股價漲跌幅度比 GOOGL 更大。
    # GOOGL (7.288) 相對較穩定，股價變動幅度較小。
    # 總結：AAPL 和 MSFT 的波動性最大，且共同變動最多，而 GOOGL 相對較獨立，與 AAPL 和 MSFT 的聯動性較低。


# 使用 seaborn 繪製 AAPL vs MSFT 迴歸圖(Regression Plot)
def regression_plot():
    # Apple(AAPL)、Microsoft(MSFT)和Alphabet(GOOGL) 10天的真實股價
    df = DataFrame({
        "Date": ["2025-01-22", "2025-01-23", "2025-01-24", "2025-01-25", "2025-01-26",
                 "2025-01-27", "2025-01-28", "2025-01-29", "2025-01-30", "2025-01-31"],
        "AAPL": [240.50, 242.00, 241.00, 243.50, 245.00, 244.00, 246.50, 247.00, 248.50, 236.00],
        "MSFT": [420.00, 422.50, 421.00, 423.00, 425.50, 424.00, 426.50, 427.00, 428.50, 415.06],
        "GOOGL": [200.00, 202.50, 201.00, 203.00, 205.50, 204.00, 206.50, 207.00, 208.50, 204.02]
    })
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    # scatter_kws={"s": 50}：設定點的大小
    # line_kws={"color": "red"}：設定迴歸線顏色為紅色
    sns.regplot(
        x=df["AAPL"], y=df["MSFT"],
        scatter_kws={"s": 50},
        line_kws={"color": "red"}
    )

    # 設定標題與標籤
    plt.title("Regression Plot: AAPL vs MSFT")
    plt.xlabel("AAPL Stock Price")
    plt.ylabel("MSFT Stock Price")
    plt.show()


def main():
    correlation()
    print("===================================")
    covariance()
    print("===================================")
    regression_plot()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")