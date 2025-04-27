from pandas import DataFrame
import pandas as pd


def add():
    # 建立一個有欄位名的DataFrame
    df = DataFrame(columns=['name', 'age'])
    print("使用loc依序新增John, Mary二列資料")
    df.loc[0] = ['John', 30]
    df.loc[1] = ['Mary', 25]
    print(f"add()-測試資料")
    print(f"df:\n{df}")
    print("-----------------------------------")
    print("新增city欄位")
    df['city'] = ['Taipei', 'Taichung']
    print(f"df:\n{df}")


def read():
    df = DataFrame({
        'name': ['John', 'Mary', 'Ken'],
        'age': [30, 25, 35],
        'city': ['Taipei', 'Taichung', 'Kaohsiung']
    })
    print(f"read()-測試資料")
    print(f"df:\n{df}")
    print("-----------------------------------")
    # 取name欄位資料
    print(f"df['name']:\n{df['name']}")
    print("-----------------------------------")
    # 取name, age欄位資料
    print(f"df[['name', 'age']]:\n{df[['name', 'age']]}")
    print("-----------------------------------")
    # 取列index=0資料
    print(f"df.loc[0]:\n{df.loc[0]}")
    print("-----------------------------------")
    # 取列index=0, 1資料
    print(f"df.loc[[0, 1]]:\n{df.loc[[0, 1]]}")
    print("-----------------------------------")
    # 取列index=0以及欄位=name的資料
    print(f"df.loc[0, 'name']: {df.loc[0, 'name']}")
    print("-----------------------------------")
    # 取age>=30資料
    print(f"df['age'] >= 30:\n{df['age'] >= 30}\n")
    print(f"df[df['age'] >= 30]:\n{df[df['age'] >= 30]}")
    print("-----------------------------------")
    # 取age>=30, city=Taipei的資料; &代表and, |代表or
    print(f"(df['age'] >= 30) & (df['city'] == 'Taipei')")
    print((df['age'] >= 30) & (df['city'] == 'Taipei'), end="\n\n")
    print(f"df[(df['age'] >= 30) & (df['city'] == 'Taipei')]:")
    print(f"{df[(df['age'] >= 30) & (df['city'] == 'Taipei')]}")
    print("-----------------------------------")
    # 只讀前2筆
    print(f"df.head(2):\n{df.head(2)}")
    print("-----------------------------------")
    # 只讀後2筆
    print(f"df.tail(2):\n{df.tail(2)}")
    print("-----------------------------------")
    print("for-nested走訪DataFrame")
    for column, values in df.items():
        print(f"{column}:", end=" ")
        for value in values:
            print(value, end=" ")
        print()


def update():
    df = DataFrame({
        'name': ['John', 'Mary', 'Ken'],
        'age': [30, 25, 35],
        'city': ['Taipei', 'Taichung', 'Kaohsiung']
    })
    print(f"update()-測試資料")
    print(f"df:\n{df}")
    print("-----------------------------------")
    print("John年齡改成33")
    # 可以直接以index=0指定，但一般不可能知道John所在的index
    # df.loc[0, 'age'] = 33
    # 以條件指定較常見
    condition = df['name'] == 'John'
    print(f"condition:\n{condition}")
    print(f"df.loc[condition, 'age'] = 33")
    df.loc[condition, 'age'] = 33 
    print(f"df:\n{df}")
    print("-----------------------------------")
    print("Ken居住城市改成Hualien")
    print("df.loc[df['name'] == 'Ken', 'city'] = 'Hualien'")
    df.loc[df['name'] == 'Ken', 'city'] = 'Hualien'
    print(f"df:\n{df}")


def delete():
    df = DataFrame({
        'name': ['John', 'Mary', 'Ken'],
        'age': [30, 25, 35],
        'city': ['Taipei', 'Taichung', 'Kaohsiung']
    })
    print(f"delete()-測試資料")
    print(f"df:\n{df}")
    print("-----------------------------------")
    # 預設inplace=False，所以不會刪除原DataFrame內資料
    print(f"df.drop(1):\n{df.drop(1)}\n")
    # 刪除列index=0與2(不連續)資料
    print(f"df.drop([0, 2]):\n{df.drop([0, 2])}\n")
    # 刪除列index=0到2(連續)資料
    print(f"df.drop(df.index[0:2]):\n{df.drop(df.index[0:2])}")
    print("-----------------------------------")
    print("刪除city欄位資料")
    print(f"df.drop('city', axis=1):\n{df.drop('city', axis=1)}")
    print("-----------------------------------")
    print("刪除所有資料(只剩欄位名稱)")
    print(f"df.drop(df.index):\n{df.drop(df.index)}")
    print("-----------------------------------")
    print("刪除原DataFrame所有資料")
    print("df.drop(df.index, inplace=True)")
    # inplace=True代表直接移除原DataFrame內容, 而非回傳新的DataFrame
    df.drop(df.index, inplace=True)
    print(f"df:\n{df}\n")
    print("移除所有欄位名稱")
    print("df.drop(columns=df.columns, inplace=True)")
    df.drop(columns=df.columns, inplace=True)
    print(f"df:\n{df}")


def main():
    add()
    print("===================================")
    read()
    print("===================================")
    update()
    print("===================================")
    delete()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
