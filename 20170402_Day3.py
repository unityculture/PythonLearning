# 資料結構 List, Tuple, Dictionary
ironman_groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
# Note : python's index 從0開始，R跟其他語言不同
# Python 基本的資料結構大致有三類：list, tuple, dictionary
# List:
participated_group = "Big Data"
current_ttl_articles = 4
is_participating = True

my_status = [participated_group, current_ttl_articles, is_participating]
print(type(my_status[0]))
print(type(my_status[1]))
print(type(my_status[2]))
# Tuple
# Note : Tuple無法新增或是刪除、更新tuple內的元素。而且是以()建立物件
# 分別建立 list 與 tuple
ironman_groups_list = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security"]
ironman_groups_tuple = tuple(ironman_groups_list)

# 新增一個元素
ironman_groups_list.insert(5, "自我挑戰組")
# ironman_groups_tuple.insert(5, "自我挑戰組") -> ERROR

# Dictionary
participated_group = "Big Data"
current_ttl_articles = 4
is_participating = True

# 建立 dictionary
my_status = {
    "group": participated_group,
    "ttl_articles": current_ttl_articles,
    "is_participating": is_participating
}
# 利用鍵值選擇元素
print(my_status["group"])
print(my_status["ttl_articles"])
print(my_status["is_participating"])

# 乘法與R不一樣
ironmen = [46, 8, 11, 11, 4, 56]
articles = ironmen * 30
print(articles)

# Numpy 的運用
import num
