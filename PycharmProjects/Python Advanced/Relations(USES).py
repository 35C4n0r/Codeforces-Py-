class Car:
    def start(self):
        print("Car has started")


class Driver:
    def travel(self):
        c = Car()
        c.start()
        print("Driver has started driving")


d = Driver()
d.travel()


print()
print()


class Laptop:
    def __init__(self, brand):
        self.brand1 = brand


class Employee:
    def __init__(self, name):
        self.name1 = name
    def to_work(self, ll):
        if ll.brand1 == "Dell":
            print("Yay")



lap1 = Laptop("Dell")
j = Employee("Raj")
j.to_work(lap1)
