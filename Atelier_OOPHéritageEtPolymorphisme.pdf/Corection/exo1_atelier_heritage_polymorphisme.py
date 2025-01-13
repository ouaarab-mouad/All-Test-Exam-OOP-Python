class BankAccount:
    def __init__(self,pin,balance = 0):
        self.pin = pin
        self.balance = balance

    def dposit(self,pin,amount):
        if pin == self.pin:
            self.balance+= amount


        else:
            return 'Opération non autorisée !'

    def withdraw(self, pin, amount):
        if pin == self.pin and amount <= self.balance:
            self.balance -= amount
        else:
            return 'Opération non autorisée !'

    def get_balance(self, pin):
        if pin == self.pin:
            return  self.balance
        else:
            return 'Opération non autorisée !'

    def change_pin(self, oldpin, newpin):
        if oldpin == self.pin:
            self.pin = newpin

        else:
            return 'Opération non autorisée !'

class SavingsAccount(BankAccount):
    def __init__(self,pin,balance = 0,interest_rate = 0):
        super().__init__(pin,balance)
        self.interest_rate = interest_rate

    def add_interest(self):      
        self.balance +=  self.balance*self.interest_rate

class FeeSavingsAccount(SavingsAccount):
    def __init__(self,pin,balance = 0,interest_rate = 0,fees = 0):
        super().__init__(pin,balance,interest_rate)
        self.fees = fees

    def withdraw(self, pin, amount):
        super().withdraw(pin,amount+self.fees)
        
"""account1 = BankAccount(1234,1000)
account1.dposit(1234,200)
account1.withdraw(1234,500)
print(account1.get_balance(1234))


account2 = SavingsAccount(1234,1000,0.02)
account2.dposit(1234,300)
account2.add_interest()

print(account2.get_balance(1234))"""

account3 = FeeSavingsAccount(1234,1000,0.02,6)

account3.withdraw(1234,900)
print(account3.get_balance(1234))
