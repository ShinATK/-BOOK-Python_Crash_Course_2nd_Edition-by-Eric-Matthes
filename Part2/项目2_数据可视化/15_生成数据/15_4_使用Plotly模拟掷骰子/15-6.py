# 15-6：两个D8 编写一个程序，模拟同时投掷两个8面骰子1000次的结果。先想象一下结果会是什么样的，再运行这个程序，看看你的直觉准不准。

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = []

for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

print(results)