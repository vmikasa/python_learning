# json来做折线图
import json
from pyecharts import charts
from pyecharts import options

# line=charts.Line()      # 创建一个折线图对象
# line.add_xaxis(["中国","美国","英国","法国","德国"])   # 添加x轴数据
# line.add_yaxis("GDP",[14,21,2.8,2.7,3])     # 添加y轴数据
#
# # 设置全局项
# line.set_global_opts(
#     title_opts=options.TitleOpts(title="全球GDP展示",pos_left="center",pos_top="5%"),
#     legend_opts=options.LegendOpts(is_show=True),
#     tooltip_opts=options.TooltipOpts(is_show=True),
#     visualmap_opts=options.VisualMapOpts(is_show=True),
# )

map_chinese=charts.Map()
map_chinese.add("地图", [("中国", 14), ("美国", 21), ("英国", 2.8), ("法国", 2.7), ("德国", 3)], "world")
map_chinese.set_global_opts(
    title_opts=options.TitleOpts(title="全球GDP展示",pos_left="center",pos_top="5%"),
    legend_opts=options.LegendOpts(is_show=True),
    tooltip_opts=options.TooltipOpts(is_show=True),
    visualmap_opts=options.VisualMapOpts(is_show=True),
)



# 通过render方法将图表渲染出来，默认会生成一个html文件，可以在浏览器中打开查看图表
map_chinese.render()