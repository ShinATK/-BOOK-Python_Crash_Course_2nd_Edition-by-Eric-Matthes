import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 使用内置样式
plt.style.use('seaborn')
fig, ax = plt.subplots()

# linewidth 设定绘制曲线的粗细
ax.plot(input_value, squares, linewidth=3)

# 设置图标标题并给坐标轴加上标签
ax.set_title("squares", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("squares of value", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()