import numpy as np
import matplotlib.pyplot as plt


def barChart_array1D():
    # 月份
    months = np.array(["1", "2", "3", "4", "5", "6",
                      "7", "8", "9", "10", "11", "12"])
    # A商品銷量
    a = np.array([1000, 1200, 1350, 1250, 1330, 1240,
                 1150, 1250, 1230, 1300, 1320, 1400])

    # 設定圖表大小為10x6(英吋)
    plt.figure(figsize=(10, 6))
    # 設定柱狀圖寬度為0.4；預設為0.8
    plt.bar(months, a, width=0.4, label="A", color="orange")
    plt.title("Sales Volume")
    plt.xlabel("2025")
    plt.ylabel("Units")
    plt.legend(loc="best")
    # 只顯示y軸網格，而且為略透明虛線
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


def barChart_array2D():
    # 月份
    months = np.array(["1", "2", "3", "4", "5", "6",
                      "7", "8", "9", "10", "11", "12"])
    # A, B商品銷量皆存入2維陣列
    data = np.array([
        # A
        [1000, 1200, 1350, 1250, 1330, 1240, 1150,
            1250, 1230, 1300, 1320, 1400],
        # B
        [300, 320, 350, 315, 330, 340, 312, 325,
            330, 323, 335, 340]
    ])

    # 生成x座標: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    x = np.arange(len(months))
    # 設定柱狀體寬度
    bar_width = 0.4

    # 設定圖表大小為10x6(英吋)
    plt.figure(figsize=(10, 6))
    # 避免A、B商品柱狀體重疊，所以各佔一半寬度。原點在左下方，所以數值大偏右，小偏左
    # 例如1月: x為0
    # "x - bar_width/2"為"0 - 0.4/2"即為-0.2代表偏左;
    plt.bar(x - bar_width/2, data[0],
            width=bar_width, label="A", color="orange")
    # "x + bar_width/2"為"0 + 0.4/2"即為0.2代表偏右
    plt.bar(x + bar_width/2, data[1], width=bar_width, label="B", color="blue")
    # 設定x座標上的對應數值。例如1月: x為0，對應數值為1
    plt.xticks(x, months)
    plt.title("Sales Volume")
    plt.xlabel("2025")
    plt.ylabel("Units")
    plt.legend(loc="best")
    # 只顯示y軸網格，而且為略透明虛線
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


def main():
    # barChart_array1D()
    barChart_array2D()


if __name__ == "__main__":
    main()
