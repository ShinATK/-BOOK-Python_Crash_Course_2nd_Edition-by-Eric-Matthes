# 3-4：嘉宾名单 如果你可以邀请任何人一起共进晚餐，你会邀请哪些人？
# 请创建一个列表，其中包含至少三个你想邀请的人，然后使用这个列表打印信息，邀请这些人来与你共进晚餐。
guest_name = ['NegoroYatsude', 'Akame', 'Ayanami Lei']
print(f'The guests\' name that I want to invite '
      f'{guest_name[0].title()}、 {guest_name[1].title()} and {guest_name[2].title()}.')
# 3-5：修改名单 以练习3-4的程序为基础，在程序末尾添加一条print语句，指出哪位嘉宾无法赴约。
# 修改嘉宾名单，将无法赴约的嘉宾姓名替换为新邀请的嘉宾的姓名
# 再打印一系列消息，向名单中的每位嘉宾发出邀请
print(f'Guest {guest_name[2]} will be absent.')

guest_name[2] = 'Black Rock Shooter'
print(f'The guests\' name that I want to invite '
      f'{guest_name[0].title()}、 {guest_name[1].title()} and {guest_name[2].title()}.')

# 3-6：添加嘉宾
# 使用insert添加到名单开头
# 使用insert添加到名单中间
# 使用append添加到in孤单末尾
# 发出邀请
guest_name.insert(0, 'New one')
guest_name.insert(2, 'New one_2')
guest_name.append('New one_3')
print(f'The guests\' name that I want to invite {guest_name}.')

# 3-7
while len(guest_name) >2:
    guest_kick = guest_name.pop()
    print(f'sry for that {guest_kick}')
print(f'last two {guest_name}')

del guest_name[0:2]
print(guest_name)