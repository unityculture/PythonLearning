# 由Dictionary轉換成DataFrame
import numpy as np
import pandas as pd
groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "tmp"]
ironmen = [46, 8, 12, 12, 6, 58]
ironmen_dict = {"groups": groups,
                "ironmen": ironmen}
ironmen_df = pd.DataFrame(ironmen_dict)
print(ironmen_df)  # 看看資料框的外觀
print(type(ironmen_df))  # pandas.core.frame.DataFrame
# 由Numpy的array轉和
my_2d_array = np.array([[1, 3], [2, 4]])
my_df = pd.DataFrame(my_2d_array, columns=["col1", "col2"])
print(my_df)
# ndarrat : 限定單一類型
# Dafaframe : 可接受不同類型
print(ironmen_df.dtypes)
# 選擇資料
# iloc = 可以使用數字來選擇列數、欄位
print(ironmen_df.iloc[0:1, 1]) # 第一列第二欄：Modern Web 組的鐵人數
print("---")
print(ironmen_df.iloc[0:1,:]) # 第一列：Modern Web 組的組名與鐵人數
print("---")
print(ironmen_df.iloc[:,1]) # 第二欄：各組的鐵人數
print("---")
print(ironmen_df["ironmen"]) # 各組的鐵人數
print("---")
print(ironmen_df.ironmen) # 各組的鐵人數
# categorical對應到R的factor
import pandas as pd
groups_categorical = pd.Categorical(["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "tmp"])
print(groups_categorical)
print("---")
print(type(groups_categorical))
# 可以設定順序
temperature_list = ["cold", "warm", "hot"]
temperature_categorical = pd.Categorical(temperature_list, categories = ["cold", "warm", "hot"], ordered = True)
temperature = pd.Series(temperature_categorical)
print(temperature)
