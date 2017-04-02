# 變數型態
print(type(5))  # 'int'
print(type(5.5))  # 'float'
print(type(5 + 3j))  # 'complex'
print(type(True))  # 'bool'
print(type(False))  # 'bool'
print(type("2017 ithome ironman"))  # 'str'
"2017 ithome ironman" + " rocks!"  # Error
print(1.0 == True)  # True
print(0 == False)  # True
print(1.2 + True)  # 2.2
print(3 + True * 2)  # 5

# "+" is acceptable for string in python
print("2017 ithome ironman" + " rocks!")  # "2017 ithome ironman rocks!"
print("2017 ithome ironman " + "rocks" + "!" * 3)  # "2017 ithome ironman rocks!!!"

# 變數轉換
days = 30
print("In order to become an ironman, you have to publish an article a day for " + str(days) + " days in a row.")
# 可轉換的類型
# - float()：轉換變數類型為 float
# - int()：轉換變數類型為 int
# - complex()：轉換變數類型為 complex
# - bool()：轉換變數類型為 bool
# - str()：轉換變數類型為 str
my_bool = True
print(type(my_bool))  # 'bool'
print(float(my_bool))  # 1.0
print(int(my_bool))  # 1
print(complex(my_bool))  # 1+0j
print(type(str(my_bool)))  # 'str'

# 運算子
days = 30
days += 3
print(days)  # 33
days -= 3
print(days)  # 30
days *= 5
print(days)  # 150
days /= 5
print(days)  # 30.0
days %= 7
print(days)  # 2.0
