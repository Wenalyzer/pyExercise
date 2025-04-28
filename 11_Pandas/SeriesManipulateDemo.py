import numpy as np
from pandas import Series


def create():
    print("Series內容來自list")
    # Series()的「Series()」是呼叫建構式而非一般函式
    seriesList = Series(
        ["Python", "Java", "JS", "Swift", "C#"],
        dtype="string"
    )
    print(f"seriesList:\n{seriesList}")
    print("-----------------------------------")

    print("series內容來自ndarray")
    array = np.array(["Python", "Java", "JS", "Swift", "C#"])
    seriesArray = Series(array)
    print(f"seriesArray:\n{seriesArray}")
    print("-----------------------------------")

    print("series內容來自dictionary")
    seriesDic = Series({
        "name": "Python",
        "price": 500,
        "author": "Paul"
    })
    print(f"seriesDic:\n{seriesDic}")


def info():
    series = Series({
        "name": "Python",
        "price": 500,
        "author": "Paul"
    })
    print(f"info()-測試資料")
    print(f"series:\n{series}")
    print("-----------------------------------")
    print("Series相關資訊")
    print(f"series.dtype: {series.dtype}")
    print(f"series.shape: {series.shape}")
    print(f"series.memory_usage(): {series.memory_usage()} bytes")
    print(f"series.count: {series.count()}")


def convert_to():
    series = Series({
        "name": "Python",
        "price": 500,
        "author": "Paul"
    })
    print(f"convert_to()-測試資料")
    print(f"series:\n{series}")
    print("-----------------------------------")
    print("series轉list")
    print(f"series.tolist(): {series.tolist()}")
    print("-----------------------------------")

    print("series轉ndarray")
    print(f"series.to_numpy(): {series.to_numpy()}")
    print("-----------------------------------")

    print("series轉dictionary")
    print(f"series.to_dict(): {series.to_dict()}")


def read():
    series = Series(["Python", 500, "Paul"])
    print(f"read()-測試資料")
    print(f"series:\n{series}")
    print("-----------------------------------")
    print("預設有index供存取")
    # 取index=0的值
    print(f"series[0]: {series[0]}")
    print("-----------------------------------")

    # 取index=[0]的series
    print(f"Series(series, index=[0]):\n"
          f"{Series(series, index=[0])}")
    print("-----------------------------------")

    # 取index=[0, 1]的series
    print(f"Series(series, index=[0, 1]):\n"
          f"{Series(series, index=[0, 1])}")
    print("-----------------------------------")

    print(f"加上index label:\nseries.index = ['name', 'price', 'author']")
    series.index = ["name", "price", "author"]
    print(f"series:\n{series}\n")
    print("可透過index label存取")
    # 取index=['name', 'price']的series
    print(f"Series(series, index=['name', 'price']):")
    print(Series(series, index=['name', 'price']))
    print("-----------------------------------")

    print("走訪Series(for value in series:)")
    for value in series:
        print(value, end=" ")
    print()
    print("走訪Series(for index, value in series.items():)")
    for index, value in series.items():
        print(f"index: {index}, value: {value}")


def add():
    series = Series({
        "name": "Python",
        "price": 500,
        "author": "Paul"
    })
    print(f"add()-測試資料")
    print(f"series:\n{series}")
    print("-----------------------------------")
    print(f"新增isbn屬性與值:\nseries['isbn'] = '123456'")
    series["isbn"] = "123456"
    print(f"series:\n{series}")


def update():
    series = Series({
        "name": "Python",
        "price": 500,
        "author": "Paul"
    })
    print(f"update()-測試資料")
    print(f"series:\n{series}")
    print("-----------------------------------")
    print(f"修改author屬性值\nseries['author'] = 'Peter'")
    series["author"] = "Peter"
    print(f"series:\n{series}")


def delete():
    series = Series({
        "name": "Python",
        "price": 500,
        "author": "Paul"
    })
    print(f"delete()-測試資料")
    print(f"series:\n{series}")
    print("-----------------------------------")
    print("刪除author屬性")
    # 回傳新的Series
    print(f"series.drop('author')\n{series.drop('author')}")


def main():
    create()
    print("===================================")
    info()
    print("===================================")
    convert_to()
    print("===================================")
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
