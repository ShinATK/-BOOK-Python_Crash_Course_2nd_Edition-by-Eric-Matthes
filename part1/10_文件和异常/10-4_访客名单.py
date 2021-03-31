# 10-4 访客名单 编写一个while循环，提示用户输入名字。用户输入名字后，在屏幕上打印一条问候语，并将一条访客记录添加到文件guest_book.txt中。确保这个文件中的每条记录都占一行。
while True:
    guest_name = input('请输入用户名(exit() 以退出):')
    if guest_name == 'exit()':
        break
    print(f"Hello, {guest_name.title()}.")
    with open('guest_book.txt', 'a') as file_guest_record:
        file_guest_record.write(f"{guest_name.title()} has been here.\n")