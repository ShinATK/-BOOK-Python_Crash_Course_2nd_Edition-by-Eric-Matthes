from plotly.graph_objs import Bar, Layout
from plotly import offline

from ..my_die import Die

while True:

    die_1 = Die(8)
    die_2 = Die(8)

    results = []
    times = int(input("请输入掷骰子次数:"))

    for roll_num in range(times):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    x_values = list(range(2, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]
    x_axis_config = {'title':'结果', 'dtick':1}
    y_axis_config = {'title':'结果的频率'}
    my_layout = Layout(title=f'掷两个D8 {times}次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data':data, 'layout':my_layout}, filename='2d8_plus.html')

    keep_running = input('Another round?(y/n):')
    if keep_running == 'n':
        break