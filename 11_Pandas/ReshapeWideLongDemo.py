from pandas import DataFrame


# 將寬格式轉為長格式
def convert_to_long(df_wide: DataFrame):
    # melt()：將寬格式轉為長格式
    df_melted = df_wide.melt(
        # id_vars是要保留的列，在轉換過程中，這些欄位不會被改變或拆開
        id_vars="months",
        # 建立新欄位products以儲存原欄位名稱(A, B)
        var_name="products",
        # 建立新欄位sales以儲存原欄位內儲存的值(A, B商品的銷量)
        value_name="sales"
    )
    print("df_melted:\n", df_melted)
    return df_melted


# 將長格式轉為寬格式
def convert_to_wide(df_long: DataFrame):
    # pivot()：將長格式轉為寬格式
    df_pivoted = df_long.pivot(
        # 將months欄位指定為index
        index="months",
        # 將products儲存的值轉成欄位名稱
        columns="products",
        # 將sales儲存的值轉成上述對應欄位名稱的值
        values="sales"
    )
    # 呼叫reset_index()將months還原為普通欄位
    # df_pivoted = df_pivoted.reset_index()
    print("df_pivoted:\n", df_pivoted)


def main():
    df = DataFrame({
        "months": range(1, 13),
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
