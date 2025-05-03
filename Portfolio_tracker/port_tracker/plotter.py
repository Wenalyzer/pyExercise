import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

DATA_PATH = Path.cwd() / "Portfolio_tracker" / "data"

def load_asset_df(
        data_path: Path = DATA_PATH, 
        file_name: str = "asset_value.csv"
        ) -> pd.DataFrame:
    
    df = pd.read_csv(
            data_path/file_name,
            index_col=0,
            parse_dates=True
        )

    df["Total"] = df.sum(axis=1)
    return df

def plot_total_asset(data_path: Path = DATA_PATH):
    """
    畫總資產變化圖
    """
    df = load_asset_df(data_path)
    plt.figure(figsize=(10,6))
    plt.plot(df.index, df["Total"], label="Total Asset", color="blue")
    plt.title("Total Portfolio Value (TWD)")
    plt.xlabel("Date")
    plt.legend()
    plt.grid(which='both', axis='x')

    ax = plt.gca()
    # 每年標一次
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    # 每季標一次格線
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[1,4,7,10]))

    # 顯示次刻度格線
    ax.grid(which='minor', axis='x', linestyle=':', color='gray')

    # Y軸每100000元一條格線
    ax.yaxis.set_major_locator(plt.MultipleLocator(100000))
    ax.grid(which='major', axis='y', linestyle='--', color='gray')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_asset_by_category(data_path: Path = DATA_PATH):
    """
    畫各資產價值變化圖（20日移動平均）
    """
    df = load_asset_df(data_path)
    plt.figure(figsize=(10,6))
    asset_cols = [col for col in df.columns if col != "Total"]
    colors = plt.cm.tab10.colors  # 最多10種顏色

    for i, col in enumerate(asset_cols):
        smooth = df[col].rolling(window=20, min_periods=1).mean()  # 20天移動平均
        plt.plot(
            df.index, smooth,
            label=col,
            color=colors[i % len(colors)],
            linewidth=2
        )

    plt.title("Asset Value by Category (TWD, 20-day MA)")
    plt.xlabel("Date")
    plt.legend()
    plt.grid(which='both', axis='x')

    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[1,4,7,10]))
    ax.grid(which='minor', axis='x', linestyle=':', color='gray')
    ax.yaxis.set_major_locator(plt.MultipleLocator(20000))
    ax.grid(which='major', axis='y', linestyle='--', color='gray')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()