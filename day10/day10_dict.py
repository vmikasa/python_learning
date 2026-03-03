# 下面进行字典的学习

# 创建一个字典:{key:value, key:value, ...}
dict1 = {"name": "灾狗", "age": 18, "gender": "男"}

# 创建一个空字典：直接用花括号{}，或者使用内置函数dict()
dict2 = {}


# 访问字典中的元素：通过key来访问value
print(dict1["name"])  # 输出：灾狗
# 注意，如果访问的key不存在，那么会报错KeyError
# print(dict1["hobby"])  # 报错：KeyError: 'hobby'

# 获取字典中某个key对应的value，如果key不存在，则返回默认值None或者指定的默认值
print(dict1.get("hobby"))  # 输出：None
print(dict1.get("hobby", "没有这个爱好"))  # 输出：没有这个爱好

# 修改字典中的元素：直接通过key来修改value
dict1["age"] = 21  # 输出：{'name': '灾狗', 'age': 21, 'gender': '男'}

# 添加字典中的元素：直接通过key来添加value
dict1["hobby"] = "football"  # 输出：{'name': '灾狗', 'age': 21, '

# 删除字典中的元素：用del语句或者pop方法
del dict1["gender"]  # 输出：{'name': '灾狗', 'age': 21, 'hobby': 'football'}
print(dict1)

# 删除字典中的元素并返回被删除的value
hobby = dict1.pop("hobby")  # 输出：{'name': '灾狗', 'age': 21}
print(dict1)
print(f"被删除的爱好是：{hobby}")  # 输出：被删除的爱好是：football

# 清空字典：用clear方法
dict1.clear()  # 输出：{}
print(dict1)

# 嵌套字典
dict3 = {
    "student1": {"name": "灾狗", "age": 21},
    "student2": {"name": "小明", "age": 20}
}
print(dict3)  # 输出：{'student1': {'name': '灾狗', 'age': 21}, 'student2': {'name': '小明', 'age': 20}}

# 嵌套字典的调用
print(dict3["student1"]["name"])  # 输出：灾狗

# 字典的常用方法
# keys方法：返回一个包含字典所有key的视图对象
print(dict3.keys())  # 输出：dict_keys(['student1', 'student2'])

# values方法：返回一个包含字典所有value的视图对象
print(dict3.values())  # 输出：dict_values([{'name': '灾狗', 'age': 21}, {'name': '小明', 'age': 20}])

# items方法：返回一个包含字典所有key-value对的视图对象，每个key-value对以元组的形式表示
print(dict3.items())  # 输出：dict_items([('student1', {'name': '灾狗', 'age': 21}), ('student2', {'name': '小明', 'age': 20})])

# update方法：用另一个字典的key-value对来更新当前字典，如果有相同的key，则覆盖原来的value；如果没有相同的key，则添加新的key-value对
dict4 = {"student3": {"name": "小红", "age": 19}}
dict3.update(dict4)
print(dict3)  # 输出：{'student1': {'name': '灾狗', 'age': 21}, 'student2': {'name': '小明', 'age': 20}, 'student3': {'name': '小红', 'age': 19}}

# setdefault方法：如果key存在，则返回对应的value；如果key不存在，则添加key并设置默认值为None或指定的默认值，并返回默认值
print(dict3.setdefault("student1"))  # 输出：{'name': '灾狗', 'age': 21}
print(dict3.setdefault("student4", {"name": "小蓝", "age": 18}))  # 输出：{'name': '小蓝', 'age

print(dict3)  # 输出：{'student1': {'name': '灾狗', 'age': 21}, 'student2': {'name': '小明', 'age': 20}, 'student3': {'name': '小红', 'age': 19}, 'student4': {'name': '小蓝', 'age': 18}}

# 字典的遍历
# 遍历字典的key。注意这个for循环得到的是key，而不是value
for key in dict3.keys():
    print(key)  # 输出：student1 student2 student3 student4

# 遍历字典的value
for value in dict3.values():
    print(value)  # 输出：{'name': '灾狗', 'age': 21} {'name': '小明', 'age': 20} {'name': '小红', 'age': 19} {'name': '小蓝', 'age': 18}



# 字典小练习
dict6={
    "灾狗":{"部门":"总裁","工资":500000,"级别":3},
    "军爷":{"部门":"司令","工资":300000,"级别":3},
    "小红":{"部门":"灾狗的小娇妻","工资":200000,"级别":2},
    "鼠鼠":{"部门":"保安","工资":3000,"级别":1},
    "小明":{"部门":"宇宙无敌暴龙战士","工资":50000,"级别":6},
}

for key in dict6:
    if dict6[key]["级别"]==1:
        print(f"{key}升职加薪")
        dict6[key]["工资"]+=1000
        dict6[key]["部门"]="保安队长"
        dict6[key]["级别"]=2

for key in dict6.items():
    print(key)
