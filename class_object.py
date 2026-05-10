#Create bank account.The Banck account class should have name and balance amount .
#It can have three methods deposit,withdraw and get account balance

class bankAccount():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def depositMoney(self,amount):
        self.balance+=amount
        print(f"{amount} has been deposited.Current balance is {self.balance}")
    def withDrawMoney(self,amount):
        if amount>self.balance:
            print("Insufficent Funds!")
        else:
            self.balance-=amount
            print(f"{amount} has been withdrawn.Current Balance is {self.balance}")
    def getAccountBalance(self):
        print(f"Current ballance is {self.balance} for {self.name}")


diptendu=bankAccount("Diptendu Bandyopadhyay",1500)
diptendu.depositMoney(15000)
diptendu.withDrawMoney(300)
diptendu.getAccountBalance()
