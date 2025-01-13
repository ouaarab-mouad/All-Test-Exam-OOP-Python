class SoldeInsuffisant(Exception):
    pass

class BankAccount:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
    
    def deposit(self, pin, amount):
        if pin == self.pin:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Invalid PIN")

    def withdraw(self, pin, amount):
        if pin == self.pin:
            if amount <= self.balance:
                self.balance -= amount
                return amount
            else:
                raise SoldeInsuffisant("Solde insuffisant pour le retrait")
        else:
            raise ValueError("Invalid PIN")

    def get_balance(self, pin):
        if pin == self.pin:
            return self.balance
        else:
            raise ValueError("Invalid PIN")

    def change_pin(self, oldpin, newpin):
        if oldpin == self.pin:
            self.pin = newpin
            print("Le code PIN a été changé avec succès.")
        else:
            raise ValueError("Invalid PIN")


# exepmle d'execution : 
# Création d'un compte bancaire avec un code PIN initial
account = BankAccount("1234")

# Dépôt de 100 euros sur le compte
account.deposit("1234", 100)
print("Solde après dépôt:", account.get_balance("1234"))  # Output: Solde après dépôt: 100

# Tentative de retrait de 50 euros
try:
    withdrawn_amount = account.withdraw("1234", 50)
    print("Montant retiré:", withdrawn_amount)  # Output: Montant retiré: 50
except SoldeInsuffisant as e:
    print(e)

print("Solde après retrait:", account.get_balance("1234"))  # Output: Solde après retrait: 50

# Tentative de retrait de 100 euros (montant supérieur au solde)
try:
    withdrawn_amount = account.withdraw("1234", 100)
    print("Montant retiré:", withdrawn_amount)
except SoldeInsuffisant as e:
    print(e)  # Output: Solde insuffisant pour le retrait

# Changement du code PIN
account.change_pin("1234", "5678")

# Tentative d'accès avec l'ancien code PIN
try:
    print("Solde actuel:", account.get_balance("1234"))
except ValueError as e:
    print(e)  # Output: Invalid PIN

# Accès avec le nouveau code PIN
print("Solde actuel:", account.get_balance("5678"))  # Output: Solde actuel: 50
