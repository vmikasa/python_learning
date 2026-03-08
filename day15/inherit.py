# 下面简单学习一下继承

"""
Python 继承速查
"""

# 1. 定义
# 继承：让子类拥有父类的属性和方法
# 父类：放公共内容
# 子类：复用父类 + 扩展自己

# 2. 基本语法
class Parent:
    pass


class Child(Parent):
    pass


# 3. 常用模板
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"姓名：{self.name}，年龄：{self.age}")


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)  # 调用父类构造方法
        self.score = score

    def show_score(self):
        print(f"{self.name}的成绩是{self.score}")


# 4. 重点
# - 子类可以直接使用父类的方法和属性
# - 子类可以新增自己的属性和方法
# - super().__init__(...) 常用于初始化父类部分


# 5. 一句话总结
# 继承 = 复用父类公共内容 + 扩展子类功能


# 方法重写：子类继承父类的方法，子类中写一个与父类同名的方法，就可以覆盖掉父类的方法，这叫做方法重写。
# 但是调用父类方法不是要用super()吗？
# 原因是，因为方法重写了才要调用super()。我的意思是，子类继承了父类的全部方法，本来就可以直接调用父类方法。即使不写super()也可以调用
# 但是，当出现方法重写的时候，子类方法会覆盖父类方法，这个时候就要用super()才能调用父类方法
# 属性重写与方法重写完全同理

