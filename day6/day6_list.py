# 练习一下列表。今天少学一点，明天要驾照考试，没时间学习了。

my_list=["zai","gou","si","de"]

# for item in my_list:
#     print(item)

# for i in range(-1,-5,-1):
#     print(my_list[i])

list1 = [10, 20, 30, 40, 50]
print(str(list1))
num=len(list1)
print(list1[-1])
list1[1]=999
print(list1[1:4])
for item in list1:
    print(item)

for i,item in enumerate(list1):
    print(f"索引是{i}，值是{item}")


