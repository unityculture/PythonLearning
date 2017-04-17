# Ref http://ithelp.ithome.com.tw/articles/10185736
#  Python 基本變數類型與資料結構可以應用的屬性或方法
# 數值
# float
my_float = 8.7
print(my_float.as_integer_ratio())
print(my_float.is_integer())
print(my_float.hex())
print(float.fromhex("0x1.1666666666666p+3"))
# int
my_int = 87
print(my_int.bit_length())
print(my_int.to_bytes(length=2, byteorder="big"))
print(int.from_bytes(b'\x00W', byteorder="big"))
print("---")
print(my_int.to_bytes(length=10, byteorder="big"))
print(int.from_bytes(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00W', byteorder="big"))
# complex
my_complex = 8 + 7j
print(my_complex.real)
print(my_complex.imag)
print(my_complex.conjugate())
# ----
# 文字
my_str = "It's the 2017 ithelp ironman contest!!!"

print(my_str.startswith("It's"))  # True
print(my_str.endswith("contest??"))  # False
print(my_str.find("2017"))  # 9
print(my_str.count("!"))  # 3
print(my_str.strip("!"))  # It's the 2017 ithelp ironman contest
print(my_str.capitalize())  # It's the 2017 ithelp ironman contest!!!
print(my_str.title())  # It'S The 2017 Ithelp Ironman Contest!!!
print(my_str.upper())  # IT'S THE 2017 ITHELP IRONMAN CONTEST!!!
print(my_str.lower())  # it's the 2017 ithelp ironman contest!!!
print(my_str.swapcase())  # iT'S THE 2017 ITHELP IRONMAN CONTEST!!!
print(my_str.replace("contest", "competition"))  # It's the 2017 ithelp ironman competition!!!
# ---
# bool
my_bool = True
print(my_bool.bit_length())
print(my_bool.to_bytes(length=2, byteorder="big"))
print(bool.from_bytes(b'\x00\x01', byteorder="big"))
print("---")
print(my_bool.to_bytes(length=10, byteorder="big"))
print(bool.from_bytes(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01', byteorder="big"))
# ----
# 基本資料結構的屬性或方法
print("---")
ironmen = [56, 8, 18, 14, 6]
ironmen.append(66)
print(ironmen)
ironmen.pop()
print(ironmen)
ironmen.insert(5, 66)  # 5 is index
ironmen.remove(66)
print(ironmen)
ironmen.index(56)
ironmen.append(66)
ironmen.append(66)
print(ironmen.count(66))
ironmen.pop()
ironmen.sort()
print(ironmen)
ironmen.reverse()
print(ironmen)

# ---
# Dict
ironmen_dict = {"Modern Web": 56,
                "DevOps": 8,
                "Cloud": 18,
                "Big Data": 14,
                "Security": 6,
                "自我挑戰組": 66}

print(ironmen_dict.get("Modern Web"))
print(ironmen_dict.keys())
print(ironmen_dict.items())
print(ironmen_dict.values())
# ---
# numpy 與 ndarray 的常用屬性或方法
import numpy as np

# 截至 2016-12-06 上午 7 時第 8 屆 iT 邦幫忙各組的鐵人分別是 56、8、19、14、6 與 71 人
ironmen = [56, 8, 19, 14, 6, 71]
ironmen_array = np.array(ironmen)

print(ironmen_array.ndim)  # number of dimensions
print(ironmen_array.shape)  # m*n
print(ironmen_array.dtype)  # 資料類型
print("\n")  # 空一行

# 2d array
ironmen_2d = [range(1, 7), [56, 8, 19, 14, 6, 71]]
ironmen_2d_array = np.array(ironmen_2d)
print(ironmen_2d_array.ndim)  # number of dimensions
print(ironmen_2d_array.shape)  # m*n
print(ironmen_2d_array.dtype)  # 資料類型
# ---
# 用索引值進行篩選
my_array = np.arange(10)
print(my_array[0])
print(my_array[0:5])
print("---")  # 分隔線

my_2d_array = np.array([np.arange(0, 5), np.arange(5, 10)])
print(my_2d_array)
print("---")  # 分隔線
print(my_2d_array[1, :])  # 第二列
print(my_2d_array[:, 1])  # 第二欄
print(my_2d_array[1, 1])  # 第二列第二欄的元素
# ---
# 用布林值進行篩選
import numpy as np

ironmen = [56, 8, 19, 14, 6, 71]
groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
ironmen_array = np.array(ironmen)
groups_array = np.array(groups)

# 用人數去篩選組別
print(ironmen_array >= 10)  # 布林值陣列
print(groups_array[ironmen_array >= 10])  # 鐵人數大於 10 的組別

# 用組別去篩選人數
print(groups_array != "自我挑戰組")  # 布林值陣列
print(ironmen_array[groups_array != "自我挑戰組"])  # 除了自我挑戰組以外的鐵人數
# ---
# 2d array 轉置
my_1d_array = np.arange(10)  # 建立一個 2d array
my_2d_array = my_1d_array.reshape((2, 5))
print(my_2d_array)
print("---")  # 分隔線
print(my_2d_array.T)
# ----
# numpy 的 where 方法
normal_samples = np.random.normal(size=10)  # 生成 10 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
uniform_samples = np.random.uniform(size=10)  # 生成 10 組介於 0 與 1 之間均勻分配隨機變數

print(normal_samples)
print("---")  # 分隔線
print(uniform_samples)
