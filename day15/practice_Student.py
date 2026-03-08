# 类的综合练习

class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

    def show_info(self):
        print(f"姓名：{self.name}，年龄{self.age}")

class Student(Person):
    def __init__(self,name,age,score,student_id):
        super().__init__(name,age)
        self.score=score
        self.__student_id=student_id

    def show_info(self):
        print(f"学生姓名：{self.name}，年龄：{self.age}，成绩：{self.score}")

    def show_student_id(self):
        print(f"学号：{self.__student_id}")

    def set_score(self,score:int):
        if 0<=score<=100:
            self.score=score
        else:
            print("成绩不合法")

class Teacher(Person):
    def __init__(self,name,age,subject:str):
        super().__init__(name,age)
        self.subject=subject

    def show_info(self):
        print(f"老师姓名：{self.name}，年龄：{self.age}，学科：{self.subject}")

def show_person_info(person):
    person.show_info()


teacher=Teacher("小明",66,"科学")
student=Student("小胡",21,88,123456)

teacher.show_info()
student.show_info()
student.set_score(100)
show_person_info(teacher)
show_person_info(student)

