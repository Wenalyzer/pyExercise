from pandas import DataFrame


def count_data():
    df = DataFrame({
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'San Francisco', 'Chicago', 'Houston'],
        'Temperature': [30, 25, 20, 30, 18, 20, 35]
    })
    print("count_data()-測試資料")
    print(f"df:\n{df}")
    print("-----------------------------------")
    # 計算每個欄位總個數
    print(f"df.count():\n{df.count()}")
    print("-----------------------------------")
    # 計算每個欄位的唯一值總個數
    print(f"df.nunique():\n{df.nunique()}")
    print("-----------------------------------")
    # 計算每個值的出現次數
    print(f"df['City'].value_counts():\n{df['City'].value_counts()}\n")
    print(f"df['Temperature'].value_counts():\n{
          df['Temperature'].value_counts()}")


def calculate():
    df = DataFrame(
        [[3, 11, 9],
         [5, 2, 15],
         [1, 6, 99]])
    print("calculate()-測試資料")
    print(f"df:\n{df}")
    print("-----------------------------------")
    # 以下不設定axis則預設為0，代表依據欄位計算
    print(f"df.min():\n{df.min(axis=0)}")
    print("-----------------------------------")
    # 沿著axis 1取最小值
    print(f"df.min(axis=1):\n{df.min(axis=1)}")
    print("-----------------------------------")
    # 沿著axis 0取最大值
    print(f"df.max():\n{df.max()}")
    print("-----------------------------------")
    # 沿著axis 0取最大與最小的差值(相當於np.ptp(a2, axis=0))
    print(f"df.max() - df.min():\n{df.max() - df.min()}")
    print("-----------------------------------")
    # 沿著axis 0取總和
    print(f"df.sum():\n{df.sum()}")
    print("-----------------------------------")
    # 沿著axis 0取平均值
    print(f"df.mean():\n{df.mean()}")
    print("-----------------------------------")
    # 沿著axis 0取加權平均值(相當於np.average(a2, axis=0, weights=[1, 2, 3])
    weights = [1, 2, 3]
    # mul(multiply)：將每欄資料分別乘以指定list
    print(f"Weighted average:\n{
          (df.mul(weights, axis=0)).sum() / sum(weights)}")
    print("-----------------------------------")
    # 沿著axis 0取中位數
    print(f"df.median():\n{df.median()}")
    print("-----------------------------------")
    # 沿著axis 0取百分位數，第50分位數就是中位數
    print(f"df.quantile(0.5):\n{df.quantile(0.5)}")
    print("-----------------------------------")
    # 變異數(方差，variance): 數列內每個數值與其平均值之差的平方的平均
    # 值越大，代表數值分布越分散；值越小，代表數值接近平均值
    # 變異數也是測量一組數值的離散程度，但比標準差更加放大資料的偏差
    # df.var()的ddof預設為1，即N-1，N為資料的個數；屬於樣本變異數(Sample Variance)，當只有部分群體(樣本)資料時使用
    # ddof=0，即N-0; 屬於母體變異數(Population Variance)，當擁有整個群體(母體)資料時使用
    print(f"df.var():\n{df.var()}")
    print("-----------------------------------")
    # 標準差(變異數的平方根): 測量一組數值的離散程度
    print(f"df.std():\n{df.std()}")
    print("-----------------------------------")
    # 顯示前n筆資料，預設為5筆
    print(f"df.head(2):\n{df.head(2)}")
    print("-----------------------------------")
    # 顯示資料的相關統計描述
    print(f"df.describe():\n{df.describe()}")


def main():
    count_data()
    print("===================================")
    calculate()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")