# 学习元组
# 元组与列表的区别:元组可以调用的方法比列表少,元组的元素不能修改,元组使用小括号,列表使用方括号。注意元组的判定依据是逗号
# 注意，元组查找不到就没有默认值。但是字典有默认值
# 下面是元组练习

tuple1=("灾狗",21,["football","music"])
print(tuple1)
# 查询年龄所在的下标位置
print(f"年龄的下标是：{tuple1.index(21)}")

# 查询学生的姓名
print(f"学生的姓名是：{tuple1[0]}")

# 删除学生爱好中的football
del tuple1[2][0]
print(tuple1)

# 增加爱好coding到list里面
# 注意，元组本身是不能增删修改的。能够增删修改的是元组里面的可变数据容器

tuple1[2].append("coding")
print(tuple1)
