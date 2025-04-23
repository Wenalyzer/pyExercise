import numpy as np


# 1維陣列數學計算
def math_array1D():
    a1 = np.array([4, 5, 6])
    a2 = np.array([1, 2, 3])
    print("math_array1D()-測試資料")
    print(f"a1: {a1}")
    print(f"a2: {a2}")
    print("-----------------------------------")
    print(f"a1 + a2: {a1 + a2}")
    print(f"a1 - a2: {a1 - a2}")
    print(f"a1 * a2: {a1 * a2}")
    print(f"a1 ** a2: {a1 ** a2}")
    print(f"a1 / a2: {a1 / a2}")
    print(f"a1 % a2: {a1 % a2}")


# 2維陣列數學計算
def math_array2D():
    a1 = np.array([[7, 8, 9], [10, 11, 12]])
    # 2D可以跟1D運算，但所有的1D的shape必須相同
    a2 = np.array([1, 2, 3])
    # [1, 2, 3]即使2D結構，結果也相同
    # a2 = np.array([[1, 2, 3]])

    # 如果a2是2D陣列，則a1與a2的shape必須相同，否則錯誤
    # a2 = np.array([[1, 2, 3], [4, 5, 6]])
    print("math_array2D()-測試資料")
    print(f"a1:\n{a1}")
    print(f"a2:\n{a2}")
    print("-----------------------------------")
    print(f"a1 + a2:\n{a1 + a2}")
    print("-----------------------------------")
    print(f"a1 - a2:\n{a1 - a2}")
    print("-----------------------------------")
    print(f"a1 * a2:\n{a1 * a2}")
    print("-----------------------------------")
    print(f"a1 ** a2:\n{a1 ** a2}")
    print("-----------------------------------")
    print(f"a1 / a2:\n{a1 / a2}")
    print("-----------------------------------")
    print(f"a1 % a2:\n{a1 % a2}")


# 1維陣列排序
def sort_array1D():
    a1 = np.array([3, 6, 5, 4, 1, 2])
    print("sort_array1D()-測試資料")
    print(f"a1: {a1}")
    print("-----------------------------------")
    print(f"np.sort(a1): {np.sort(a1)}")


# 2維陣列排序
def sort_array2D():
    a2 = np.array(
        [[3, 11, 9],
         [5, 2, 15],
         [1, 6, 99]])
    print("sort_array2D()-測試資料")
    print(f"a2:\n{a2}")
    print("-----------------------------------")
    # axis=0代表列, axis=1代表欄
    print(f"np.sort(a2, axis=0):\n{np.sort(a2, axis=0)}")
    print("-----------------------------------")
    print(f"np.sort(a2, axis=1):\n{np.sort(a2, axis=1)}")


def main():
    math_array1D()
    print("===================================")
    math_array2D()
    print("===================================")
    sort_array1D()
    print("===================================")
    sort_array2D()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
