import numpy as np


def read():
    a1 = np.array([1, 2, 3, 4, 5, 6])
    print(f"read()-測試資料")
    print(f"a1: {a1}")
    print("-----------------------------------")
    print("1維陣列取值:")
    # 取索引為0的元素值
    print(f"a1[0]: {a1[0]}")
    # 取索引0到3(不含)的元素值
    print(f"a1[:3]: {a1[:3]}")

    print("走訪1維陣列: ", end="")
    for number in a1:
        print(number, end=" ")
    print()
    print("-----------------------------------")

    print("下列2種取出陣列局部的功能相同，都會參照到原陣列:")
    print(f"a1[slice(0, 3)]等於a1[slice(3)]: {a1[slice(3)]}")
    # slice()的簡易版
    print(f"a1[:3]: {a1[:3]}")
    print("-----------------------------------")
    print("取出的陣列局部，若修改會影響原始陣列")
    arr_slice = a1[:3]
    print(f"arr_slice修改前: {arr_slice}")
    arr_slice[0] = 10
    print(f"arr_slice修改後: {arr_slice}")
    print(f"a1(原陣列): {a1}")


def add():
    a1 = np.array([1, 2, 3, 4, 5, 6])
    print(f"add()-測試資料")
    print(f"a1: {a1}")
    print("-----------------------------------")
    print("1維陣列附加，新增(會產生新的陣列):")
    print(f"np.append(a1, 7): {np.append(a1, 7)}")
    print(f"np.insert(a1, 0, 8): {np.insert(a1, 0, 8)}")


def update():
    a1 = np.array([1, 2, 3, 4, 5, 6])
    print(f"update()-測試資料")
    print(f"a1: {a1}")
    print("-----------------------------------")
    print("1維陣列修改(修改原陣列):")
    a1[0] = 100
    print(f"a1[0] = 100: {a1}")


def delete():
    a1 = np.array([1, 2, 3, 4, 5, 6])
    print(f"delete()-測試資料")
    print(f"a1: {a1}")
    print("-----------------------------------")
    print("1維陣列刪除(會產生新的陣列):")
    print(f"np.delete(a1, 0): {np.delete(a1, 0)}")


def main():
    read()
    print("===================================")
    add()
    print("===================================")
    update()
    print("===================================")
    delete()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
