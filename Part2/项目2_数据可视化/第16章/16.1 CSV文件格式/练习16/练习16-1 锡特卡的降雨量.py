import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename_sitka = '../data/sitka_weather_2018_simple.csv'
filename_death_valley = '../data/death_valley_2018_simple.csv'

with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates_sitka, prcps_sitka = [], []
    for row in reader:
        current_date_sitka = datetime.strptime(row[2], '%Y-%m-%d')
        prcp_sitka = float(row[3])

        dates_sitka.append(current_date_sitka)
        prcps_sitka.append(prcp_sitka)

with open(filename_death_valley)as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates_death_valley, prcps_death_valley = [], []
    for row in reader:
        current_date_death_valley = datetime.strptime(row[2], '%Y-%m-%d')
        prcp_death_valley = float(row[3])

        dates_death_valley.append(current_date_death_valley)
        prcps_death_valley.append(prcp_death_valley)


plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates_sitka, prcps_sitka, c='red', alpha=0.5)
ax.plot(dates_death_valley, prcps_death_valley, c='blue', alpha=0.5)

# 设置图形的格式
ax.set_title('PRCP in 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制倾斜的日期标签，避免重合
ax.set_ylabel('PRCP', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

