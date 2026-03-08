# 判断某字符是否为字母或者数字，使用str内置方法来解决
str1="zai gou side"
str1.isdigit()  # 判断是否为全数字，返回值是布尔值
str1.isalpha()  # 判断是否为全字母，返回值是布尔值

# join是字符串内置方法，使用它来连接字符串
# join的语法：分隔符字符.join(可迭代对象)    这里的分割字符串指的是想要用什么字符拼接
# 例如
str2=",".join(str1)     # 将str1这个可迭代对象拆分，然后用逗号拼接起来，最后赋值给str2
print(str2)             # 输出：z,a,i, ,g,o,u, ,s,i,d,e


