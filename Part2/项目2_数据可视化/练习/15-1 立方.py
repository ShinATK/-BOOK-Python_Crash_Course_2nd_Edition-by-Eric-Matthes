# 立方 请绘制一个图形，显示前5个整数的立方值。再绘制一个图形，显示前5000个整数的立方值。

# 导入 matplotlib 库
import matplotlib.pyplot as plt

set_values_x= input('请输入x的最大值：')

# 设置 x，y 数值
x_values = range(1, int(set_values_x)+1)
y_values = [x**3 for x in x_values]


# 设定绘图风格与获取图像与坐标轴属性
plt.style.use('seaborn')
fig, ax = plt.subplots()

# 传递 x，y 数值，设置点大小与曲线颜色
ax.scatter(x_values, y_values, s=10)

# 设置坐标轴标签与字体大小
ax.set_title('cubic values', fontsize=24)
ax.set_xlabel('values', fontsize=14)
ax.set_ylabel('cubic values', fontsize=14)

# 设置刻度标记大小
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置坐标轴取值范围
ax.axis([0, int(set_values_x), 0, int(set_values_x)**3])

# 绘制图像
plt.show()
