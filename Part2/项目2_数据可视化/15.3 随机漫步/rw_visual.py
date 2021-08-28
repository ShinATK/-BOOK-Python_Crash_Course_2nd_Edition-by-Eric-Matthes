# 15.3.3 绘制随机漫步图
# 15.3.4 模拟多次随机散步。
#   更新：增加循环，多次模拟随机漫步
# 15.3.5 设置随机漫步图的样式
#   更新：突出某些元素，如：漫步的器起点、终点和经过的路径

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个 RandomWalk 实例
    rw = RandomWalk()
    rw.fill_walk()

    # 将所有点绘制出来
    plt.style.use('classic')
    # 15.3.5 5. 调整尺寸以适合屏幕
    # figsize 指定生成的图形的尺寸，单位为英寸（1英寸=2.54厘米）,dpi传递分辨率
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)


    # # 15.3.5 1.给点着色
    # # edgecolors='none' 删除每个点周围轮廓
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 15.3.5 2.重新绘制起点和终点
    # 突出起点和终点
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 15.3.5 3.隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 15.3.5 4.增加点数
    # 5000 变为 50_000


    plt.show()

    keep_running = input('Make another walk?(y/n):')
    if keep_running == 'n':
        break