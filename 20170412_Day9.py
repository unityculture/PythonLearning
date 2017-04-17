import pandas as pd  # 引用套件並縮寫為 pd

groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
ironmen = [51, 8, 18, 14, 6, 64]

ironmen_dict = {"groups": groups,
                "ironmen": ironmen
                }

# 跟 R 語言程式比較這兩行
ironmen_df = pd.DataFrame(ironmen_dict)
print(ironmen_df.dtypes)
print(ironmen_df.head(n=3))

# 一定要看R的物件導向概念：http://ithelp.ithome.com.tw/articles/10185564
