# 列表的常用方法

my_list=["zai","gou","si","de"]

# 查询元素
# 语法： 列表.index（元素）
# 功能：查找指定元素在列表的下标，返回值是下标数字。如果找不到，则报ValueError
# 示例：
x=my_list.index("de")
print(x)    # 输出：3



# 插入元素
# 语法：列表.insert(下标，元素)
# 功能：在指定的下标插入指定的元素。补充说明，比如在第一处插入，那么原第一处元素顺位到第二处
# 示例：
my_list.insert(1,"😡")
print(my_list)      # 输出：['zai', '😡', 'gou', 'si', 'de']


# 追加元素
# 语法：列表.append(元素)
# 功能：在列表的末尾追加一个元素
# 示例：
my_list.append("发财啦")   # 原列表输出：['zai', '😡', 'gou', 'si', 'de']
print(my_list)      # 输出：['zai', '😡', 'gou', 'si', 'de', '发财啦']

# 追加其他数据容器元素
# 语法：列表.extend(其他数据容器)
# 功能：将其他数据容器内容取出，依次追加到列表末尾
# 示例:
my_list2=['6','6','6']
my_list.extend(my_list2)
print(my_list)      # 输出：['zai', '😡', 'gou', 'si', 'de', '发财啦', '6', '6', '6']


# 删除元素
# 语法1：del 列表[下标]        仅删除元素，没有返回值     如果不指定下标，则默认删除整个列表（注意，是删除掉列表这个变量，并不是清空列表）
# 语法2：列表.pop(下标)        pop的意思是弹出，因此删除元素的同时，返回值就是该元素。因为是把元素弹出       如果不指定下标，则默认删除最后一个元素
# 示例：
del my_list[1]
print(my_list)      # 输出：['zai', 'gou', 'si', 'de', '发财啦', '6', '6', '6']

element=my_list.pop(4)
print(element)      # 输出：发财啦


# 删除某元素在列表中的第一个匹配项
# 语法：列表.remove(元素)
# 功能：删除元素在列表中第一个匹配项。注意，只删除第一个
# 示例：
my_list.remove("6")
print(my_list)      # 输出；['zai', 'gou', 'si', 'de', '6', '6']



# 清空列表
# 语法：列表.clear()
# 功能：清空列表，只是让列表内容为空，但是仍然保留该列表变量
# 示例：
my_list.clear()
print(my_list)      # 输出：[]



# 修改元素
# 直接用赋值号即可
# 示例：
my_list=["zai","gou","si","de"]
my_list [0]="😭"     # 把原来的"zai"修改为"😭"
print(my_list[0])   # 输出：😭


# 统计列表中某元素的数量
# 语法：列表.count(元素)
my_list2=['6','6','6','7','7','8']
num=my_list2.count("7")
print(num)      # 输出：2


# 统计列表长度
# 语法：len(列表)
# 功能：统计列表长度，返回int类型变量
# 示例:
count=len(my_list2)
print(count)        # 输出：6