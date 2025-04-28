from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


def bar_chart(df: DataFrame):
    df.plot(kind="bar", figsize=(8, 5))
    plt.title("Sales Performance by Month & Employee")
    plt.ylabel("Sales Amount")
    plt.xlabel("Month")
    plt.xticks(rotation=0)  # Horizontal x-axis labels
    plt.legend(title="Salesperson")
    plt.show()


def line_chart(df: DataFrame):
    df.plot(kind="line", marker="o", figsize=(8, 5))
    plt.title("Sales Trend Over Time")
    plt.ylabel("Sales Amount")
    plt.xlabel("Month")
    plt.grid()
    plt.legend(title="Salesperson")
    plt.show()


def pie_chart(df: DataFrame):
    # 3月份各業務員銷售量
    df.loc["3"].plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6))
    plt.title("Sales Share in March")
    plt.ylabel("")  # Hide y-axis label
    plt.show()


def heatmap(df: DataFrame):
    plt.figure(figsize=(8, 5))
    sns.heatmap(df, annot=True, cmap="coolwarm", fmt=".0f")
    plt.title("Sales Heatmap")
    plt.show()


def pivot_table(df: DataFrame):
    print("pivot_table()")
    # index, columns組合可以重複
    # 善於多維度交叉分析：例如不同業務員在不同月份的銷售總額
    df_pivot_sum = df.pivot_table(
        index="months",
        columns="Salesperson",
        values="Sales",
        aggfunc="sum",
        fill_value=0
    )
    print("df_pivot_sum:\n", df_pivot_sum)
    bar_chart(df_pivot_sum)
    line_chart(df_pivot_sum)
    pie_chart(df_pivot_sum)
    heatmap(df_pivot_sum)
    print("-----------------------------------")

    # 總和、平均都要分析，且空值補0
    df_pivot_sum_mean_fillvalue = df.pivot_table(
        index="months",
        columns="Salesperson",
        values="Sales",
        aggfunc=["sum", "mean"],
        fill_value=0
    )
    print("df_pivot_sum_mean_fillvalue:\n",
          df_pivot_sum_mean_fillvalue)


def pivot(df: DataFrame):
    print("pivot()")
    # pivot()單純將長轉寬，index, columns組合必須唯一，否則執行錯誤
    # 因為同月份(index)、同業務員(columns)有2筆以上銷售額，未遵守上述的唯一性，所以執行錯誤
    try:
        df_pivot = df.pivot(
            index="months",
            columns="Salesperson",
            values="Sales"
        )
        print("df_pivot:\n", df_pivot)
    except ValueError as err:
        print("error:", err)


def groupby(df: DataFrame):
    print("groupby()")
    # groupby()善於單維度分組統計：例如每個業務員的總銷售額
    df_groupby_sum_mean = df.groupby("Salesperson")["Sales"].agg(
        ["sum", "mean"]
    ).reset_index()
    print("df_groupby_sum_mean:\n", df_groupby_sum_mean)


def main():
    # 每個業務員的銷售額
    # Alice 在 months=1 有兩筆銷售記錄（100、110）
    # Charlie 在 months=3 也有兩筆銷售記錄（123、140）
    df = DataFrame({
        "months": ["1", "1", "1", "2", "2", "2", "3", "3", "3", "3"],
        "Salesperson": ["Alice", "Bob", "Alice", "Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie", "Charlie"],
        "Sales": [100, 120, 110, 125, 133, 124, 115, 125, 123, 140]
    })
    print("df:\n", df)
    print("===================================")
    pivot_table(df)
    print("===================================")
    pivot(df)
    print("===================================")
    groupby(df)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
