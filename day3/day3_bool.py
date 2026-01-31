# 学习布尔类型数据

# 定义变量存储布尔类型的数据
bool1=True
bool2=False

print(f"bool1的内容是{bool1},类型是{type(bool1)}")
print(f"bool2的内容是{bool2},类型是{type(bool2)}")

bool3=3>1
print(f"3>1的结果是{bool3},类型是{type(bool3)}")
bool4=3<1
print(f"3<1的结果是{bool4},类型是{type(bool4)}")

# 布尔类型，True本身的返回值是整数1，False本身的返回值是整数0
print(f"bool3+1={bool3+1},类型是{type(bool3+1)}")
print(f"bool4+1={bool4+1},类型是{type(bool4+1)}")

# 布尔类型可以和整数进行运算
print(f"bool3*10={bool3*10},类型是{type(bool3*10)}")
print(f"bool4*10={bool4*10},类型是{type(bool4*10)}")

# 布尔类型可以和整数进行拼接
print(f"bool3和字符串拼接：{'结果是'+str(bool3)}")
print(f"bool4和字符串拼接：{'结果是'+str(bool4)}")

# 布尔类型可以进行逻辑运算
print(f"bool3 and bool4的结果是{bool3 and bool4},类型是{type(bool3 and bool4)}")
print(f"bool3 or bool4的结果是{bool3 or bool4},类型是{type(bool3 or bool4)}")
print(f"not bool3的结果是{not bool3},类型是{type(not bool3)}")
print(f"not bool4的结果是{not bool4},类型是{type(not bool4)}")

print()
print()

# 下面进行if语句的学习
print("下面进行if语句的学习\n")

age=21
if age>=18:
    print(f"灾狗已经{age}岁了，可以打瓦了")
print("灾狗莫叫太大声\n\n")

age=input("欢迎来到灾狗爱打瓦，请输入你的年龄：")
age=int(age)
if age>=18:
    print(f"灾狗已经{age}岁了，可以打瓦了")
else:
    print(f"灾狗只有{age}岁，小毛毛打什么打")
print("灾狗又乱叫起来了")


