# 依旧是综合小练习

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__is_borrowed=False        # 私有属性，表示书籍是否被借出去

    def borrow(self):
        if not self.__is_borrowed:
            print("借阅成功")
            self.__is_borrowed=True
        else:
            print("这本书已被借出")

    def return_book(self):
        if self.__is_borrowed:
            print("归还成功")
            self.__is_borrowed=False
        else:
            print("这本书当前未借出")

    def is_borrowed(self):
        return self.__is_borrowed

    def check_status(self):
        if self.__is_borrowed:
            return "已借出"
        else:
            return "未借出"

    def show_info(self):
        print(f"书名：{self.title}，作者：{self.author}，状态：{self.check_status()}")

    def __str__(self):
        return f"书名：{self.title}，作者：{self.author}，状态：{self.check_status()}"

class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size=file_size

    def show_info(self):
        print(f"电子书：{self.title}，作者：{self.author}，大小：{self.file_size}MB，状态：{self.check_status()}")

class PaperBook(Book):
    def __init__(self,title,author,pages):
        super().__init__(title,author)
        self.pages=pages

    def show_info(self):
        print(f"纸质书：{self.title}，作者：{self.author}，页数：{self.pages}，状态：{self.check_status()}")

def show_book_detail(book):
    book.show_info()

