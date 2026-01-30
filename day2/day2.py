# 复健第二天

# 定义一个变量，用来记录钱包余额
money=50

# 通过print语句，输出变量内容
print("钱包还有：",money)

# 买了个灾狗，花了10元
money=money-10

#现在还剩下money元，也就是40元
print(f"买了个灾狗，现在还剩下{money}元")
print(f"买了个灾狗，现在还剩下{money}元")

# 买个骨头
bone=15
print(f"给灾狗买个骨头，花了{bone}元")
money=money-bone
print(f"现在还剩下{money}元")

print(type("灾狗无敌啦"))
print(type(money))
print(type(1.2))

name="""叼你奶奶
灾狗无敌啦"""

print(name)

print("灾狗还有%s元"%money)
print("money的类型是",type(money))