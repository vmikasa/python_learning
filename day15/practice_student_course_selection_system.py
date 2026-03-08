# 还是简单的类练习

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_info(self):
        print(f"姓名：{self.name}，年龄：{self.age}")

    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}"

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
        self.__courses=[]       #保存学生已选课程名。私有属性。即学生课表

    def select_course(self,course):     # 学生自己选课
        if course.course_name in self.__courses:
            print("该课程已选择")
        else:
            course.add_student(self.name)    # 这里的self是学生那边的。所以self.name是学生名字。指的是，某节课列表追加某个学生的名字
            self.__courses.append(course.course_name)       # 这里的self是学生。因此是学生课表增加。学生课表增加，这节课也应该增加学生。也就是说，学生已选课表，追加某个课程


    def show_courses(self):
        if self.__courses:
            print(f"{self.name}已选课程：{",".join(self.__courses)}")
        else:
            print(f"{self.name}当前没有选课")

    def show_info(self):
        print(f"学生姓名：{self.name}，年龄：{self.age}，学号：{self.student_id}")

    def get_courses(self):
        return self.__courses   # 返回已选课程列表

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def show_info(self):
        print(f"老师姓名：{self.name}，年龄：{self.age}，学科：{self.subject}")

    def __str__(self):
        return f"{self.name}"


class Course:
    def __init__(self,course_name,teacher:Teacher):
        self.course_name=course_name
        self.teacher=teacher.name
        self.__students=[]      # 学生名单

    def add_student(self,student):      # 把学生加入选课名单
        if student in self.__students:
            print("该学生已在课程中")
        else:
            self.__students.append(student)     # 所以是课程名单增加学生
            print("加入课程成功")

    def show_students(self):
        if self.__students:
            print(f"{self.course_name}课程学生：{",".join(self.__students)}")
        else:
            print(f"{self.course_name}课程当前无人选课")

    def show_info(self):
        print(f"课程名：{self.course_name}，任课老师：{self.teacher}")

    def __str__(self):
        return f"课程名：{self.course_name}，任课老师：{self.teacher}"

def show_person_detail(person):
    person.show_info()

t1 = Teacher("王老师", 35, "Python")
t2 = Teacher("李老师", 40, "算法")

c1 = Course("Python基础", t1)
c2 = Course("数据结构", t2)

s1 = Student("小明", 18, "2026001")
s2 = Student("小红", 19, "2026002")

show_person_detail(t1)
show_person_detail(s1)

c1.show_info()
c2.show_info()

s1.select_course(c1)
s1.select_course(c2)
s2.select_course(c1)

s1.show_courses()
s2.show_courses()

c1.show_students()
c2.show_students()

print(c1)
print(s1)





