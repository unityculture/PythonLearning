# Numpy introduction
import numpy as np  # 引用套件
ironmen = np.array([46, 8, 11, 11, 4, 56])  # 將 list 透過 numpy 的 array 方法進行轉換
print(ironmen)  # 看看 ironmen 的外觀
print(type(ironmen))  # 看看 ironmen 的資料結構
articles = ironmen * 30
print(articles)
# empty, ones and zero function in numpy
print(np.empty(10))
print(np.ones(10))
print(np.zeros(10))
# 類型轉換
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr)
print(float_arr.dtype)
str = np.array(['1.12', '2.21', '31.3', '4.41', '5.51'], dtype=np.string_)
print(str.dtype)
str_float = str.astype(np.float64)
print(str_float)
# array maniulate
my_np_array = np.array([[1, 2], [4, 5]])
print(my_np_array)
my_np_array = np.array([1, 2, 3, 4])
print(my_np_array ** 2)
my_2d_array = np.array([[1, 3], [2, 4]])
print(my_2d_array ** 2)
# filter on one dimension
ironmen = np.array([46, 8, 11, 11, 4, 56])
print(ironmen[0])  # 選出 Modern Web 組的鐵人數
print(ironmen > 10)  # 哪幾組的鐵人數超過 10 人
print(ironmen[ironmen > 10])  # 超過 10 人的鐵人數
# filter on two dimension
ironmen = np.array([[10, 20], [15, 25]])
print(ironmen[0, 0])
print(ironmen > 15)
print(ironmen[ironmen > 15])
# attributes for array
ironmen_2d_array = np.array([[46, 11, 4],
                             [8, 11, 56]])
print(ironmen_2d_array.size)  # length in R
print(ironmen_2d_array.shape)  # dim in R
