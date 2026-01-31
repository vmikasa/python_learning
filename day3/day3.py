# 热身
name=input("请输入你的名字：")
birth_year=int(input("请输入你的出生年份："))
age=2026-birth_year
print(f"你叫{name}, 今年{age}岁了")

# 股票计算小程序
name="灾狗的公司"
stock_price=23.6 #显然所示float类型
stock_count="0721" # 数字不能以0开头，所以只能用str
stock_price_daily_increase=1.2 # 显然是float类型
growth_day=int(input("请输入持有天数："))
print(f"公司：{name}，股票代码{stock_count}，当前股价{stock_price}元")
print(f"每日增长系数是：{stock_price_daily_increase}元,经过{growth_day}天的增长，股价达到了{stock_price*stock_price_daily_increase**growth_day:.2f}元")
