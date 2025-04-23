import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 不支援中文字型，搜尋並下載「Noto Fonts TC」，解壓縮後隨意複製一個文字檔案到專案內
# 建立FontProperties物件指定字型檔案名稱
font = FontProperties(fname="10_NumPy/NotoSansTC-Regular.otf", size=10)


def lineChart_array1D():
    # 月份
    months = np.array(["1月", "2月", "3月", "4月", "5月", "6月",
                      "7月", "8月", "9月", "10月", "11月", "12月"])
    # A, B商品銷量各為1維陣列
    a = np.array([1000, 1200, 1350, 1250, 1330, 1240,
                 1150, 1250, 1230, 1300, 1320, 1400])
    b = np.array([300, 320, 350, 315, 330, 340, 312, 325,
                  330, 323, 335, 340])

    # 設定圖表大小為10x6(英吋)
    plt.figure(figsize=(10, 6))
    # x軸, y軸, 標記, 線條顏色, 資料點樣式(https://matplotlib.org/stable/api/markers_api.html)
    plt.plot(months, a, label="A", color="orange", marker=".")
    plt.plot(months, b, label="B", color="blue", marker="o")
    plt.title("銷售量", fontproperties=font)
    plt.xlabel("2025年", fontproperties=font)
    plt.ylabel("個數", fontproperties=font)
    # x與y軸的值可能有中文，需要設定字型
    plt.xticks(fontproperties=font)
    plt.yticks(fontproperties=font)
    # 設定圖例在最佳位置
    plt.legend(loc="best")
    # 加網格
    plt.grid()
    # 將繪圖結果顯示
    plt.show()


def lineChart_array2D():
    months = np.array(["1月", "2月", "3月", "4月", "5月", "6月",
                      "7月", "8月", "9月", "10月", "11月", "12月"])
    # A, B商品銷量皆存入2維陣列
    data = np.array([
        [1000, 1200, 1350, 1250, 1330, 1240, 1150,
            1250, 1230, 1300, 1320, 1400],  # A
        [300, 320, 350, 315, 330, 340, 312, 325,
            330, 323, 335, 340]             # B
    ])

    # 設定圖表大小為10x6(英吋)
    plt.figure(figsize=(10, 6))
    # 轉置後，每一行分別對應A和B
    plt.plot(months, data.T, marker="o")
    # 設定圖例(顏色會自動配置)
    # 圖例原錨點位置在(0, 0)，就是在圖表的左下方
    # bbox_to_anchor=(1, 1): 代表圖例新的錨點位置設在圖表右上方邊界
    # loc="upper left": 代表圖例的左上端對齊新的錨點(所以圖例會在錨點右下方)
    plt.legend(["A", "B"], bbox_to_anchor=(1, 1), loc="upper left")

    plt.title("銷售量", fontproperties=font)
    plt.xlabel("2025年", fontproperties=font)
    plt.ylabel("個數", fontproperties=font)
    # x與y軸的值可能有中文，需要設定字型
    plt.xticks(fontproperties=font)
    plt.yticks(fontproperties=font)
    # 加網格
    plt.grid()
    # 將繪圖結果顯示
    plt.show()


def main():
    lineChart_array1D()
    # lineChart_array2D()


if __name__ == "__main__":
    main()
