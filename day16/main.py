from file_define import TextFileReader,JsonFileReader
from data_define import Record

text_file_reader=TextFileReader("2011年1月销售数据.txt")
json_file_reader=JsonFileReader("2011年2月销售数据JSON.txt")

jan_data:list[Record]=text_file_reader.read_data()
feb_data:list[Record]=json_file_reader.read_data()

# 将两个月的list合并为1个月来进行计算
all_data:list[Record]=jan_data+feb_data

# 数据处理，计算每日总金额
# 日期：2011-01-01，订单号：9e8a65e6-0d8c-6d74-bb23-c3fa6eff8c08，销售额：231，省份：广东省
# 所以可以以日期为关键词。计算日期相同的天的金额
money=0
for key in all_data:
    if key.date=="2011-01-01":
        money+=int(key.money)
print(f"2011-01-01总销售额：{money}")

# 假如是计算每一天的金额呢？
# 可以用字典。以日期作为key，以金额作为value，然后遍历
data_dict={}
for record in all_data:     # 这里record是一个Record对象
    if record.date in data_dict:
        data_dict[record.date]+=int(record.money)
    else:
        data_dict[record.date]=int(record.money)
# 至此，data_dict字典里面保存了所有日期的金额。

print(f"2月2日销售额：{data_dict["2011-02-02"]}")