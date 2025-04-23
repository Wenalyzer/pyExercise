import numpy as np


# 1維陣列統計
def statistics_array1D():
    a1 = np.array([3, 5, 1])
    print("statistics_array1D()-測試資料")
    print(f"a1: {a1}")
    print("-----------------------------------")
    # 取最小值
    print(f"np.amin(a1): {np.amin(a1)}")
    # 取最大值
    print(f"np.amax(a1): {np.amax(a1)}")
    # 取最大與最小的差值
    print(f"np.ptp(a1): {np.ptp(a1)}")
    # 沿著axis 0取總和
    print(f"np.sum(a1): {np.sum(a1)}")
    # 取平均值
    print(f"np.mean(a1): {np.mean(a1)}")
    # average()也是算平均值，沒有加權則與mean()相同
    print(f"np.average(a1): {np.average(a1)}")
    # 有加權: ((3 * 1) + (5 * 2) + (1 * 3)) / (1 + 2 + 3) = 2.66666667
    print(f"np.average(a1, weights=[1, 2, 3]): {
          np.average(a1, weights=[1, 2, 3])}")
    # 中位數
    print(f"np.median(a1): {np.median(a1)}")
    # 取百分位數，第50分位數就是中位數
    print(f"np.percentile(a1, 50): {np.percentile(a1, 50)}")

    # 變異數(variance, σ^2 或 𝑠^2): 數列內每個數值與其平均值之差的平方的平均
    # np.var()的ddof預設為0，即N-0，N為數據的個數; 屬於母體變異數(Population Variance)，當擁有整個群體(母體)資料時使用
    # ddof=1，即N-1，N為數據的個數; 屬於樣本變異數(Sample Variance)，當只有部分群體(樣本)資料時使用
    print(f"np.var([1, 2, 3], ddof=0): {np.var([1, 2, 3], ddof=0)}")
    print(f"np.var([1, 20, 30], ddof=0): {np.var([1, 20, 30], ddof=0)}")
    # 標準差(Standard Deviation, σ 或 𝑠): 變異數的平方根
    print(f"np.std([1, 2, 3], ddof=0): {np.std([1, 2, 3])}")
    print(f"np.std([1, 20, 30], ddof=0): {np.std([1, 20, 30])}")
    # 變異數與標準差，都可測量一組數值的離散程度：
    # 值越大，代表數值分布越分散；值越小，代表數值接近平均值
    # 但有所不同：
    # 變異數：原資料單位的平方，不易理解
    # 標準差：與原資料相同的單位，可直接表示資料的波動範圍，易於理解，較常被使用


# 2維陣列統計
def statistics_array2D():
    a2 = np.array(
        [[3, 11, 9],
         [5, 2, 15],
         [1, 6, 99]])
    print("statistics_array2D()-測試資料")
    print(f"a2:\n{a2}")
    print("-----------------------------------")
    # 陣列所有值中的最小值，未指定axis會將array平面化看待
    print(f"np.amin(a2): {np.amin(a2)}")
    # 沿著axis 0取最小值
    print(f"np.amin(a2, axis=0): {np.amin(a2, axis=0)}")
    # 沿著axis 1取最小值
    print(f"np.amin(a2, axis=1): {np.amin(a2, axis=1)}")
    # 沿著axis 0取最大值
    print(f"np.amax(a2, axis=0): {np.amax(a2, axis=0)}")
    # 沿著axis 0取最大與最小的差值
    print(f"np.ptp(a2, axis=0): {np.ptp(a2, axis=0)}")
    # 沿著axis 0取總和
    print(f"np.sum(a2, axis=0): {np.sum(a2, axis=0)}")
    # 沿著axis 0取平均值
    print(f"np.mean(a2, axis=0): {np.mean(a2, axis=0)}")
    # average()也是算平均值，沒有加權則與mean()相同
    print(f"np.average(a2, axis=0): {np.average(a2, axis=0)}")
    # 加權計算
    # column1: ((3 * 1) + (5 * 2) + (1 * 3)) / (1 + 2 + 3) = 2.66666667
    # column2: ((11 * 1) + (2 * 2) + (6 * 3)) / (1 + 2 + 3) = 5.5
    # column2: ((9 * 1) + (15 * 2) + (99 * 3)) / (1 + 2 + 3) = 55
    print(f"np.average(a2, axis=0, weights=[1, 2, 3]): ")
    print(np.average(a2, axis=0, weights=[1, 2, 3]))

    # 沿著axis 0取中位數
    print(f"np.median(a2, axis=0): {np.median(a2, axis=0)}")
    # 沿著axis 0取百分位數，第50分位數就是中位數
    print(f"np.percentile(a2, 50, axis=0): {np.percentile(a2, 50, axis=0)}")

    # 變異數(方差，variance): 數列內每個數值與其平均值之差的平方的平均
    # 值越大，代表數值分布越分散；值越小，代表數值接近平均值
    # 變異數也是測量一組數值的離散程度，但比標準差更加放大數據的偏差
    # np.var()的ddof預設為0，即N-0，N為數據的個數; 屬於母體變異數(Population Variance)，當擁有整個群體(母體)資料時使用
    # ddof=1，即N-1，N為數據的個數; 屬於樣本變異數(Sample Variance)，當只有部分群體(樣本)資料時使用
    print(f"np.var(a2, axis=0, ddof=0)): {np.var(a2, axis=0, ddof=0)}")
    # 標準差(變異數的平方根): 測量一組數值的離散程度
    print(f"np.std(a2, axis=0, ddof=0): {np.std(a2, axis=0, ddof=0)}")


def main():
    statistics_array1D()
    print("===================================")
    statistics_array2D()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")