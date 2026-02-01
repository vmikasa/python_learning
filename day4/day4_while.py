# 利用while循环，做等差数列计算小程序

print("等差数列计算小程序")
a1=int(input("请输入等差数列的起始项： "))
an=int(input("请输入终项："))
try:
    step=int(input("请输入等差数列的公差："))
except ValueError:
    print()
    print("你输入的公差有误，现在默认以1计算")
    step=1

current=a1 # 初始化计数变量current==a1，current即为当前项
sn=0 # 初始化sn==0
tag=False
if step>0:
    if a1<=an:
        tag=True
        while current<=an:    # 该条件等价于 当前项<=an的时候，执行循环
            sn += current
            current+= step   # a2=a1+d,因此该式子等价于把a1变成a2，以此类推，所以这里的current实际为当前项

elif step<0:
    if a1>=an:
        tag=True
        while current>=an:
            sn += current
            current+= step
else :
    print()
    print("公差不能为0，请重新运行程序并输入正确的公差值")

if tag:
    print(f"该等差数列，首项为{a1}，尾项为{an}，公差为{step}，求和等于{sn}")
