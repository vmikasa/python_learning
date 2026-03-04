def print_file_info(file_path):
    """
    功能是打印指定目录的文件内容
    :param file_path: 文件名
    :return: 无return
    """
    f=None
    try:
        f=open(file_path,"r",encoding="utf-8")
        print("文件的全部内容如下：")
        for line in f:
            print(line)
    except FileNotFoundError:
        print(f"文件{file_path}不存在，请检查路径是否正确")
    finally:
        if f is not None:
            f.close()

def append_to_file(file_path,content):
    """功能是将content追加到指定目录的文件中
    :param file_path: 文件名
    :param content: 需要追加的内容
    :return: 无return
    """
    with open(file_path,"a+",encoding="utf-8") as f:
        f.write(content)
        f.flush()


if __name__ == '__main__':
    print_file_info("G:/Code Source/Python/restart/python_learning/day12/test.txt")
    append_to_file("test.txt","灾狗无敌啦！\n")