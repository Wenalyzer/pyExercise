import numpy as np


# 1維陣列資訊
def array1D_info():
    a1 = np.array([1, 2, 3], dtype=np.int32)
    print("array1D_info()-測試資料")
    print(f"a1: {a1}")
    print("-----------------------------------")
    print("np.info(a1)")
    np.info(a1)
    print("-----------------------------------")
    # 取得維度資訊
    print(f"a1.ndim: {a1.ndim}")
    print(f"a1.shape: {a1.shape}")
    print("-----------------------------------")
    # 取得長度資訊
    print(f"len(a1): {len(a1)}")
    print("-----------------------------------")
    # 取得元素總個數
    print(f"a1.size: {a1.size}")
    print("-----------------------------------")
    # 取得型別
    print(f"a1.dtype: {a1.dtype}")


# 2維陣列資訊
def array2D_info():
    a2 = np.array([
        [1, 2, 3],
        [4, 5, 6]],
        dtype=np.int32
    )
    print("array2D_info()-測試資料")
    print(f"a2:\n{a2}")
    print("-----------------------------------")
    print("np.info(a2)")
    np.info(a2)
    print("""
    np.info(a2)的輸出結果:
    class:  ndarray - 陣列的類型為 numpy.ndarray
    shape:  (2, 3) - 陣列的維度為2x3
    strides:  (12, 4) - 
          陣列內移至下個元素需要的步幅為12 (3 elements × 4 bytes per element)
          因為2維陣列的元素是1維陣列，所以[1, 2, 3]移至[4, 5, 6]步幅為12
    itemsize:  4 - 陣列的元素大小為4 bytes
    aligned:  True - 陣列的元素是否對齊
    contiguous:  True - 陣列是否是連續的
    fortran:  False - 陣列是否是Fortran順序
    data pointer: 0x7f8c2f6c1c30 - 陣列的起始位置，每次運行都會變化
    byteorder:  little - 陣列的字節順序為little endian(<); 另一為big endian(>)
    byteswap:  False - 
          陣列是否進行字節交換。當little endian轉為big endian，需要進行字節交換
    type: int32 - 陣列的元素型別為int32
    """)
    print("-----------------------------------")
    # 取得維度資訊
    print(f"a2.ndim: {a2.ndim}")
    print(f"a2.shape: {a2.shape}")
    print("-----------------------------------")
    # 取得長度資訊
    print(f"len(a2): {len(a2)}")
    print("-----------------------------------")
    # 取得元素總個數
    print(f"a2.size: {a2.size}")
    print("-----------------------------------")
    # 取得型別
    print(f"a2.dtype: {a2.dtype}")
    # 轉換型別
    a2_newType = a2.astype(np.float64)
    print(f"a2_newType.dtype: {a2_newType.dtype}")


def main():
    array1D_info()
    print("===================================")
    array2D_info()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
