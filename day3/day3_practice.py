# 如果不用while的简单的猜数字小练习

import random
num=random.randint(1,10)

guess=int(input("猜数字，1-10："))
if guess==num:
    print("恭喜你，第一次就猜对了")
else:
    if guess>num:
        print("你猜的数字太大了")
    else:
        print("你猜的数字太小了")
    guess=int(input("再猜一次，1-10："))
    if guess==num:
        print("恭喜你，第二次猜对了")
    else:
        if guess > num:
            print("你猜的数字太大了")
        else:
            print("你猜的数字太小了")

        guess=int(input("最后一次机会，1-10："))
        if guess==num:
            print("恭喜你，最后一次机会猜对了")
        else:
            print(f"很遗憾，三次机会都没猜对，正确答案是{num}")