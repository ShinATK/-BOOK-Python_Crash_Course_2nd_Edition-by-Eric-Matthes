import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    # alpha为透明度，0为完全透明，1为默认，不透明
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    ax.set_title('Temperature in 2018', fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate() # 绘制倾斜的日期标签，避免重合
    ax.set_ylabel('Temperature(F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()