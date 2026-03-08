# 草稿练习

class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name}正在吃东西")

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color

    def meow(self):
        print(f"{self.name}在喵喵叫")


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_info(self):
        print(f"姓名：{self.name}，年龄：{self.age}")

class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score

    def shwo_score(self):
        print(f"{self.name}的成绩是{self.score}")