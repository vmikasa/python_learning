# -*- coding: utf-8 -*-

# 柱状图绘制
from pyecharts.charts import Bar, Timeline
from pyecharts import options
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

# 读取数据
with open("C:/Users/33226/Downloads/gdp_year_country_zh.csv", "r", encoding="utf-8") as f:
    data_lines = f.readlines()

# 创建一个空字典用于存储数据
# key: 年份, value: [[国家, GDP], ...]
data_dict = {}

# 过滤聚合项关键词（世界/高收入/OECD/地区/IDA/IBRD 等）
# 说明：这里用 Unicode 转义，避免终端编码导致关键词失真
EXCLUDE_KEYWORDS = [
    "\u4e16\u754c", "\u6536\u5165", "\u4eba\u53e3\u7ea2\u5229", "\u7ecf\u5408\u7ec4\u7ec7", "OECD",
    "\u6210\u5458", "\u5730\u533a", "IDA", "IBRD", "\u5408\u8ba1", "\u6b27\u76df", "\u6b27\u5143\u533a",
    "\u5206\u7c7b", "\u4e0d\u542b", "\u5317\u7f8e", "\u62c9\u4e01\u7f8e\u6d32", "\u52a0\u52d2\u6bd4",
    "\u6b27\u6d32\u548c\u4e2d\u4e9a", "\u4e1c\u4e9a\u548c\u592a\u5e73\u6d0b", "\u4e2d\u4e1c", "\u5317\u975e",
    "\u8106\u5f31\u4e0e\u51b2\u7a81", "\u6700\u4e0d\u53d1\u8fbe", "\u91cd\u503a\u7a77\u56fd", "\u5c0f\u56fd", "\u5357\u4e9a",
]

# 去除第一行表头中的 BOM 字符
if data_lines:
    data_lines[0] = data_lines[0].replace("\ufeff", "")

# 把读取到的数据放入字典
for line in data_lines:
    line = line.strip()     # 去掉首尾换行符和空格
    if not line:        # 跳过空行
        continue

    year = int(line.split(",")[0])
    country = line.split(",")[1].strip()
    gdp = float(line.split(",")[2])

    # 跳过分组/聚合项，只保留具体国家
    if any(keyword in country for keyword in EXCLUDE_KEYWORDS):
        continue

    if year in data_dict:       # 这里years是标准。先把同一年的所有国家都放在一个列表里，等到后面再处理每个年份的数据
        data_dict[year].append([country, gdp])
    else:
        data_dict[year] = [[country, gdp]]

# 构建时间线对象
timeline = Timeline(init_opts=options.InitOpts(theme=ThemeType.LIGHT)) # 创建时间线对象，设置主题为LIGHT

# 年份排序（从小到大）
# 由于这里year是key，所以只需要把所有的keys取出来排序即可
# data_dict.keys()返回一个包含所有年份的视图对象，但不是列表
# sorted函数可以对任何可迭代对象进行排序，并返回一个新的列表。这里我们对data_dict.keys()进行排序，得到一个包含所有年份的列表，按照从小到大的顺序排列
sorted_years = sorted(data_dict.keys())
# print(sorted_years) # 打印调试：查看排序后的年份列表
# 至此，年份排序完成

# 处理每个年份数据：按 GDP 降序取前 8
for year in sorted_years:
    data_dict[year].sort(key=lambda x: x[1], reverse=True)  # 按 GDP 降序排序。lambda x: x[1]表示按照每个国家GDP（即列表中的第二个元素）进行排序，reverse=True表示降序排序
    year_data = data_dict[year][:8] # 切片，取前八个

    # 至此，所有的数据都处理完成
    # 下面创建x轴和y轴数据列表，准备绘图
    x_data = [] # 把所有的国家名称放在x轴
    y_data = [] # 把所有的GDP数据放在y轴

    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000) # 这里把单位从美元转换为亿，方便展示

    # 打印调试：查看当前年份前 8 国家
    # print(x_data)  #打印调试x轴
    # print(y_data) 打印调试y轴

    # 在这个for循环里面，顺便就构建每一个柱状图对象了
    bar=Bar()
    x_data.reverse() # 反转x轴数据，使GDP最高的国家在最上面
    y_data.reverse() # 反转y轴数据，使GDP最高的国家在最上面
    bar.add_xaxis(x_data) # 添加x轴数据
    bar.add_yaxis("单位（亿美元）",y_data,label_opts=LabelOpts(position="right")) # 添加y轴数据
    # 反转x和y轴，使柱状图水平显示
    bar.reversal_axis()

    # 设置每一年图表的标题
    bar.set_global_opts(
        title_opts=options.TitleOpts(title=f"{year}年全球GDP前8国家", pos_left="center", pos_top="5%"),
        legend_opts=options.LegendOpts(is_show=False), # 不显示图例，因为只有一个系列
        tooltip_opts=options.TooltipOpts(is_show=True), # 显示提示框
    )

    # 当前年份，添加当前的bar到时间线对象中
    timeline.add(bar, str(year))

# 设置时间线自动播放
timeline.add_schema(
    play_interval=500,  # 每两秒切换一次
    is_auto_play=True,   # 自动播放
    is_loop_play=True,   # 循环播放
    is_timeline_show=False # 显示时间线
)

# 绘图
timeline.render()
