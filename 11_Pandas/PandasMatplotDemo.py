import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def pieChart():
    df = pd.DataFrame({
        "labels": ["A", "B", "C", "D", "E"],
        "sales": [1000, 250, 200, 150, 100],
        "colors": ["brown", "cyan", "green", "yellow", "orange"]
    }).set_index("labels")
    print(f"df:\n{df}")
    ax = df["sales"].plot(
        kind="pie",
        figsize=(8, 8),
        autopct="%.2f%%",
        startangle=90,
        wedgeprops={"width": 0.6},
        colors=df["colors"]
    )
    ax.set_title("Sales Volume - July")
    # 隱藏x, y軸標籤
    ax.set_xlabel("")
    ax.set_ylabel("")
    plt.legend(loc="best")
    # 將圖存檔；必須在plt.show()之前執行，否則存檔一片白
    plt.savefig("11_Pandas/PandasMatplotDemo")
    plt.show()


def lineChart(df):
    ax = df.plot(
        kind="line",
        # 設定圖表大小為10x6(英吋)
        figsize=(10, 6),
        # 資料點樣式(https://matplotlib.org/stable/api/markers_api.html)
        marker="o",
        color={"A": "orange", "B": "blue"}
    )
    # 下兩行都需要方能顯示所有月份，否則顯示1, 3, 5, 7, 9, 11
    # 將x軸刻度分成12段
    ax.set_xticks(range(len(df.index)))
    # 將x軸刻度上的標籤填入index值
    ax.set_xticklabels(df.index)

    ax.set_title("Sales Volume")
    ax.set_xlabel("2025")
    ax.set_ylabel("Units")
    # ax.legend(loc="best")
    ax.grid()
    # 圖例原錨點位置在(0, 0)，就是在圖表的左下方
    # bbox_to_anchor=(1, 1): 代表圖例新的錨點位置設在圖表右上方邊界
    # loc="upper left": 代表圖例的左上端對齊新的錨點(所以圖例會在錨點右下方)
    plt.legend(["A", "B"], bbox_to_anchor=(1, 1), loc="upper left")
    plt.show()


def barChart(df):
    # 下列方式繪製bar chart不會重疊，但使用plt.bar()會重疊
    ax = df.plot(
        kind="bar",
        figsize=(10, 6),
        color={"A": "orange", "B": "blue"}
    )
    # 只有bar chart的x軸刻度上的標籤預設旋轉90度，需加此行轉正
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.set_title("Sales Volume")
    ax.set_xlabel("2025")
    ax.set_ylabel("Units")
    ax.legend(loc="best")
    # 只顯示y軸網格，而且為略透明虛線，alpha=0.7代表70%不透明
    # linestyle樣式：https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


def hbarChart(df):
    ax = df.plot(
        kind="barh",
        figsize=(10, 6),
        color={"A": "orange", "B": "blue"}
    )
    ax.set_title("Sales Volume")
    ax.set_xlabel("Units")
    ax.set_ylabel("2025")
    ax.legend(loc="best")
    ax.grid(axis="x", linestyle="--", alpha=0.7)
    plt.show()


def main():
    # pieChart()

    # line/bar chart測試資料
    months = np.array(["1", "2", "3", "4", "5", "6",
                      "7", "8", "9", "10", "11", "12"])
    A = np.array([1000, 1200, 1350, 1250, 1330, 1240,
                 1150, 1250, 1230, 1300, 1320, 1400])
    B = np.array([300, 320, 350, 315, 330, 340, 312, 325, 330, 323, 335, 340])
    df = pd.DataFrame({
        "months": months,
        "A": A,
        "B": B
    }).set_index("months")  # 將月份設為索引
    print("line/bar chart測試資料")
    print(df)

    # lineChart(df)
    # barChart(df)
    # hbarChart(df)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
