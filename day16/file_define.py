"""与文件相关的类"""
import json

from data_define import Record

# 先定义一个抽象类做顶层设计，确定有哪些功能需要实现
class FileReader:
    def __init__(self,path):
        self.path = path    # 目标文件位置

    def read_data(self)->list[Record]:
        """读取文件数据，将读取到的每一条数据都转换为Record对象，并且封装到list返回"""
        pass



# 下面是顶层抽象类的子类，做具体的功能实现
class TextFileReader(FileReader):
    """读取txt文件，最后返回读取后的对象列表。"""
    def __init__(self,path):
        super().__init__(path)



    def read_data(self) ->list[Record]:
        record_list = []
        with open(self.path,'r',encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                data_list=line.split(',')
                record=Record(data_list[0],data_list[1],data_list[2],data_list[3])     # 创建record实例对象
                record_list.append(record)

        return record_list

class JsonFileReader(FileReader):
    def __init__(self,path):
        super().__init__(path)

    def read_data(self) ->list[Record]:
        record_list = []
        with open(self.path,'r',encoding="utf-8") as f:
            for line in f:
                data_dict=json.loads(line)
                record=Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
                record_list.append(record)

        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("2011年1月销售数据.txt")
    lst1=text_file_reader.read_data()    # 返回值是对象列表。该对象有data,order_id,money,province四个属性
    json_file_reader=JsonFileReader("2011年2月销售数据JSON.txt")
    lst2=json_file_reader.read_data()    # 读取Json数据

    for line in lst1:
        print(line)

    for line in lst2:
        print(line)

