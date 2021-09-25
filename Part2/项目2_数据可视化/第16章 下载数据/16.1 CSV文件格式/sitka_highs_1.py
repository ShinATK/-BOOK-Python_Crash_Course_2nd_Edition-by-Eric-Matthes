import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f: # 文件对象赋给f
    reader = csv.reader(f) # 用reader将存储的文件对象作为实参传递给reader，从而创建一个与该文件相关联的阅读器对象
    header_row = next(reader) # next可以获取文件的下一行，调用一次则只获取到文件的第一行，也就是标题行。
    # 此阅读器位置会被记住，所以后边16.1.3处遍历文件时，直接从文件的第二行开始
    # print(header_row)

    # 16.1.2 打印文件头及其位置
    # for index, column_header in enumerate(header_row): # enumerate()获取列表每个元素的索引和值
    #     print(index, column_header)

    # 16.1.3 提取并读取数据
    # 获取文件中最高温度
    highs = []

    # 16.1.4在图表中添加日期
    dates = []

    for row in reader:
        # 16.1.6在图表中添加日期
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        high = int(row[5])

        # 16.1.6在图表中添加日期
        dates.append(current_date)

        highs.append(high)

    print(highs)

    # 16.1.4 绘制温度图表
    # 根据最高温度绘制图形
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.set_xlabel('', fontsize=16)

    fig.autofmt_xdate() # 绘制倾斜的日期标签，避免重合

    ax.set_ylabel('Temperature(F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()