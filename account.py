class Account:
    # initializing class variables name and balance.
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    # a few functions contained in the class Account ie deposit,withdraw,check
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance -= amount
        else:
            print('insuffiecient balance')

    def check(self):
        print(self.balance)

# using class Account and its constituent functions.
acc1=Account('Dennis',500000)
acc1.deposit(2000)
acc1.check()

# acc2=Account('Walt',60000)
# acc2.check()
# acc2.withdraw(10000)
# acc2.check()
