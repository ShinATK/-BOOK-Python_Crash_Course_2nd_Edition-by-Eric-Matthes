# 15-7：同时投掷三个骰子 同时投掷三个D6时，可能得到的最小点数为3，最大点数为18.请通过可视化展示同时投掷3个D6的结果

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


die_1 = Die()
die_2 = Die()
die_3 = Die()

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll() + die_3.roll())

# 分析结果
frequencies = []
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化,dtick设置为1，是为了将x轴全部刻度都显示
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title':'结果', 'dtick':1}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='投掷一个D6和一个D10 50000次的结果', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='3d6.html')