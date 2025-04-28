from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 計算偏態
def skewness(df):
    skewness = df["Score"].skew()
    print(f"Skewness: {skewness:.3f}")
    # 偏態 (skewness) 衡量資料的對稱性，描述資料是否向左或向右偏斜:
    # skew() > 0 (正偏態, Right-skewed, Positive-skewed)：大部分資料集中在較小值，右側有長尾巴 (如考試較難)。
    # skew() = 0 (對稱, Symmetric)：資料接近對稱 (鐘形曲線)。
    # skew() < 0 (負偏態, Left-skewed, Negative-skewed)：大部分資料集中在較大值，左側有長尾巴 (如考試簡單)。
    # -----------------------------------
    # 輸出結果說明：
    # Skewness = -0.259 (輕微負偏態)：
    # 負偏態代表考試較容易，大部分學生都考得不錯。
    # 大部分學生的分數集中在較高區間 (如 70-90 分)，但仍有一些學生考得比較低，稍微拉低了分佈。


# 計算峰度
def kurtosis(df):
    kurtosis = df["Score"].kurt()
    print(f"Kurtosis: {kurtosis:.3f}")
    # 峰度 (Kurtosis) 衡量資料的尾部厚度，也就是分佈是否具有較多極端值。
    # kurt() > 0 (高峽峰, Leptokurtic)：分佈尖峰較高，表示有更多極端值 (長尾效應)。
    # kurt() = 0 (常態峰, Mesokurtic)：接近正態分佈。
    # kurt() < 0 (低闊峰, Platykurtic)：分佈較平坦，極端值較少。
    # -----------------------------------
    # 輸出結果說明：
    # Kurtosis = -0.225 (低闊峰)：
    # 低闊峰代表極端值較少，分數較平均，不像常態峰那樣有明顯的峰值。
    # 資料較為分散，沒有太多的極端高分或極端低分。


# 畫出直方圖，顯示資料的頻率分佈
def histogram(df):
    # KDE(Kernel Density Estimation)為True會繪製平滑的分佈趨勢線
    # bins代表直方圖的分組數量，預設是auto(自動計算)
    sns.histplot(df["Score"], kde=True, bins=10, color="blue")

    # 顯示標題與標籤
    skewness = df["Score"].skew()
    kurtosis = df["Score"].kurt()
    plt.title(f"Exam Scores Distribution\nSkewness: {
              skewness:.3f}, Kurtosis: {kurtosis:.3f}")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()


def main():
    # 設定隨機種子以確保結果一致
    np.random.seed(10)
    # normal()產生常態分布陣列，生成平均75分，標準差10，30人的分數
    scores = np.random.normal(loc=75, scale=10, size=30)
    # 確保分數介於[0,100]：分數<0為0；分數>100為100
    scores = np.clip(scores, 0, 100)
    # 建立 DataFrame
    df = DataFrame({"Score": scores})
    print("測試資料")
    print(f"df.sort_values():\n{df.sort_values(by="Score")}")
    print("-----------------------------------")
    print(f"df.describe():\n{df.describe()}")

    skewness(df)
    kurtosis(df)
    histogram(df)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
