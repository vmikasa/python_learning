# 下面，我将进入类与对象的学习

class User:
    pass
user=User() # 创建了一个对象，叫user
print(user) # <__main__.User object at 0x000001E9BC8B0> 这是一个对象的内存地址
print(type(user)) # <class '__main__.User'> 这是一个User类的对象

class Clock:

    id=None
    price=None

    def ring(self):
        import winsound
        winsound.Beep(100,2000) # 频率为1000Hz，持续时间为1000ms

class Student():
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        # print(f"Student创建了一个类对象。并且，初始化name为{self.name}，age为{self.age}，address为{self.address}")

clock=Clock()
clock.ring()

student=Student("灾狗",21,"天家")


# 下面是简易的学生输入系统
student_count=int(input("请输入需要录入系统的学生数量："))      # 学生数量计数
student_list=[]     # 创建一个空列表，来存储学生对象

for i in range(student_count):
    # 怎么把对象存起来？很简单，每弄好一个对象，就append到列表里面，用的时候再取出来。这样可以把对象的所有属性也自然存好。
    name=input(f"请输入第{i+1}个学生的姓名：")
    age=int(input(f"请输入第{i+1}个学生的年龄："))
    address=input(f"请输入第{i+1}个学生的地址：")

    student=Student(name,age,address)       # 创建学生对象，并且将刚刚得到的学生信息传入进去
    student_list.append(student)            # 将学生对象存入列表中

print("学生信息录入完成！下面是所有学生的信息：")
for student in student_list:
    print(f"姓名：{student.name}，年龄：{student.age}，地址：{student.address}")
