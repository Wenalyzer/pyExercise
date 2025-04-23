import numpy as np


def create_array1D():
    print("建立1維陣列: ")
    # array內容來自list
    print(f"np.array([1, 2, 3]): {np.array([1, 2, 3])}")
    print("-----------------------------------")
    # 呼叫arange()建立1~10(不含)且差值為1的1維陣列
    print(f"np.arange(1, 10, 1): {np.arange(1, 10, 1)}")


def create_array2D():
    print("建立2維陣列: ")
    print(f"np.array([[1, 2, 3], [4, 5, 6]]):\n"
          f"{np.array([[1, 2, 3], [4, 5, 6]])}")
    print("-----------------------------------")
    # 建立2x3且初始值為0的整數2維陣列。不指定dtype則為float
    print(f"np.zeros((2, 3), dtype=int):\n"
          f"{np.zeros((2, 3), dtype=int)}")
    print("-----------------------------------")
    # 建立2x3且初始值為空字串的2維陣列
    print(f"np.empty((2, 3), dtype=str):\n"
          f"{np.empty((2, 3), dtype=str)}")
    print("-----------------------------------")
    # 建立2x3且初始值為1的2維陣列
    print(f"np.ones((2, 3), dtype=int):\n"
          f"{np.ones((2, 3), dtype=int)}")
    print("-----------------------------------")
    # 建立2x3且指定初始值為5的2維陣列
    print(f"np.full((2, 3), 5):\n"
          f"{np.full((2, 3), 5)}")
    print("-----------------------------------")
    # 建立2x3且亂數範圍[0, 1)的2維陣列
    print(f"np.random.rand(2, 3):\n"
          f"{np.random.rand(2, 3)}")
    print("-----------------------------------")
    # 建立2x3且亂數範圍[1, 100)的整數2維陣列
    print(f"np.random.randint(1, 100, (2, 3)):\n"
          f"{np.random.randint(1, 100, (2, 3))}")
    print("-----------------------------------")
    # 建立2x3且亂數範圍[1, 100)的浮點數2維陣列
    print(f"np.random.uniform(1, 100, (2, 3)):\n"
          f"{np.random.uniform(1, 100, (2, 3))}")


def main():
    create_array1D()
    print("===================================")
    create_array2D()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
