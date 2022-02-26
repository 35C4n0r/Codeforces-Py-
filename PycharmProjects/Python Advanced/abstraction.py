from abc import ABCMeta, abstractmethod


class Customer(metaclass=ABCMeta):
    @abstractmethod
    def discount(self):
        pass


class Regcustomer(Customer):
    def discount(self):
        print("ARARARARARRARARARARARARARARARARA")


class precustomer(Customer):
    def discount(self):
        print("arararararararararaarararararararar")


r1 = Regcustomer()
r1.discount()