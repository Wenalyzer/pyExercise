from pandas import DataFrame


# 基於index合併，用途單純
def join():
    # 第一個 DataFrame：商店ID, 商店名
    df1 = DataFrame({
        "Store_ID": ["S001", "S002", "S003"],
        "Store_Name": ["FamilyMart Taipei", "FamilyMart Taichung", "FamilyMart Kaohsiung"]
    }).set_index("Store_ID")

    # 第二個 DataFrame：商店ID, 月營業額
    df2 = DataFrame({
        "Store_ID": ["S001", "S002", "S004"],
        "Monthly_Revenue": [850000, 730000, 600000]
    }).set_index("Store_ID")

    # join()預設為"left"，也可使用 "inner", "right", "outer"
    result = df1.join(df2, how="outer")
    print(result)


# 基於column合併，用途廣泛
def merge():
    # 第一個 DataFrame
    df1 = DataFrame({
        "Store_ID": ["S001", "S002", "S003"],
        "Store_Name": ["FamilyMart Taipei", "FamilyMart Taichung", "FamilyMart Kaohsiung"]
    })

    # 第二個 DataFrame
    df2 = DataFrame({
        "ID": ["S001", "S002", "S004"],
        "Monthly_Revenue": [850000, 730000, 600000]
    })

    # 使用merge()基於Store_ID屬性進行合併
    # merge()的how參數預設為 "inner"；也可使用 "left", "right", "outer"
    # 關聯欄位名稱相同：on即可；欄位名稱不同：left_on, right_on都需要
    result = df1.merge(df2, left_on="Store_ID", right_on="ID", how="outer")
    print(result)


def main():
    join()
    print("===================================")
    merge()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
