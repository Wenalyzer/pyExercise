from pathlib import Path
import numpy as np


def save_load_array_csv(path):
    data = np.array(
        [["Alice", 80, 90, 85],
         ["Charlie", 88, 92, 86],
         ["David", 60, 65, 70],
         ["Eva", 95, 88, 94]]
    )
    header = "姓名,國文,英文,數學"
    np.savetxt(
        path,
        data,
        delimiter=",",
        # 存檔為文字類型
        fmt="%s",
        # 加上標題
        header=header,
        # 加在標題前的文字，預設為"#"，可改為空字串
        comments="",
        encoding="utf-8"
    )
    print(f"已儲存陣列為{path.name}檔")
    print("-----------------------------------")

    # 載入csv檔，並跳過第一列標題
    data_loaded = np.genfromtxt(
        path,
        # 分隔符號，預設為空白字元
        delimiter=",",
        # 設定結果陣列的資料類型，如不設定會依照各欄位自動推定類型
        dtype=str,
        # 使用當初文字編碼方式來解碼
        encoding="utf-8",
        # 跳過第一列標題
        skip_header=1
    )
    print(f"載入{path}檔:\n{data_loaded}")


def main():
    path = Path("10_NumPy", "ArrayCsvDemo.csv")
    save_load_array_csv(path)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")