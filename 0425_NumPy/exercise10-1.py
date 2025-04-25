from pathlib import Path
import numpy as np

path = Path.cwd()/"0425_NumPy/Ex10_1.csv"

print(path)

data = np.array(
        [["Alice", 80, 90, 85],
         ["Bob", 70, 75, 80],
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

data_load = np.genfromtxt(
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