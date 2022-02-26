'''class Employee:
    def __init__(self):
        self.id = None
        self.name = None


e1 = Employee()
e1.id = 1
e1.name = "jay"

e2 = Employee()
e2.id = 2
e2.name = "shachi"'''


'''class Employee:
    def __init__(self, eid, ename):
        self.id = eid
        self.name = ename
        
    def working(self):
        print("working")


e1 = Employee(1, "raj")
print(e1.id)

e1.working()'''

class Employee:
    def __init__(self):
        self.id = None
        self.name = None
        self.__salary = 50000 #==> private instace variable i.e cannot be accesed outside the class.
    def working(self):
        print("working")
        print(self.__salary) #==> This is how we acess it frm inside the class


e1 = Employee()
print(e1.id)
#only way to acess it is
print(e1._Employee__salary) #==> this is how we acess it from outside the class(a secret ninja technique)
e1.working()