# 15-3：分子运动 修改rw_visual.py文件，将其中的ax.scatter()替换为ax.plot()。为模拟花粉在水滴表面的运动路径，向plt.plot()传递rw.x_values和rw.y_values，并指定实参linewidth。请使用5000个点而不是50 000个点。

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk()
    rw.fill_walk()
    # 将所有的点都绘制出来
    plt.style.use('classic')
    # 调整尺寸以适应屏幕(英寸)
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    # edgecolors='none'是为了去掉每个点的轮廓
    ax.plot(rw.x_values, rw.y_values, linewidth=5)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk?(y/n):')
    if keep_running == 'n':
        break
