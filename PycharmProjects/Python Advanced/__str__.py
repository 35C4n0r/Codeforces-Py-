class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.id + " " + self.name


e1 = Employee('1', 'Raj')
print(e1)