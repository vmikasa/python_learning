# 下面学习魔术方法
#魔术方法通常以下划线开头和结尾，且都是小写字母组成的特殊方法，这些方法在特定的情况下会被自动调用。比如__init__方法在创建对象时会被自动调用，__str__方法在使用print函数输出对象时会被自动调用。
# 下面以Student类对象为例子，演示常见的魔术方法

class Student:
    # __init__方法在创建对象时会被自动调用
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # __str__方法，当print（对象）的时候，该方法会自动调用，替代原来打印内存地址的情况
    def __str__(self):      # 必须用return，不能用print，因为这个方法的作用就是返回一个字符串表示对象的内容，而不是直接打印出来。print函数会调用这个方法来获取字符串表示，然后再打印出来。
        return f"学生(名字={self.name}, 年龄={self.age})"

    # __repr__方法，当在交互式环境中输入对象时，该方法会自动调用，返回对象的字符串表示
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"

    # __lt__方法，当使用<运算符比较对象时，该方法会自动调用，返回一个布尔值
    def __lt__(self, other):        # 这里的self是左侧对象，other是右侧对象，比较两个对象的年龄大小。当比较对象大小的时候，会自动调用该方法
        return self.age < other.age     # 事实上，这个比较逻辑随便写也可以。写成大于也没事。但是lt是less than的缩写，所以还是写成小于比较好

    # __le__方法，当使用<=运算符比较对象时，该方法会自动调用，返回一个布尔值
    def __le__(self, other):
        return self.age <= other.age        # le是less than or equal to的缩写，所以写成小于等于比较好

    # __eq__方法，当使用==运算符比较对象时，该方法会自动调用，返回一个布尔值
    def __eq__(self, other):
        return self.age == other.age        # eq是equal的缩写，所以写成等于比较好