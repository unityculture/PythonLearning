# [第 07 天] 迴圈與流程控制
ironmen = [49, 8, 12, 12, 6, 61]
for i in ironmen:
    print(i)
print("---")
# For 帶索引值的寫法
for index in list(range(len(ironmen))):  # 產生出一組 0 到 5 的 list
    print(ironmen[index])
print("---")
print(index)  # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看
# while 帶索引值的寫法
ironmen = [49, 8, 12, 12, 6, 61]
index = 0
while index < len(ironmen):
    print(ironmen[index])
    index += 1
print("---")
print(index)  # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看

my_seq = list(range(1, 11))
for index in my_seq:
    if (index % 2 == 0):
        print(index, "是偶數")
    else:
        print(index, "是奇數")

# Python 的 break 與 continue
# break 描述
ironmen = [49, 8, 12, 12, 6, 61]
for ironman in ironmen:
    if (ironman < 10):
        break
    else:
        print(ironman)

print("---")
print(ironman)  # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看

print("\n")  # 空一行方便閱讀

# continue 描述
for ironman in ironmen:
    if (ironman < 10):
        continue
    else:
        print(ironman)

print("---")
print(ironman)  # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看
