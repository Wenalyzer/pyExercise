import numpy as np


def read():
    a2 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
    print(f"read()-測試資料")
    print(f"a2:\n{a2}")
    print("-----------------------------------")
    print("2維陣列取值:")
    # 取列索引0到2(不含)，欄索引為1的元素值
    print(f"a2[:2, 1]: {a2[:2, 1]}")
    # 取每列，欄索引為0的元素值
    print(f"a2[:, 0]: {a2[:, 0]}")
    # 取列索引0的每個欄位值
    print(f"a2[0, :]: {a2[0, :]}")
    # 取列索引1到最後，欄索引為1到最後的元素值
    print(f"a2[1:, 1:]:\n{a2[1:, 1:]}")
    # 取列索引1, 2，欄索引1, 2的元素值
    print(f"a2[(1, 2), (1, 2)]: {a2[(1, 2), (1, 2)]}")
    print("-----------------------------------")
    # 走訪2維陣列
    print("for-nested走訪2維陣列:")
    for arr in a2:
        for number in arr:
            print(number, end=" ")
        print()
    print("-----------------------------------")
    print("np.nditer()走訪2維陣列:")
    for number in np.nditer(a2):
        print(number, end=" ")
    print()


def add():
    a2 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
    print(f"add()-測試資料")
    print(f"a2:\n{a2}")
    print("-----------------------------------")
    print("2維陣列附加、新增(會產生新的陣列):")

    # 未指定axis會將array與附加的值平面化
    print("未指定axis會將陣列與附加的值平面化，所以[10, 11, 12]與[[10, 11, 12]]結果一樣")
    print(f"np.append(a2, [10, 11, 12]):\n{np.append(a2, [10, 11, 12])}")
    print(f"np.append(a2, [[10, 11, 12]]):\n{np.append(a2, [[10, 11, 12]])}")
    print("-----------------------------------")

    # 指定axis=0, 代表要新增列
    print("append(): 2維陣列附加一列，該列需為2維資料: [[10, 11, 12]]")
    print("np.append(a2, [[10, 11, 12]], axis=0):")
    print(np.append(a2, [[10, 11, 12]], axis=0))
    print("-----------------------------------")
    print("insert()有指定是哪一列，所以新增1維資料: [10, 11, 12]")
    print(f"np.insert(a2, 1, [10, 11, 12], axis=0):")
    print(np.insert(a2, 1, [10, 11, 12], axis=0))
    print("-----------------------------------")

    # 指定axis=1, 代表要新增欄
    print("append(): 2維陣列附加一欄，該欄需為2維資料: [[10], [11], [12]]，否則產生ValueError")
    print(f"np.append(a2, [[10], [11], [12]], axis=1)")
    print(np.append(a2, [[10], [11], [12]], axis=1))
    print("-----------------------------------")
    print("附加的一欄若為[[10, 11, 12]]，需先transpose()處理後方可附加")
    print(f"np.transpose([[10, 11, 12]]):\n{np.transpose([[10, 11, 12]])}")
    print(f"np.append(a2, np.transpose([[10, 11, 12]]), axis=1)")
    print(np.append(a2, np.transpose([[10, 11, 12]]), axis=1))
    print("-----------------------------------")
    print("insert()有指定是哪一欄，所以新增1維資料: [10, 11, 12]")
    print(f"np.insert(a2, 1, [10, 11, 12], axis=1)")
    print(np.insert(a2, 1, [10, 11, 12], axis=1))


def update():
    a2 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
    print(f"update()-測試資料")
    print(f"a2:\n{a2}")
    print("-----------------------------------")
    print("2維陣列修改(修改原陣列):")
    # 修改單一值
    a2[0, 1] = 100
    print(f"a2[0, 1] = 100:\n{a2}\n")
    # 修改一列
    a2[1] = [14, 15, 16]
    print(f"a2[1] = [14, 15, 16]:\n{a2}\n")
    # 修改一欄
    a2[:, 0] = [1, 41, 17]
    print(f"a2[:, 0] = [1, 41, 17]:\n{a2}")


def delete():
    a2 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
    print(f"delete()-測試資料")
    print(f"a2:\n{a2}")
    print("-----------------------------------")
    print("2維陣列刪除(會產生新的陣列):")
    print(f"np.delete(a2, 0, axis=0):\n{np.delete(a2, 0, axis=0)}")
    print(f"np.delete(a2, 0, axis=1):\n{np.delete(a2, 0, axis=1)}")


def reshape():
    # 重構(會產生新的陣列)
    a1 = np.array([1, 2, 3, 4, 5, 6])
    print(f"reshape()-測試資料")
    print(f"a1: {a1}")
    print("1維陣列重構維度:")
    print(f"b = a1.reshape(2, 3):\n{a1.reshape(2, 3)}")
    print("-----------------------------------")

    # 展開
    a2 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
    print(f"a2:\n{a2}")
    print("2維陣列展開:")
    print(f"a2.ravel(): {a2.ravel()}")
    print("2維陣列的列與欄位置轉置，下列2種方式功能相同:")
    print(f"np.transpose(a2):\n{np.transpose(a2)}")
    # transpose()的簡易版
    print(f"a2.T:\n{a2.T}")


def main():
    read()
    print("===================================")
    add()
    print("===================================")
    update()
    print("===================================")
    delete()
    print("===================================")
    reshape()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
