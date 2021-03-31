# 10-3 访客 编写一个程序。提示用户输入名字。用户做出响应后，将其名字写入文件guest.txt中
guest_name = input('请输入用户名：')
with open('guest.txt', 'a') as file_guest:
    file_guest.write(guest_name + '\n')



