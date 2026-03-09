# 数据定义类

# 示例：2011-01-01,9e8a65e6-0d8c-6d74-bb23-c3fa6eff8c08,231,广东省   # 即，日期，订单ID，销量额，省份

class Record:
    def __init__(self,date,order_id,money,province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"日期：{self.date}，订单号：{self.order_id}，销售额：{self.money}，省份：{self.province}"
