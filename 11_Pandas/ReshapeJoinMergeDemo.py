from pandas import DataFrame


# 基於 index 合併
def join():
    # 第一個 DataFrame：商店ID, 商店名
    df1 = DataFrame({
        "Store_ID": ["S001", "S002", "S003"],
        "Store_Name": ["FamilyMart Taipei", "FamilyMart Taichung", "FamilyMart Kaohsiung"]
    })
    # 設定索引為 Store_ID
    df1.set_index("Store_ID", inplace=True)

    # 第二個 DataFrame：商店ID, 月營業額
    df2 = DataFrame({
        "Store_ID": ["S001", "S002", "S004"],
        "Monthly_Revenue": [850000, 730000, 600000]
    })
    # 設定索引為 Store_ID
    df2.set_index("Store_ID", inplace=True)

    # join()預設為"left"，也可使用 "inner", "right", "outer"
    result = df1.join(df2, how="left")
    print(result)


# 基於 column 合併
def merge():
    # 第一個 DataFrame
    df1 = DataFrame({
        "Store_ID": ["S001", "S002", "S003"],
        "Store_Name": ["FamilyMart Taipei", "FamilyMart Taichung", "FamilyMart Kaohsiung"]
    })

    # 第二個 DataFrame
    df2 = DataFrame({
        "Store_ID": ["S001", "S002", "S004"],
        "Monthly_Revenue": [850000, 730000, 600000]
    })

    # 使用merge()基於Store_ID屬性進行合併
    # merge()的how參數預設為 "inner"，與join()不同；也可使用 "left", "right", "outer"
    result = df1.merge(df2, on="Store_ID", how="inner")
    print(result)


def main():
    join()
    print("===================================")
    merge()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
