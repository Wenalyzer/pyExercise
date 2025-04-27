import numpy as np
from pandas import DataFrame


class Book:
    def __init__(self, name="", price=0.0):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.price}"


def create():
    print("內容來自2維list：1維list長度可以不同，缺值則為NaN")
    df_list2D = DataFrame([
        ["Python", 500], ["Java", 400], ["Swift"]
    ])
    print(f"df_list2D:\n{df_list2D}")
    print("-----------------------------------")

    print(f"加上column label:\ndf_list2D.columns=['name', 'price']")
    df_list2D.columns = ["name", "price"]
    print(f"df_list2D:\n{df_list2D}")
    print("-----------------------------------")

    print("內容來自2維陣列：長度要相同，否則產生ValueError")
    array2D = np.array([["Python", 500], ["Java", 400], ["Swift", 550]])
    df_array2D = DataFrame(array2D)
    print(f"df_array2D:\n{df_array2D}")
    print("-----------------------------------")

    print("內容來自dict-list：list長度要相同，否則產生ValueError")
    df_dict_list = DataFrame({
        "name": ["Python", "Java", "Swift"],
        "price": [500, 450, 550]
    })
    print(f"df_dict_list:\n{df_dict_list}")
    print("-----------------------------------")

    print("內容來自list-dict：dict長度可以不同，缺值則為NaN")
    df_list_dict = DataFrame([
        {"name": "Python", "price": 500},
        {"name": "Java", "price": 450},
        {"name": "Swift"}
    ])
    print(f"df_list_dict:\n{df_list_dict}\n")
    print("將name欄位定為index",
          "df_list_dict.set_index('name', inplace=True)", sep="\n")
    df_list_dict.set_index("name", inplace=True)
    print(f"df_list_dict:\n{df_list_dict}")
    print("-----------------------------------")

    print("內容來自多個物件：先將物件轉成dictionary，再轉成DataFrame")
    books = [
        Book("Python", 500),
        Book("C++", 400),
    ]
    df_books = DataFrame([vars(book) for book in books])
    print(f"df_books:\n{df_books}")


def info():
    df = DataFrame({
        "name": ["Python", "Java", "Swift"],
        "price": [500, 450, 550]
    })
    print(f"info()-測試資料")
    print(f"df:\n{df}")
    print("-----------------------------------")
    # 呈現DataFrame資訊
    print("呈現DataFrame資訊\ndf.info():")
    df.info()
    print(f"\ndf1.index:\n{df.index}")
    print(f"\ndf1.columns:\n{df.columns}")


def convert_to():
    df = DataFrame({
        "name": ["Python", "Java", "Swift"],
        "price": [500, 450, 550]
    })
    print(f"convert_to()-測試資料")
    print(f"df:\n{df}")
    print("-----------------------------------")
    print("DataFrame轉dict")
    print(f"df.to_dict():\n{df.to_dict()}")
    print("-----------------------------------")
    print("DataFrame轉ndarray")
    print(f"df.to_numpy():\n{df.to_numpy()}")
    print("-----------------------------------")
    print("DataFrame轉list，需要先轉成ndarray")
    print(f"df.to_numpy().tolist():\n{df.to_numpy().tolist()}")
    print("-----------------------------------")
    print("DataFrame轉多個物件，需先轉成dictionary")
    books = [Book(**data) for data in df.to_dict(orient="records")]
    for book in books:
        print(book)


def main():
    create()
    print("===================================")
    info()
    print("===================================")
    convert_to()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
