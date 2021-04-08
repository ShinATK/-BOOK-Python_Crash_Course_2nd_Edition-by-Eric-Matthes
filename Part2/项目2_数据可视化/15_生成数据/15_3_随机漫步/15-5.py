# 15-5：重构 方法fill_walk()很长。请新建一个名为get_step()的方法，用于确定每次漫步的距离和方向，并计算每一步。然后，在fill_walk()中调用get_step()两次：
# x_step = self.get_step()
# y_step = self.get_step()
# 通过这样的重构，可以缩小方法fill_walk()。

# 15-4：改进的随机漫步 在类RandomWalk中，x_step和y_step是根据相同的条件生成的：从列表[1, -1]中随机选择方向，并从列表[0, 1, 2, 3,
# 4]中随机选择距离。请修改这些列表中的值，看看对随机漫步路径有何影响。尝试使用更长的距离选择列表（如：0~8），或者将-1从x或y方向列表中删除。

from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):

        while True:
            # 决定前进方向以及沿这个方向前进的距离。
            x_direction = choice([1, -1])

            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])

            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地散步
            if x_step == 0 and y_step == 0:
                continue
            else:
                break

        return x_step, y_step

    def fill_walk(self):
        """计算随机漫步包含的点"""
        # 不断漫步，直到列表达到指定长度
        while len(self.x_values) < self.num_points:
            x_step, y_step = self.get_step()

            # 计算下一个点的x与y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

if __name__ == '__main__':
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