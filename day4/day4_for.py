# 用for循环写一个九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}×{j}={i*j}",end="\t")
    print()

# for循环遍历真好用