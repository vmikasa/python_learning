# 文件的打开、读写、关闭等基本操作

# 打开文件：使用open函数
# open函数的语法：open（name,mode,encoding）
# name是打开的文件名，可以追加路径。mode是打开的模式，比如只读模式，写入模式，追加模式。encoding是编码格式
# mode的模式：
# r，以只读模式打开。w，以写入模式打开。打开未存在的文件，则创建新文件。打开已存在的文件，则原有内容会被删除。a，以追加模式打开。原有内容保留。若文件不存在，则创建新文件

# 基本的读取方法有read和readline。其中read是一次性读取所有的数据，适合小文件。readline是一行一行读取，并且返回列表，适合大文件
# 需要注意的是，使用read方法读取文件，读取后指针会到最末尾，也就是说，每打开一次文件，read（）只能读取一次。如果想重新读取，需要用f.seek(0)，将指针重新移到开头
# read（3）表示读取前3个字
# 其中，with open （...） as f：
# for line in f 等价于readlines（）
# 注意，readline是读取一行，但是readlines是读取多行
# 基本语法应该是，打开，操作，关闭
# 示例：
f=open("test.txt","r",encoding="utf-8")
# print(type(f))
# txt=f.read()
# print(type(txt))
# print(txt)
txt=f.readlines()
print(txt)

f.close()

# 下面是一个小练习,关于读取
with open("city.txt","r",encoding="utf-8") as f:
    content=f.read()

print(content.count("shanghai"))

# 下面是写入练习
# 注意，write是写入内存缓冲区，flush才是真正写入硬盘
# 再次注意。close方法是自带flush的，with open as f不仅自带close，也自带flush
with open("zaigou.txt","w",encoding="utf-8") as f:
    f.write("灾狗无敌啦")
    f.flush()

# writeline用于写多行，需要自己加换行符。而且writeline是要自己先把内容处理成列表，所以准确来说，writeline是写入列表的