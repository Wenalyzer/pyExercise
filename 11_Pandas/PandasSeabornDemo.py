import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# line, bar chart測試資料
months = np.array(["1", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "11", "12"])
a = np.array([1000, 1200, 1350, 1250, 1330, 1240,
             1150, 1250, 1230, 1300, 1320, 1400])
b = np.array([300, 320, 350, 315, 330, 340, 312, 325, 330, 323, 335, 340])


def lineChart():
    # 將array資料轉成DataFrame
    df = pd.DataFrame(
        {"months": months, "A": a, "B": b}
    )
    print(df)
    print("-----------------------------------")
    # 呼叫melt()轉成可繪圖的資料結構，可參看「資料重塑」相關說明
    df = df.melt(
        # 指定由"months"來擔當index
        id_vars="months",
        # 指定欄位的變數名稱為"products"，在此"products"為"A", "B"
        var_name="products",
        # 指定值的變數名稱為"sales"，在此"sales"為a, b
        value_name="sales"
    )
    print("after melt()\n", df)

    plt.figure(figsize=(10, 6))
    sns.lineplot(
        # hue="products"為依據products欄位的值來區分不同產品的線條顏色
        data=df, x="months", y="sales", hue="products",
        # 設定顏色以及各商品要使用標記(但標記樣式無法指定)
        palette={"A": "orange", "B": "blue"}, style="products", markers=True)
    plt.title("Sales Volume")
    plt.xlabel("2025")
    plt.ylabel("Units")
    plt.legend(loc="best")
    plt.grid()
    plt.show()


def barChart():
    df = pd.DataFrame({"months": months, "A": a, "B": b}).melt(
        id_vars="months", var_name="products", value_name="sales")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="months", y="sales", hue="products",
                palette={"A": "orange", "B": "blue"})
    plt.title("Sales Volume")
    plt.xlabel("2025")
    plt.ylabel("Units")
    plt.legend(loc="best")
    # 只顯示y軸網格，而且為略透明虛線
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


def hbarChart():
    df = pd.DataFrame({"months": months, "A": a, "B": b}).melt(
        id_vars="months", var_name="products", value_name="sales")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, y="months", x="sales", hue="products",
                palette={"A": "orange", "B": "blue"})
    plt.title("Sales Volume")
    plt.xlabel("Units")
    plt.ylabel("2025")
    plt.legend(loc="best")
    # 只顯示x軸網格，而且為略透明虛線
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.show()


def main():
    lineChart()
    barChart()
    hbarChart()

    # seaborn不支援Pie Chart


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")