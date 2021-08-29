from random import randint

class Die:
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        # randint(1, num_sides)返回1到num_sides之间的随机整数
        return randint(1, self.num_sides)

