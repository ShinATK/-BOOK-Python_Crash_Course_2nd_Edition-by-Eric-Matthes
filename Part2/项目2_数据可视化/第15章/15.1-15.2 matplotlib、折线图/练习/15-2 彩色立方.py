# 给前边绘制的立方图像指定颜色映射

import matplotlib.pyplot as plt

set_values_x = int(input('请输入x最大值：'))+1

x_values = range(1, set_values_x)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title('cubic', fontsize=24)
ax.set_xlabel('values', fontsize=14)
ax.set_ylabel('cubic values', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, set_values_x, 0, set_values_x**3])

plt.show()

