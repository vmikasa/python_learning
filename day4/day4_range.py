# 看看range的特性。range（start，stop，step）

import random
num=random.randint(1,500)

count=0

for i in range(1,num+1):
    if i%2==0:
        count+=1

print(f"从1到{num}，一共有{count}个偶数")