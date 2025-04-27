from pandas import DataFrame


# 將寬格式轉為長格式
def convert_to_long(df_wide: DataFrame):
    # melt()：將寬格式轉為長格式
    df_melted = df_wide.melt(
        # 指定由"months"來擔當index
        id_vars="months",
        # 指定欄位的變數名稱為"products"，此為"A", "B"
        var_name="products",
        # 指定值的變數名稱為"sales"，此為"A", "B"商品的list
        value_name="sales"
    )
    print("df_melted:\n", df_melted)
    return df_melted


# 將長格式轉為寬格式
def convert_to_wide(df_long: DataFrame):
    # pivot()：將長格式轉為寬格式
    df_pivoted = df_long.pivot(
        index="months",
        columns="products",
        values="sales"
    ).reset_index()  # 呼叫reset_index()將months還原為普通欄位
    print("df_pivoted:\n", df_pivoted)


def main():
    df = DataFrame({
        "months": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        "A": [1000, 1200, 1350, 1250, 1330, 1240, 1150, 1250, 1230, 1300, 1320, 1400],
        "B": [300, 320, 350, 315, 330, 340, 312, 325, 330, 323, 335, 340]
    })
    print("df:\n", df)
    print("===================================")
    df_long = convert_to_long(df)
    print("===================================")
    convert_to_wide(df_long)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
