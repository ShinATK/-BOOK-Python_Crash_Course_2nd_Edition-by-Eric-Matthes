# 创建一个 RandomWalk 类，它随机的选择前进的方向。
# 需要有三个属性：一个是存储随机漫步次数的变量，其他两个是列表，分别存储随机漫步经过的每个点的 x 和 y 坐标
# 使用模块 random 中的 choice() 来决定使用哪种选择

from random import choice

class RandomWalk:
    """一个生成随机漫步数据的类。"""

    def __init__(self, num_points=50_000):
        """初始化随机漫步属性"""
        self.num_points = num_points

        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    # 选择方向
    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 & y_step == 0:
                continue

            # 计算下一个点的x值与y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

