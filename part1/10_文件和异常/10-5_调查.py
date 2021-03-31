# 10-5 调查 编写一个while循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
while True:
    guest_reason = input('Type exit() to exit:')

    if guest_reason == 'exit()':
        break

    with open('guest_reason.txt', 'a') as file_reason:
        file_reason.write(f"{guest_reason}\n")

