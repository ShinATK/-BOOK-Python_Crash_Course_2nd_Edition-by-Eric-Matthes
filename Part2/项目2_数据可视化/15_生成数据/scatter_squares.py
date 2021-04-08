import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# 设置图标标题并给坐标轴加上标签
ax.set_title('square num', fontsize=24)
ax.set_xlabel('num', fontsize=14)
ax.set_ylabel('square of num', fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()