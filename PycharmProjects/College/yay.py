class Bank:
    def __init__(self, IFSC_Code = 12345678, bankname="qwerty", branchname="qwerty2", loc="123"):
        self.IFSC_Code = IFSC_Code
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc


class Customer:
    def __init__(self, CustomerID, custname, address, contactdetails):
        self.CustomerID = CustomerID
        self.custname = custname
        self.address = address
        self.contactdetails = contactdetails


class Account(Bank):
    def __init__(self, loc="qwerty3", AccountID=1234567890, cust="dfghjk", balance=0):
        super().__init__()
        self.AccountID = AccountID
        self.cust = cust
        self.balance = balance


    def getAccountInfo(self):
        print(f"User's account's IFSC code is {self.IFSC_Code}")
        print(f"User's Bank name is {self.bankname}")
        print(f"User's Branch name is {self.branchname}")
        print(f"User's loc is {self.loc}")

    def deposit(self, amount=2000, condition=True):
        self.balance += amount

    def widthraw(self, neg=500):
        if self.balance >= neg:
            self.balance -= neg
        else:
            print("Not Enough Balance")

    def getBalance(self):
        print(self.balance)


class SavingsAccount(Account):
    def __init__(self, SMinBalance):
        super().__init__()
        self.SMinBalance = SMinBalance

    def getAccountInfo(self):
        print(f"User's account's IFSC code is {self.IFSC_Code}")
        print(f"User's Bank name is {self.bankname}")
        print(f"User's Branch name is {self.branchname}")
        print(f"User's loc is {self.loc}")

    def deposit(self, amount=2000, condition=True):
        self.balance += amount

    def widthraw(self, neg=500):
        self.SMinBalance = self.balance-neg
        if self.SMinBalance >= 0:
            self.balance -= neg
        else:
            print("Not Enough Balance")

    def getBalance(self):
        print(self.balance)
