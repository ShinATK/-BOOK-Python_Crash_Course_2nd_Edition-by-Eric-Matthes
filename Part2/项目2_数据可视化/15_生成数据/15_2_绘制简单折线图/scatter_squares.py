import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# c设置颜色，设置一个元组，分别表示红绿蓝的分量，越接近1颜色越深
# ax.scatter(x_values, y_values, color=(1, 0, 0), s=10)

# 颜色映射：用c赋予需要上色的映射数值，用cmap告知使用何种颜色映射
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


# 设置图标标题并给坐标轴加上标签
ax.set_title('squares', fontsize=24)
ax.set_xlabel('num', fontsize=14)
ax.set_ylabel('square of num', fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

plt.show()