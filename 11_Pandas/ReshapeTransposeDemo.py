from pandas import DataFrame


def transpose_property(df: DataFrame):
    print("df.T:\n", df.T)


def transpose_method(df: DataFrame):
    # 效果與df.T相同
    print("df.transpose():\n", df.transpose())


def main():
    df = DataFrame({
        "months": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        "A": [1000, 1200, 1350, 1250, 1330, 1240, 1150, 1250, 1230, 1300, 1320, 1400],
        "B": [300, 320, 350, 315, 330, 340, 312, 325, 330, 323, 335, 340]
    }).set_index("months")
    print("df:\n", df)
    print("===================================")
    transpose_property(df)
    print("===================================")
    transpose_method(df)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
