import random
num=random.randint(1,100)   # 生成1-100之间的随机整数
tag=True  # while循环的标志变量

print("欢迎来到数字猜谜游戏！")
print("我已经选择了一个1到100之间的数字。")
print("下面我们来开始猜数字吧")
i=1 # 初始化猜测次数

while tag:
    print()
    try:
        guess=int(input(f"请输入你第{i}次猜的数字："))

    except ValueError:
        print("你输入的数字有误，请重新输入。")
        continue

    if guess<num:
        print("你输入的数字太小了！")
        i+=1
    elif guess>num:
        print("你输入的数字太大了！")
        i+=1
    else:
        print(f"恭喜你，第{i}次猜对了")
        tag=False
