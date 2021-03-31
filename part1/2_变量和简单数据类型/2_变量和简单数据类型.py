
# 在字符串中插入变量的值（占位符之外的方法）
# f字符串 是Python3.6版本引入
# Python3.5或更早版本则应使用format
# full_name = '{} {}'.format(first_name, last_name)
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name.title())

# 使用制表符或换行符来添加空白
# 空白泛指任何非打印字符，如空格、制表符和换行符
print('Languages:\n\tPython\n\tC\n\tJavaScript')

# 删除空白

#1.删除字符串末尾空白
# .rstrip()方法会直接修改变量的值
favorite_language = 'python '
favorite_language.rstrip()
print(favorite_language)

#2.删除字符串开头空白或同时剔除首尾空白
# .lstrip()
