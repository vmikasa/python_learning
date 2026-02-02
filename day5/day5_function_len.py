# 统计字符串长度，不使用内置函数len()

str1="zai gou side"

def my_len():
    count=0
    for x in str1:
        count+=1
    print(count)

def my_square(num):
   return num*num

def is_even(num):

    if num %2==0:
        return True
    else:
        return False




def arithemetic_sum(a1,an,step):
   if step==0:
       return None
   else:
       sn=0
       for i in range(a1,an+step,step):
           sn+=i
        return sn


print(my_square(3))
print(my_square(2.5))

print(is_even(7))
print(is_even(10))

print(arithemetic_sum(1,100,1))

