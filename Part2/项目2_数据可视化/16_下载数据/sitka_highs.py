import csv
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # next会返回文件的下一行，此出只调用了一次所i只返回第一行
    # print(header_row)

# 从文件中获取最高温度
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

    # print(highs)

# 根据最高温度绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# 设置图片的格式
ax.set_title('2018.7 Max_temperature on each day', fontsize=24)
ax.set_xlabel('', fontsize=24)
ax.set_ylabel('Temperature(F)', fontsize=24)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()