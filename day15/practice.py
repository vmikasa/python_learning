# 打草稿用的练习

class Student:

    def __init__(self,name,score):
        self.name=name
        self.__score=score

    def show_score(self):
        print(f"{self.name}的成绩是{self.__score}")

    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            print("成绩必须在0到100之间")

class Cat:
    species="猫"

    def __init__(self,name,color):
        self.name=name
        self.color=color

    def show_info(self):
        print(f"名字：{self.name}，颜色：{self.color}，物种：{self.species}")

class Hero:
    def __init__(self,name,level):
        self.name=name
        self.level=level

    def show_info(self):
        print(f"英雄{self.name}当前等级为{self.level}")
    def level_up(self):
        self.level+=1

class Book:
    def __init__(self,title,price):
        self.title=title
        self.price=price

    def increase_price(self,value):
        self.price+=value

    def __str__(self):
        return "书名：{self.title}，价格：{self.price}"

class Airconditioner:
    def __init__(self,brand,temperature):
        self.brand=brand
        self.__temperature=temperature

    def show_temp(self):
        print(f"当前温度是{self.__temperature}")

    def set_temp(self,temp):
        if 16<=temp<=30:
            self.__temperature=temp
        else:
            print("设置的温度不合法")


class Vehicle:
    def __init__(self):
        pass

    def run(self):
        print("交通工具在运行")

class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def run(self):
        print("汽车在路上行驶")

class Plane(Vehicle):
    def __init__(self):
        super().__init__()


    def run(self):
        print("飞机在天空飞行")

class Employee:
    def __init__(self):
        pass

    def work(self):
        print("员工在工作")

class Programmer(Employee):
    def __init__(self):
        super().__init__()

    def work(self):
        print("程序员正在写代码")

class Designer(Employee):
    def __init__(self):
        super().__init__()
    def work(self):
        print("设计师在做设计")
