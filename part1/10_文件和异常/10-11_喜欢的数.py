# 编写一个程序，提示用户输入喜欢的数字，并使用json.dump()将这个数存储到文件中，再编写一个程序，从文件中读取这个值，并打印如下所示的消息。
#   I know your favorite number! It's _____.
import json

favr_num = input('请输入你喜欢的数字：')
filename = 'favorite_num.json'

