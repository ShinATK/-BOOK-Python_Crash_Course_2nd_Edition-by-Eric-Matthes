class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f'{self.name} rolled over.')

# my_dog = Dog('Willie', 6)
#
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
#
# my_dog.sit()
# my_dog.roll_over()

class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 默认值

    def get_descriptive_name(self):
        """返回整洁对描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        """禁止将里程表读数回调"""
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

class ElectricCar(Car):
    """电动汽车"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

# my_new_car = Car('audi', 'A4', '2019')
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
#
# # 修改默认值
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#
# # 利用方法修改默认值
# my_new_car.update_odometer(33)
# my_new_car.read_odometer()

# 继承
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()