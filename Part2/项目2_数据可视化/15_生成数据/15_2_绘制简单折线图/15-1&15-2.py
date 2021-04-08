# 15-1：立方 数的三次方称为立方。请绘制一个图形，显示前5个整数的立方值。再绘制一个图形，显示前5000个整数的立方值。
# 15-2：彩色立方 给前面绘制的立方图指定颜色映射。

import matplotlib.pyplot as plt

def set_values(n):

    x_values = range(n+1)
    y_values = [x**2 for x in x_values]

    return x_values, y_values

def draw_squares(x, y):

    fig, ax = plt.subplots()

    ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=20)

    ax.set_title('squares', fontsize=24)
    ax.set_xlabel('x_values', fontsize=14)
    ax.set_ylabel('y_values', fontsize=14)

    ax.tick_params(axis='both', which='major', labelsize=14)

    plt.show()

    return 0

if __name__ == '__main__':

    x, y = set_values(5)
    draw_squares(x, y)

    x, y = set_values(5000)
    draw_squares(x, y)
