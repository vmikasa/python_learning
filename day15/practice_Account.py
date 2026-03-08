# 下面依然是类与对象的练习

class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    def deposit(self,money):    # 存钱
        if money>0:
            self.__balance+=money
        else:
            print("存款金额不合法")

    def withdraw(self,money):   # 取钱
        if 0<money<=self.__balance:
            self.__balance-=money
        else:
            print("取款失败")

    def show_balance(self):
        print(f"{self.owner}，余额：{self.__balance}")

    def get_balance(self):
        return self.__balance   # 获取当前余额

    def __str__(self):
        return f"账户名：{self.owner}，余额：{self.__balance}元"

    def set_balance(self,balance):
        self.__balance=balance


class SavingsAccount(Account):
    def __init__(self,owner,balance,interest_rate:float):
        super().__init__(owner,balance)
        self.interrest_rate=interest_rate

    def add_interest(self):

        balance=self.get_balance()  # 获取当前余额
        money=balance*self.interrest_rate # 计算存钱一年的本息
        self.deposit(money)     # 将利息存入账户，更新账户


class CreditAccount(Account):
    def __init__(self,owner,balance,limit):     # 新增属性透支度
        super().__init__(owner,balance)
        self.limit=limit

    def withdraw(self,money):
        balance=self.get_balance()
        if 0<money<balance:
            balance-=money
            self.set_balance(balance)
        elif money>balance and money-balance<self.limit:
            balance-=money
            self.set_balance(balance)
            print(f"可以透支取钱，余额为{money-balance}。最多可透支{self.limit}元")
        elif money-balance>self.limit:
            print("无法取钱，余额不足，且超过透支额度")

def show_account_info(account):
    print(account)


