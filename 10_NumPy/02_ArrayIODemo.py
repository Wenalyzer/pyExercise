from pathlib import Path
import numpy as np


def save_load_array_binary(path):
    a2 = np.array(
        [[1, 2, 3],
         [4, 5, 6]]
    )
    print(f"save_load_array_binary()-測試資料")
    print(f"a2:\n{a2}")
    print("-----------------------------------")

    np.save(path, a2)
    print("已儲存陣列為二進位的npy檔")

    a2_loaded = np.load(path)
    print(f"載入陣列:\n{a2_loaded}")


def save_load_array_text(path):
    a2 = np.array(
        [[1, 2, 3],
         [4, 5, 6]]
    )
    print(f"save_load_array_text()-測試資料")
    print(f"a2:\n{a2}")
    print("-----------------------------------")

    np.savetxt(path, a2)
    print("已儲存陣列為txt檔")

    # 載入檔案並轉成整數類型(預設為float)
    a2_loaded = np.loadtxt(path).astype(int)
    print(f"載入陣列:\n{a2_loaded}")


def main():
    path_binary = Path("10_NumPy", "a2.npy")
    save_load_array_binary(path_binary)
    print("===================================")
    path_text = Path("10_NumPy", "a2.txt")
    save_load_array_text(path_text)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")