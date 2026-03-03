# 补充一下数据容器的通用操作
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}


# max语法：max(数据容器)
# 功能：返回数据容器中的最大值。注意，数据容器中的元素必须是可比较的，否则会抛出TypeError异常
print(max(my_list))      # 输出：5
print(max(my_tuple))     # 输出：5
print(max(my_str))       # 输出：g
print(max(my_set))       # 输出：5
print(max(my_dict))      # 输出：key5 因为字典默认比较的是键

# min语法：min(数据容器)
# 功能：返回数据容器中的最小值。注意，数据容器中的元素必须是可比较的，否则会抛出TypeError异常
print(min(my_list))     # 输出：1
print(min(my_tuple))    # 输出：1
print(min(my_str))      # 输出：a
print(min(my_set))      # 输出：1
print(min(my_dict))     # 输出：key1 因为字典默认比较的是键

# sort排序
# sort方法只能用于列表，不能用于其他数据容器。sort方法会对列表进行原地排序，也就是说会修改原列表，并且没有返回值
my_list.sort()
print(my_list)      # 输出： [1, 2, 3, 4, 5]

# sorted函数可以用于所有数据容器，sorted函数会返回一个新的列表，原数据容器不变
new_list = sorted(my_tuple)
print(new_list)     # 输出： [1, 2, 3, 4, 5]
print(my_tuple)    # 输出： (1, 2, 3, 4, 5) 原数据容器不变

# 如果要反向排序，可以传入参数reverse=True
new_list_desc = sorted(my_tuple, reverse=True)
print(new_list_desc)    # 输出： [5, 4, 3, 2, 1]

# 字符串比大小
# 字符串的比较是按照字典序进行比较的，也就是说先比较第一个字符，如果第一个字符相同，再比较第二个字符，以此类推，直到比较出大小或者比较到字符串末尾为止
print("abc" < "abd")    # 输出：True 因为c比d小
print("abc" < "abcd")   # 输出：True 因为前面三个字符相同，比较到字符串末尾，abc比abcd小
print("abc" < "abb")    # 输出：False 因为c比b大