import numpy as np
import matplotlib.pyplot as plt


def hbarChart_array1D():
    # 月份
    months = np.array(["1", "2", "3", "4", "5", "6",
                      "7", "8", "9", "10", "11", "12"])
    # A商品銷量
    a = np.array([1000, 1200, 1350, 1250, 1330, 1240,
                 1150, 1250, 1230, 1300, 1320, 1400])

    plt.figure(figsize=(10, 6))
    # 設定柱狀圖寬度為0.4；預設為0.8；不設定顏色則自動配色
    plt.barh(months, a, height=0.4, label="A")
    plt.title("Sales Volume")
    plt.xlabel("Units")
    plt.ylabel("2025")
    plt.legend(loc="best")
    # 只顯示x軸網格，而且為略透明虛線
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.show()


def hbarChart_array2D():
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

    # 生成y座標: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y = np.arange(len(months))
    # 設定柱狀體高度
    bar_height = 0.4

    plt.figure(figsize=(10, 6))
    # 避免A、B商品柱狀體重疊，所以各佔一半高度。原點在左下方，所以數值大偏上，小偏下
    # 例如1月: x為0
    # "y - bar_height/2"為"0 - 0.4/2"即為-0.2代表偏下;
    plt.barh(y - bar_height/2, data[0], height=bar_height, label="A")
    # "y + bar_height/2"為"0 + 0.4/2"即為0.2代表偏上
    plt.barh(y + bar_height/2, data[1], height=bar_height, label="B")
    # 設定y座標上的對應數值。例如1月: y為0，對應數值為1
    plt.yticks(y, months)
    plt.title("Sales Volume")
    plt.xlabel("Units")
    plt.ylabel("2025")
    plt.legend(loc="best")
    # 只顯示x軸網格，而且為略透明虛線
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.show()


def main():
    hbarChart_array1D()
    hbarChart_array2D()


if __name__ == "__main__":
    main()
