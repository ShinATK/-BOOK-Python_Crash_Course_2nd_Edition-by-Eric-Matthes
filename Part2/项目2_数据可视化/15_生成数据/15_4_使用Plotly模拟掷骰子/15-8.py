# 15-8：将点数相乘 同时投掷两个骰子时，通常将其点数相加。请通过可视化展示将两个骰子的点数相乘的结果。

from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint

class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

if __name__ == '__main__':

    die_1 = Die()
    die_2 = Die()

    results = []
    for roll_num in range(1000):
        results.append(die_1.roll() * die_2.roll())

    max_result = die_1.num_sides * die_2.num_sides
    frequencies = []
    for value in range(1, max_result+1):
        frequencies.append(results.count(value))

    x_values = list(range(1, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]
    x_label_config = {'title':'result', 'dtick':1}
    y_label_config = {'title':'frequency'}
    my_layout = Layout(title='同时投掷两个筛子的结果相乘', xaxis=x_label_config, yaxis=y_label_config)
    offline.plot({'data':data, 'layout': my_layout}, filename='2D6_mutiply.html')
