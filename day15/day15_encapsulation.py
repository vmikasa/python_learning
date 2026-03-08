# 类与对象中的封装
# 封装：将属性和方法包装在一个类中，隐藏内部实现细节，只暴露必要的接口给外部使用。
# 类中允许定义自己的私有成员变量和私有成员方法
# 私有成员变量和方法，不能被外部使用，但是可以被class内部使用

# 小练习
# 私有成员变量可以在创建对象的时候传参数进去，但是只能通过init初始化接收

class Phone:
    def __init__(self,brand,model):
        self.__is_5g_enable=True
        self.brand=brand
        self.model=model

    def show_info(self):
        print(f"手机品牌：{self.brand}，手机型号：{self.model}")


    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G网络已开启，可以使用5G网络了")
        else:
            print("5G网络已关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")



class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def show_core(self):
        print(f"{self.name}的成绩是{self.score}")


class GameRole:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp

    def shows_status(self):
        print(f"角色{self.name}当前血量为{self.hp}")
r1=GameRole("亚索",100)
r1.shows_status()
r1.hp=80
r1.shows_status()





