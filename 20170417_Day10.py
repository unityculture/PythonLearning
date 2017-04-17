# Python 物件導向(2)
class Ironmen:
    '''這是一個叫做 Ironmen 的類別'''  # Doc string

    def __init__(self, group, participants):
        self.group = group
        self.participants = participants

# 在物件名稱後面使用 . 接屬性名稱就可以使用。
modern_web = Ironmen("Modern Web", 54)
print(modern_web)
print(modern_web.group)
print(modern_web.participants)
print(modern_web.__doc__)
print(dir(modern_web))
# -------
# 定義方法(Method)


class Ironmen:
    '''這是一個叫做 Ironmen 的類別'''  # Doc string

    def __init__(self, group, participants):
        self.group = group
        self.participants = participants

    def print_info(self):
        print(self.group, "組有", self.participants, "位鐵人參賽！")

# 根據 Ironmen 類別建立一個物件 modern_web
modern_web = Ironmen("Modern Web", 54)

# 根據 Ironmen 類別建立一個物件 dev_ops
dev_ops = Ironmen("DevOps", 8)

# 使用 modern_web 的 print_info() 方法
modern_web.print_info()

# 使用 dev_ops 的 print_info() 方法
dev_ops.print_info()
# -----
# 繼承（Inheritance）


class Ironmen:
    '''這是一個叫做 Ironmen 的類別'''  # Doc string

    def __init__(self, group, participants):
        self.group = group
        self.participants = participants

    def print_info(self):
        print(self.group, "組有", self.participants, "位鐵人參賽！")
# --------
# Articles 類別繼承 Ironmen 類別


class Articles(Ironmen):
    '''
    這是一個叫做 Articles 的類別。
    Articles 繼承 Ironmen 類別，她新增了一個 print_articles() 方法
    '''

    def print_articles(self):
        print(self.group, "組預計會有", self.participants * 30, "篇文章！")

# 根據 Articles 類別建立一個物件 modern_web
modern_web = Articles("Modern Web", 54)

# 使用 modern_web 的 print_articles() 方法
modern_web.print_articles()

# 檢查 modern_web 是否還擁有 print_info() 方法
modern_web.print_info()
# ------
# 繼承 : super()
# 可以根據原本的屬性或方法之上建立新的屬性或方法。


class OnlyGroup:
    '''這是一個叫做 OnlyGroup 的類別'''  # Doc string

    def __init__(self, group):
        self.group = group

# Ironmen 類別繼承 OnlyGroup 類別


class Ironmen(OnlyGroup):
    '''這是一個叫做 Ironmen 的類別'''  # Doc string

    def __init__(self, group, participants):
        super().__init__(group)
        self.participants = participants

# 根據 Ironmen 類別建立一個物件 modern_web
modern_web = Ironmen("Modern Web", 54)

# 印出 modern_web 的兩個屬性
print(modern_web.group)
print(modern_web.participants)
# --------
# 在繼承時改寫方法（Override）
# 我們在先前繼承時成功增加一個方法 print_articles()，現在我們要試著在 Article 類別中改寫原本 Ironmen 類別中的 print_info() 方法。


class Ironmen:
    '''這是一個叫做 Ironmen 的類別'''  # Doc string

    def __init__(self, group, participants):
        self.group = group
        self.participants = participants

    def print_info(self):
        print(self.group, "組有", self.participants, "位鐵人參賽！")

# Articles 類別繼承 Ironmen 類別


class Articles(Ironmen):
    '''
    這是一個叫做 Articles 的類別。
    Articles 繼承 Ironmen 類別，她新增了一個 print_articles() 方法
    '''

    def print_articles(self):
        print(self.group, "組預計會有", self.participants * 30, "篇文章！")

    # 改寫 print_info() 方法
    def print_info(self):
        print(self.group, "組有", self.participants, "位鐵人參賽！p.s.我被改寫了！")

# 根據 Articles 類別建立一個物件 modern_web
modern_web = Articles("Modern Web", 54)

# 檢查 modern_web 的 print_info() 方法是否被改寫
modern_web.print_info()
