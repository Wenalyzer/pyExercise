from port_tracker.trade_parser import load_trade_record, save_trade_record
from port_tracker.asset_calculator import create_asset_value_csv
from port_tracker.plotter import plot_total_asset, plot_asset_by_category

def main():
    # 1. 讀取與處理交易紀錄
    # trade_df = load_trade_record()
    # save_trade_record(trade_df)
    
    # 2. 計算每日資產價值
    # create_asset_value_csv()
    
    # 3. 畫圖
    plot_total_asset()
    plot_asset_by_category()

if __name__ == "__main__":
    main()