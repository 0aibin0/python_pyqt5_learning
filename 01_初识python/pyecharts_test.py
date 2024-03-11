
from pyecharts.charts import Line

line = Line()
line.add_xaxis(["中国", "美国", "日本"])
line.add_yaxis("GDP", [30, 20, 10])
line.render()