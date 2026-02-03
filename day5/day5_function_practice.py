# 函数案例小练习


money=5000000 # 灾狗的五千万
name=None

#   菜单
def menu():
    print()
    print(f'{"-"*15}主菜单{"-"*15}')
    print(f"{name}，欢迎来到灾狗的私家银行，请选择你的操作：")
    print(f'{"查询余额":<19}[输入1]')
    print(f'{"存款":<20}[输入2]')
    print(f'{"取款":<20}[输入3]')
    print(f'{"退出":<20}[输入4]')

    choice=input_non_negative_int("请输入您的选择：")
    return choice

#   查询余额
def query():
    print()
    print(f'{"-" * 15}查询余额{"-" * 15}')
    print(f"{name}，您的账户余额为：{money}元")
    print(f"{"-" * 40}")

#   存款
def saving():
    global money
    print()
    print(f'{"-"*15}存款{"-"*15}')
    num=input_non_negative_int("请输入您要存入的金额：")
    money += num
    print(f"存入{num}元，账户余额还剩下{money}元")

#   取款
def get_money():
    global money
    print()
    print(f"{"-"*15}取款{"-"*15}")
    num=input_non_negative_int("请输入您要取出的金额：")
    if num>money:
        print("余额不足，取款失败！")
    else:
        money -= num
        print(f"取出{num}元，账户余额还剩下{money}元")

def input_non_negative_int(prompt):
    """
    只接受非负整数的input()
    :param prompt:
    :return:int
    """
    while True:
        str1=input(prompt)
        if str1.isdigit():
            return int(str1)

        print("输入有误，请重新输入非负整数：")


def main():
    global name
    name=input("欢迎来到灾狗银行，请输入您的姓名：")
    while True:
        choice=menu()
        if choice==1:
            query()

        elif choice==2:
            saving()

        elif choice==3:
            get_money()

        elif choice==4:
            break
        else:
            print("输入有误，请重新选择，输入范围是1-4")


    print("感谢使用灾狗银行，欢迎下次光临！")

if __name__ == '__main__':
    main()