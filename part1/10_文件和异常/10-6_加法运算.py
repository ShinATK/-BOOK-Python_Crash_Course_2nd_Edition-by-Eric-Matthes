# 提示用户提供数值输入时，常出现问题是，用户提供的是文本而不是数。在此情况下，当你尝试将输入转换为整数时，将引发ValueError异常。编写一个程序，提示用户输入两个数字，再将其相加并打印结果。在用户输入的任何一个值不是数时都捕获ValueError异常，并打印一条友好的错误信息。

try:
    while True:
        number_1 = input('请输入第一个数字：')
        try:
            int(number_1)
        except ValueError:
            print('请正确输入数字。\n')
            continue
        else:
            break

    while True:
        number_2 = input('请输入第二个数字：')
        try:
            int(number_2)
        except ValueError:
            print('请正确输入数字。\n')
            continue
        else:
            break

except ValueError:
    pass
else:
    answer = int(number_1) + int(number_2)
    print(f"\n{number_1} + {number_2} = {answer}")
