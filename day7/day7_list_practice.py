# # 好，今天把科目四考完了。驾照也算是考出来了，就做一个小练习，暂且休息一天吧
# # 接近过年时间越来越少了
# # 这两天进度慢下来，先把列表学完吧
#
#
#
# def list_while_func(list_even):
#
#     i=0
#     while i<len(my_list):
#         if my_list[i] % 2 == 0:
#             list_even.append(my_list[i])
#
#
#         i+=1
#
#
# def list_for_func(even_list):
#
#     for item in my_list:
#         if item % 2 == 0:
#             even_list.append(item)
#
# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# even=list()
# list_for_func(even)
# print(even)

def foo(x):
    x[0] = 999

def bar(x):
    x = [7, 7, 7]

a = [1, 2, 3]

foo(a)
print(a)

bar(a)
print(a)

# 有点像C语言里面的指针
