# 9_1 餐馆 创建一个名为Restaurant的类，为其方法__init__()设置属性restaurant_name 和 cuisine_type。
#   创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，
#   前者打印前两项信息，而后者打印一条消息，指出餐馆正在营业。
#   根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name}.")
        print(f"And it has {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant named {self.restaurant_name} is now opened.")

    def set_number_served(self, number):
        self.number_served = number
        return self.number_served

    def increment_number_served(self, number_today):
        self.number_served += number_today
        return self.number_served

restaurant_1 = Restaurant('name_1', 'eating things')

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

# 9-2 三家餐馆 根据为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法
#   descrive_restaurant()

restaurant_2 = Restaurant('name_2', 'eating things')
restaurant_3 = Restaurant('name_3', 'eating things')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# 9-3 用户 创建一个名为User的类，其中包含属性first_name last_name,
#   以及用户简介通常会存储其他几个属性。在类User中定义一个名为describe_user()的方法，
#   用户打印用户信息摘要。再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
#   创建多个表示不同用户的实例，并对每个实例调用上述两个方法。

class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's first name is {self.first_name} and last name is {self.last_name}.")

    def greet_user(self):
        print(f"Hi, {self.first_name}. What a good day!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

user_1 = User('abusoruto', 'tarutarosi')
user_2 = User('urutora', 'man')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

# 9-4 就餐人数 在为完成练习9-1而编写的程序中，添加一个number_served 的属性，并将其默认值设置为0。根据这个类创建一个restaurant的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
#   添加一个名为set_number_served()的方法，让你能够设置就餐人数。调用这个方法并向它传递一个这样的值，然后再次打印这个值。
#   添加一个名为increment_number_served()的方法，让你能够将就餐人数递增。调用这个方法并尝试向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

restaurant_4 = Restaurant('restaurant_4', 'eating things')
print(f'Number served:{restaurant_4.number_served}')
restaurant_4.number_served = 3
print(f'Number served:{restaurant_4.number_served}')

print(restaurant_4.set_number_served(5))

print(restaurant_4.increment_number_served(10))

# 9-5 尝试登陆次数 在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。编写一个名为increment_login_attempts()的方法，将属性login_attempts的值加1。再编写一个名为reset_login_attempts()的方法，将属性login_attempts的值重制为0。
#   根据User类创建一个实例，再调用方法increment_login_attempts()多次。打印属性login_attempts的值，确认它被正确的递增。然后调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重制为0。

user_3 = User('Ace', 'Zeta')
user_3.increment_login_attempts()
user_3.increment_login_attempts()
user_3.increment_login_attempts()
print(user_3.login_attempts)

user_3.reset_login_attempts()
print(user_3.login_attempts)

# 9-6 冰淇凌小店 冰淇凌小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承为完成练习9-1或练习9-4而编写的Restaurant类。这两个版本的Restaurant类都可以。添加一个flavors的属性，用于存储一个由各种口味的冰淇凌组成的列表。编写一个显示这些冰淇凌的方法，创建一个IceCreamStand的实例，并调用这个方法。

class IceCreamStang(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def show_flavors(self):
        print(self.flavors)

my_icecream = IceCreamStang('my_icecream', 'cold eating things')
my_icecream.show_flavors()

# 9-7 管理员 管理员是一种特殊的用户。编写一个名为Admin的类，让它继承为完成练习9-3或练习9-5而编写的User类。添加一个名为privileges的属性，用于存储一个由字符串（如："can add post"、"can ban user"等）组成的列表。编写一个名为show_privileges()的方法，显示管理员的权限。创建一个Admin实例，并调用这个方法。

# 9-8 权限 编写一个名为Privileges的类，它只有一个属性privileges，其中存储了练习9-7所述的字符串列表。将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges实例用作其属性。创建一个Admin实例，并使用方法show_privileges来显示其权限。

class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

admin = Admin('negoro', 'yatsude')
admin.privileges.show_privileges()

admin_1 = Admin('hikari', 'yokoe')
admin_1.privileges.show_privileges()

# 9-9 电瓶升级 在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()方法。该方法检查电瓶容量，如果不是100，就将其设置为100。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，然后对电瓶进行升级，并再次调用get_range()。你将看到这辆汽车的续航里程增加了。

