from pandas import DataFrame
from pandas import Series


def math():
    df1 = DataFrame([[7, 8, 9], [10, 11, 12]])
    # 2D可以跟1D運算，但所有的1D的shape必須相同，否則產生NaN
    df2 = Series([1, 2, 3])

    # 如果df2是2D陣列，則df1與df2的shape必須相同，否則產生NaN
    # df2 = DataFrame([[1, 2, 3], [4, 5, 6]])
    print("math()-測試資料")
    print(f"df1:\n{df1}\n")
    print(f"df2:\n{df2}")
    print("-----------------------------------")
    print(f"df1 + df2:\n{df1 + df2}")
    print("-----------------------------------")
    print(f"df1 - df2:\n{df1 - df2}")
    print("-----------------------------------")
    print(f"df1 * df2:\n{df1 * df2}")
    print("-----------------------------------")
    print(f"df1 ** df2:\n{df1 ** df2}")
    print("-----------------------------------")
    print(f"df1 / df2:\n{df1 / df2}")
    print("-----------------------------------")
    print(f"df1 % df2:\n{df1 % df2}")


def sort():
    df = DataFrame(
        [[3, 11, 9],
         [5, 2, 15],
         [1, 6, 99]])
    print(f"sort()-測試資料")
    print(f"df:\n{df}")
    print("-----------------------------------")
    # "by=0"僅將第一欄排序
    print(f"df.sort_values(by=0, axis=0):\n{df.sort_values(by=0, axis=0)}")
    # 如果有欄位名稱，則可以用欄位名稱排序
    print("-----------------------------------")
    df.columns = ['A', 'B', 'C']
    print(f"df.sort_values(by='A', axis=0):\n{df.sort_values(by='A', axis=0)}")
    print("-----------------------------------")
    # 僅將第一列排序
    print(f"df.sort_values(by=0, axis=1):\n{df.sort_values(by=0, axis=1)}")
    print("-----------------------------------")
    # 每列各自排序，類似array
    print(f"df.apply(sorted, axis=1):\n{df.apply(sorted, axis=1)}")


def main():
    math()
    print("===================================")
    sort()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")