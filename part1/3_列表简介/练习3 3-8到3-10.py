# 3-8：放眼世界 想出至少5各你渴望去旅游的地方
place_travel = ['Cambridge', 'Babel Tower', 'Antarctica', 'London', 'Akihabara']
print('origin list:', place_travel, '\n')

# sorted按字母顺序打印，同时不要修改
changed_list = sorted(place_travel)
print('changed list:', changed_list)
print('origin list check:', place_travel, '\n')

# sorted按与字母顺序相反的顺序打印，同时不要修改
changed_list_reverse = sorted(place_travel,reverse=True)
print('changed list reverse:', changed_list_reverse)
print('origin list check again:', place_travel, '\n')

# reverse()修改元素排列顺序，核实排列顺序改变
place_travel.reverse()
print('reversed list:', place_travel, '\n')

# reverse()再次反转顺序
place_travel.reverse()
print('reversed reversed list:', place_travel, '\n')

# sort()按字母顺序
place_travel.sort()
print('alpha list:', place_travel, '\n')

# sort()按与字母顺序相反
place_travel.sort(reverse=True)
print('reverse alpha list:', place_travel, end='\n')

