# 关于lambda定义函数用法
# lambda匿名函数
# lambda参数列表:表达式
# lambda函数的参数可以有多个，但只能有一个表达式，表达式的结果就是函数的返回值
# lambda函数可以作为返回值返回，也可以作为参数传递
# lambda函数的使用场景：当需要一个简单的函数，但又不想命名一个函数时，可以使用lambda函数
# lambda函数语法：lambda 参数：执行表达式
# lambda函数的执行表达式只能写一行代码，不能写多行代码，如果需要写多行代码，只能使用def定义函数
# 示例：

def call_function(compute):
    result=compute(1,2)
    print(f"结果是{result}")

def compute(x,y):
    return x+y

call_function(compute)
call_function(lambda x,y:x+y)