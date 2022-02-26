class Address:
    def __init__(self, address_line, city, state):
        self.address_line = address_line
        self.city = city
        self.state = state


class Customer:
    def __init__(self, name, add):
        self.name = name
        self.customer_address = add


add = Address("abcd", "#1234", "qwerty")
s1 = Customer("Jay", add)
print(s1.customer_address.address_line)
print(s1.customer_address.city)
print(s1.customer_address.state)
