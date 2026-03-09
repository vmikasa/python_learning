import random
from datetime import datetime, timedelta

# 配置参数
start_date = datetime(2011, 1, 1)
days = 31  # 生成1月份的数据
provinces = ["湖南省", "河北省", "湖北省", "山东省", "安徽省", "广东省", "江苏省", "福建省", "浙江省", "四川省"]
output_file = "2011年1月销售数据.txt"

# 生成数据
with open(output_file, "w", encoding="utf-8") as f:
    for day in range(days):
        current_date = start_date + timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")

        # 每天生成10-20条记录
        for _ in range(random.randint(10, 20)):
            # 生成随机订单ID
            order_id = f"{random.getrandbits(128):032x}"
            order_id = "-".join([
                order_id[:8], order_id[8:12], order_id[12:16], order_id[16:20], order_id[20:]
            ])

            # 生成随机金额和省份
            amount = random.randint(100, 5000)
            province = random.choice(provinces)

            # 写入一行数据
            line = f"{date_str},{order_id},{amount},{province}"
            f.write(line + "\n")

print(f"数据集已生成：{output_file}")