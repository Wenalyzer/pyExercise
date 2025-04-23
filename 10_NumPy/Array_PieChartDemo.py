import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 不支援中文字型，搜尋並下載「Noto Fonts TC」，解壓縮後隨意複製一個文字檔案到專案內
# 建立FontProperties物件指定字型檔案名稱
font = FontProperties(fname="10_NumPy/NotoSansTC-Regular.otf", size=10)


def pieChart():
    # 各商品單月銷量
    sales = [1000, 250, 200, 150, 100]
    labels = ["商品A", "商品B", "商品C", "商品D", "商品E"]
    # 顏色
    colors = ["brown", "cyan", "green", "yellow", "orange"]
    # 設定圖表大小為10x6(英吋)
    plt.figure(figsize=(10, 6))
    plt.title("7月銷售量", fontproperties=font)
    # pie chart
    # autopct：值以百分比顯示
    # startangle：第一個資料起始度數，0度代表從x軸開始(3點鐘方向)，正度數代表逆時鐘
    # wedgeprops={"width": 0.6}：設定資料圓形佔比，0.6代表佔60%，內圓則佔40%
    # textprops={"fontproperties": font}：中文需要設定字型屬性
    plt.pie(
        x=sales,
        labels=labels,
        colors=colors,
        autopct='%.2f%%',
        startangle=90,
        wedgeprops={"width": 0.6},
        textprops={"fontproperties": font}
    )
    plt.yticks(fontproperties=font)
    # 加圖例並設定字型
    plt.legend(loc="best", prop=font)
    plt.show()


def main():
    pieChart()


if __name__ == "__main__":
    main()
