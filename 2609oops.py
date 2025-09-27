# Q1. Build a bank with customers , accounts , balance , deposit and withdraw

class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def addCustomers(self, customers_list):

        self.customers.append(customers_list)

        print('Customers added to Bank')

    def addAccounts(self, accounts_list):

        self.accounts.append(accounts_list)
        print('Drivers are added to the Zone')
class Customer:
    def __init__(self,custId,custName):

        self.custId = custId
        self.custName = custName
        

class Account:
    def __init__(self, accountId, TotBalance):
        self.accountId = accountId
        self.TotBalance = TotBalance

    def reqWithdraw(self, withAmount):
        if self.TotBalance >= withAmount:
            self.TotBalance -= withAmount   # deduct amount
            print(f'Amount {withAmount} withdrawn successfully.')
            print(f'Updated Balance: {self.TotBalance}')
        else:
            print('Not enough Balance')



b1 = Bank()
c1 = Customer(1, 'Carlos')
a1 = Account(1023, 20000)

b1.addCustomer(c1)
b1.addAccount(a1)

a1.reqWithdraw(10000)   
a1.reqWithdraw(15000)

    



        

    
