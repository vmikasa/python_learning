# 黑心狗的故事
import random
money=10000

for i in range(1,21):
    print()
    level=random.randint(1,10)
    if money==0:
        print("钱发完了，黑心狗跑路了😡")
        break
    if level<5:
        print(f"绩效等级为{level}，低于5，不发工资")
        print("黑心狗克扣穷鼠鼠工资😭")

    else:
        print(f"向鼠鼠{i}发放1000元工资，财物还剩下{money-1000}元")
        money-=1000
