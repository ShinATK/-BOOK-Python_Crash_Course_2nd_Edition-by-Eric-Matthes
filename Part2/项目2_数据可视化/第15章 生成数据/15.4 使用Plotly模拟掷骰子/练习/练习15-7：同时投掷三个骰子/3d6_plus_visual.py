from plotly.graph_objs import Bar, Layout
from plotly import offline

from my_die import Die

while True:

    die_1 = Die(6)
    die_2 = Die(6)
    die_3 = Die(6)

    results = []
    times = int(input("请输入投掷骰子次数:"))

    for roll_num in range(1, times+1):
        result = die_1.roll() + die_2.roll() + die_3.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
    for value in range(3, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    x_values = list(range(2, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]
    x_axis_config = {'title':"结果", 'dtick':1}
    y_axis_config = {'title':"结果的频率"}
    my_layout = Layout(title=f'投掷三个D6 {times}次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data':data, 'layout':my_layout}, filename='练习/练习15-7：同时投掷三个骰子/3d6_plus.html')

    keep_running = input('Another round?(y/n):')
    if keep_running == 'n':
        break