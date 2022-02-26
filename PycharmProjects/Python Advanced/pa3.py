class Employee:

    no_of_laptop = 40   #=====> Static variable or class variable (PUBLIC) #### This variable belong to the class and not to a particular object

    def allocate_laptop(self):
        print("allocating laptop")
        Employee.no_of_laptop -= 1
        print("remaining laptop = " + str(Employee.no_of_laptop))

e1 = Employee()
e1.allocate_laptop()

e2 = Employee()
e2.allocate_laptop()

e3 = Employee()
e3.allocate_laptop()

Employee.no_of_laptop = 80
e1 = Employee()
e1.allocate_laptop()

e2 = Employee()
e2.allocate_laptop()

e3 = Employee()
e3.allocate_laptop()
##############################################################################################################################################################
print()








print()
##################################################################################################################################################################
class Employee:
    __no_of_laptop = 40  # =====> Static variable or class variable (PRIVATE) #### This variable belong to the class and not to a particular object

    def allocate_laptop(self):
        print("allocating laptop")
        Employee.__no_of_laptop -= 1
        print("remaining laptop = " + str(Employee.__no_of_laptop))

Employee._Employee__no_of_laptop = 80 #======> ninja technique to acess static private variable class
e1 = Employee()
e1.allocate_laptop()

e2 = Employee()
e2.allocate_laptop()

e3 = Employee()
e3.allocate_laptop()

##############################################################################################################################################################
print()








print()
##################################################################################################################################################################
class Employee:
    __no_of_laptop = 40

    def allocate_laptop(self):
        print("allocating laptop")
        Employee.__no_of_laptop -= 1

    @staticmethod #=====> now get laptop count can be accesed just by mentioning class name see last line
    def get_laptop_count():
        print("No of laptop left = " + str(Employee.__no_of_laptop))
e1 = Employee()
e1.allocate_laptop()

e2 = Employee()
e2.allocate_laptop()

Employee.get_laptop_count()