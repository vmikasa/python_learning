lst = [98, 90, 34, 56, 21]

n = len(lst)
# 冒泡排序
# for i in range(n-1):
#     swapped=False
#     for j in range(n-1-i):
#         if lst[j]<lst[j+1]:
#             lst[j],lst[j+1]=lst[j+1],lst[j]
#             swapped=True

#     if not swapped:
#         break

# print(lst)

# # 选择排序
# for i in range(n-1):
#     min_index=i     # 假设第一个元素是最小的。思路就是保持第一个元素最小，然后第二个元素最小
#     for j in range(i+1,n):      # j应该从i+1开始，因为是i与j比较，如果j从i开始，就无法比较了。因为是保持最前面的元素最小，所以最前面的元素是慢慢确定的
#         if lst[min_index]>lst[j]:       # 如果min_index比j大，那么就说明不满足min_index最小，把min_index更新
#             min_index=j
#     if min_index!=i:
#         lst[i],lst[min_index]=lst[min_index],lst[i]

# print(lst)

# # 插入排序

# for i in range(1,n):
#     current=lst[i]
#     j=i-1

#     while j>=0 and lst[j]<current:
#         lst[j+1]=lst[j]
#         j-=1            # 比较对象往前挪

#     lst[j+1]=current

# print(lst)
# print(lst)