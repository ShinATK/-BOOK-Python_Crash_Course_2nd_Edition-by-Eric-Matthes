# 2-3：个性化消息 用变量表示一个人的名字，并向其现实一条消息。
# 例：Hello Eric, would you like to learn some Python today?
person_name = input('请输入姓名：')
print(f'Hello {person_name.title()}, would you like to learn some Python today?')

# 2-4：调整名字的大小写 用变量表示一个人的名字，再以小写，大写和首字母大写的方式显示这个人名
user_name = input('请输入姓名：')
print(f'小写：{user_name.lower()}')
print(f'大写：{user_name.upper()}')
print(f'首字母大写：{user_name.title()}')

# 2-5：名言 找一句你钦佩的名人说的名言，将其姓名和名言打印出来。输出应类似于下面这样（包括引号）
# 例：    Alebert Einstein once said, "A personwho never made a mistake never tried anything new."
someone_name = 'Jorge Luis Borges'
someone_said = 'What can I hold you with？'
name_said = f'{someone_name.title()} once said, "{someone_said}"'
print(f'\t{name_said}')

# 2-6：名言2 重复练习2-5，但用变量famous_person表示名人的姓名，再创建要显示的消息并将其赋给变量message，然后打印这条消息
famous_person = 'Jorge Luis Borges'
message = f'\t{famous_person.title()} once said, "{someone_said}"'
print(message)

# 2-7：剔除人名中的空白 用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符，务必至少使用字符组合'\t' '\n'各一次
# 打印这个人名，显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() rstrip() strip()对人名进行处理，并将结果打印出来
person = '\tJorge\tLuis\nBorges'
print(person)

print(f'使用lstrip：{person.lstrip()}')
print(f'使用rstrip：{person.rstrip()}')
print(f'使用strip：{person.strip()}')

