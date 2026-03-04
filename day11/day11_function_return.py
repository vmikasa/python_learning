# something about function
# 函数多返回值，返回是元组
def func():
    return 1, 2, 3

result = func()
print(result)  # 输出：(1, 2, 3)

# 函数多返回值，返回是列表
def func2():
    return [1, 2, 3]

# 注意，虽然返回的是列表，但是这个列表是一个整体，因此返回值是一个列表，而不是三个元素
result2 = func2()
print(result2)  # 输出：[1, 2, 3]

# 函数多返回值，返回是字典
def func3():
    return {"a": 1, "b": 2, "c": 3}

# 注意，虽然返回的是字典，但是这个字典是一个整体，因此返回值是一个字典，而不是三个键值对
result3 = func3()
print(result3)  # 输出：{'a': 1, 'b': 2, 'c': 3}

# 函数多返回值，返回是字符串
def func4():
    return "abc"

# 注意，虽然返回的是字符串，但是这个字符串是一个整体，因此返回值是一个字符串，而不是三个字符
result4 = func4()
print(result4)  # 输出：abc

# 函数多返回值，返回是集合
def func5():
    return {1, 2, 3}

# 注意，虽然返回的是集合，但是这个集合是一个整体，因此返回值是一个集合，而不是三个元素
result5 = func5()
print(result5)  # 输出：{1, 2, 3}

# 函数多返回值，返回是元组，但是没有括号
def func6():
    return 1, 2, 3

# 注意，虽然返回的是元组，但是没有括号，但是这个元组是一个整体，因此返回值是一个元组，而不是三个元素
result6 = func6()
print(result6)  # 输出：(1, 2, 3)

# 返回的元组可以被解包
x,y,z=func6()
print(x)    # 输出：1
print(y)    # 输出：2
print(z)    # 输出：3