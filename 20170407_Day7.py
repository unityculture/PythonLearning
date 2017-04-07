# Function
import math  # 要使用 pi 得引入套件 math

# 定義自訂函數


def circle_calculate(radius, area=True):
    '依據輸入的半徑與 area 參數計算圓形的面積或周長'  # 單行的 docstring
    circle_area = math.pi * radius**2
    circle_circum = 2 * math.pi * radius
    if area == True:
        return circle_area
    else:
        return circle_circum

# 呼叫自訂函數
my_radius = 3
print(circle_calculate(my_radius))  # 預設回傳面積
print(circle_calculate(my_radius, area=False))  # 指定參數回傳周長

# 交換排序法（exchange sort）
import random  # 呼叫函數時使用隨機整數

# 定義自訂函數


def exchange_sort(input_list, reverse=False):
    ''' # 多行的 docstrings
    依據輸入的 list 與 reverse 參數排序 list 中的數字後回傳。
    reverse 參數預設為 False 遞增排序，可以修改為 True 遞減排序。
    '''
    input_list_cloned = input_list
    # 遞增排序
    if reverse == False:
        for i in range(0, len(input_list) - 1):
            for j in range(i + 1, len(input_list)):
                # 如果前一個數字比後一個數字大則交換位置
                if input_list_cloned[i] > input_list_cloned[j]:
                    temp = input_list_cloned[i]
                    input_list_cloned[i] = input_list_cloned[j]
                    input_list_cloned[j] = temp
    # 遞減排序
    else:
        for i in range(0, len(input_list) - 1):  # -1 是因為最後一項在倒數第二
            for j in range(i + 1, len(input_list)):
                # 如果前一個數字比後一個數字小則交換位置
                if input_list_cloned[i] < input_list_cloned[j]:
                    temp = input_list_cloned[i]
                    input_list_cloned[i] = input_list_cloned[j]
                    input_list_cloned[j] = temp
    return input_list_cloned

# 呼叫自訂函數
my_vector = random.sample(range(0, 100), 10)  # 產生一組隨機數
print(my_vector)  # 看看未排序前
print(exchange_sort(my_vector))  # 預設遞增排序
print(exchange_sort(my_vector, reverse=True))  # 指定參數遞減排序

# 定義自訂函數


def ironmen_stats(ironmen_list):
    max_ironmen = max(ironmen_list)
    min_ironmen = min(ironmen_list)
    ttl_groups = len(ironmen_list)
    ttl_ironmen = sum(ironmen_list)
    return max_ironmen, min_ironmen, ttl_groups, ttl_ironmen

# 呼叫自訂函數
ironmen = [50, 8, 16, 12, 6, 62]
max_ironmen, min_ironmen, ttl_groups, ttl_ironmen = ironmen_stats(ironmen)
print("最多：", max_ironmen, "\n", "最少：", min_ironmen, "\n", "總組數：", ttl_groups, "\n", "總鐵人數：", ttl_ironmen)

ironmen = [50, 8, 16, 12, 6, 62]
ironmen_articles = list(map(lambda x: x * 30, ironmen))
print(ironmen_articles)
help(map)
