def str_reverse(s):
    """
    反转字符串
    :param s: 输入字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s,start,end):
    """
    截取字符串
    :param s: 输入字符串
    :param start: 起始位置
    :param end: 结束位置
    :return: 截取后的字符串
    """
    return s[start:end]

if __name__ == '__main__':
    s=str_reverse("hello")
    print(s)

