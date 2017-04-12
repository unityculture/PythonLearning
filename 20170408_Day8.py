# Scope Function : global and local function
def my_square(input_number):
    '計算平方數'
    ans = input_number**2  # 區域變數，只有在函數中可以被使用
    return ans
# 呼叫函數
print(my_square(3))
# 印出變數
# print(ans)  # 無法印出區域變數

# Nested functions

def my_mean(input_list):
    'compute mean'
    def my_sum(input_list):
        'count sun'
        tmp_sum = 0
        for i in input_list:
            tmp_sum += i
        return tmp_sum
    def my_length(input_list):
        tmp_len = 0
        for i in input_list:
            tmp_len += 1
        return tmp_len
    return my_sum(input_list) / my_length(input_list)
my_list = [51, 8, 18, 13, 6, 64]
print(my_mean(my_list))

# Error Handling
# python : try - except <-> R : trycatch
print('-----')


def my_square(input_number):
    '計算平方數且有錯誤處理的函數'
    try:
        ans = input_number**2
        return ans
    except:
        print("請輸入數值。")

print(my_square(3))
my_square('ironmen')

# Flexible arguments
# 定義自訂函數


def ironmen_list(*args):
    '列出各組參賽鐵人數'
    for ironman in args:
        print(ironman)

# 呼叫自訂函數
ironmen_list(51, 8, 18, 13, 6)  # 不含自我挑戰組
print("---")
ironmen_list(51, 8, 18, 13, 6, 64)  # 含自我挑戰組

# 不太懂用法


def ironmen_list(**kwargs):
    '列出各組參賽鐵人數'
    for key in kwargs:
        print(key, "：", kwargs[key], "人")

ironmen_list(a=51)
