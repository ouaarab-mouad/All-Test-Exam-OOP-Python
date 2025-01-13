class BankAccount:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin

    def deposit(self, pin, amount):
        if pin != self.pin:
            raise PinError("Invalid PIN")
        self.balance += amount
        return self.balance

    def withdraw(self, pin, amount):
        if pin != self.pin:
            raise PinError("Invalid PIN")
        if amount > self.balance:
            raise SoldeInsuffisant("Insufficient balance")
        self.balance -= amount
        return amount

    def get_balance(self, pin):
        if pin != self.pin:
            raise PinError("Invalid PIN")
        return self.balance

    def change_pin(self, oldpin, newpin):
        if oldpin != self.pin:
            raise PinError("Invalid PIN")
        self.pin = newpin

#parte 2
class SavingsAccount(BankAccount):
    def __init__(self, pin, interest_rate):
        super().__init__(pin)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

#parte 3
class FeeSavingsAccount(SavingsAccount):
    def __init__(self, pin, interest_rate, fee):
        super().__init__(pin, interest_rate)
        self.fee = fee

    def withdraw(self, pin, amount):
        amount += self.fee
        return super().withdraw(pin, amount)
    
