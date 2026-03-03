# 学习集合
# 集合里面的所有元素必须是可哈希的，也就是说不能包含可变元素（如列表这类的数据类型）。集合中的元素是无序的，不能通过索引访问。
# 集合的创建
my_set={1,2,3,4,5}
print(my_set)      # 输出：{1, 2, 3, 4, 5}

# 空集合的创建。 注意空集合的创建不能写成my_set2={},因为花括号默认是创建一个空字典，而不是空集合
my_set2=set()
print(my_set2)     # 输出：set()

# 创建集合的几种方法
s1 = {1, 2, 3}
s2 = set([1, 2, 2, 3])     # 从列表创建，会去重
s3 = set("banana")         # {'b', 'a', 'n'}（字符去重）

# 集合的增删改查
# 查找元素
print(3 in my_set)     # 输出：True
print(6 in my_set)     # 输出：False

# 添加元素：用add方法
my_set.add(6)
print(my_set)      # 输出：{1, 2, 3, 4

# 添加多个元素：用update方法
my_set.update([7, 8, 9])
print(my_set)      # 输出：{1, 2, 3, 4, 5, 6, 7, 8, 9}

# 删除元素：用remove方法。也可以用discard方法，区别是remove方法如果删除的元素不存在会抛出KeyError异常，而discard方法则不会抛出异常
my_set.remove(9)
print(my_set)      # 输出：{1, 2, 3, 4, 5, 6, 7, 8}
my_set.discard(9)
print(my_set)      # 输出：{1, 2, 3, 4, 5, 6, 7, 8} 不会抛出异常

# 关于集合的pop方法
# pop方法会随机删除集合中的一个元素，并返回被删除的元素。由于集合是无序的，所以无法确定被删除的元素是什么。
# 但是，pop()的 “随机” 是「顺序不保证」，而非「每次运行必不同」；在小整数集合 + 固定运行环境下，删除顺序会完全固定。
removed_element = my_set.pop()
print(f"被删除的元素是：{removed_element}")     # 输出：删除的元素是：？（每次运行可能不同）
print(my_set)      # 输出：{2, 3, 4, 5, 6, 7, 8}（每次运行可能不同）

# 集合的运算
# 交集：用intersection方法或&运算符
s4 = {1, 2, 3}
s5 = {2, 3, 4}
print(s4.intersection(s5))     # 输出：{2, 3}
print(s4 & s5)                # 输出：{2, 3}

# 并集：用union方法或|运算符
print(s4.union(s5))            # 输出：{1, 2, 3, 4}
print(s4 | s5)                 # 输出：{1, 2, 3, 4}

# 差集：用difference方法或-运算符
print(s4.difference(s5))       # 输出：{1}
print(s4 - s5)                # 输出：{1}

# 对称差集：用symmetric_difference方法或^运算符
print(s4.symmetric_difference(s5))    # 输出：{1, 4}
print(s4 ^ s5)                       # 输出：{1, 4}

# 集合的子集和超集
# 子集：用issubset方法或<=运算符
s6 = {1, 2}
print(s6.issubset(s4))       # 输出：True
print(s6 <= s4)             # 输出：True

# 超集：用issuperset方法或>=运算符
print(s4.issuperset(s6))     # 输出：True
print(s4 >= s6)             # 输出：True

# 集合的不可变版本：frozenset
# frozenset是集合的不可变版本，一旦创建就不能修改。frozenset支持集合的所有操作，但不支持添加或删除元素。
fs = frozenset([1, 2, 3])
print(fs)       # 输出：frozenset({1, 2, 3})

# 清空集合：使用clear方法
my_set.clear()
print(my_set)      # 输出：set()

# 集合的复制：使用copy方法
s7 = s4.copy()
print(s7)       # 输出：{1, 2, 3}

# 集合的长度：使用len函数
print(len(s4))      # 输出：3

# 集合的练习

fruits = ['苹果', '香蕉', '苹果', '橙子', '香蕉', '葡萄', '橙子', '草莓', '葡萄', '西瓜']
set1=set()
for x in fruits:
    set1.add(x)

print(set1)
print(len(set1))
