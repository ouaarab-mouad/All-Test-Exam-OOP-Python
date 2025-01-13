class CoffeeShop:
    def __init__(self, nom, menu):
        self.nom = nom
        self.menu = menu
        self.commandes = []

    def add_order(self, article):
        for item in self.menu:
            if item['article'] == article:
                self.commandes.append(article)
                return f"{article} ajouté à la commande !"
        return "Cet article est actuellement indisponible!"

    def fill_order(self):
        if self.commandes:
            article = self.commandes.pop(0)
            return f"Le {article} est prêt !"
        else:
            return "Toutes les commandes ont été livrées !"

    def list_orders(self):
        return self.commandes

    def due_amount(self):
        total_amount = sum(item['prix'] for item in self.menu if item['article'] in self.commandes)
        return f"Montant total dû : ${total_amount:.2f}"

    def cheap_item(self):
        cheapest_item = min(self.menu, key=lambda x: x['prix'])
        return cheapest_item['article']

    def drinks_only(self):
        return [item['article'] for item in self.menu if item['type'] == 'drink']

    def food_only(self):
        return [item['article'] for item in self.menu if item['type'] == 'food']

# Exemple d'utilisation de la classe CoffeeShop
menu_items = [
    {'article': 'Café', 'type': 'drink', 'prix': 2.50},
    {'article': 'Croissant', 'type': 'food', 'prix': 3.00},
    {'article': 'Thé', 'type': 'drink', 'prix': 2.00},
    # Ajoutez d'autres articles au menu au besoin
]

coffee_shop = CoffeeShop("Mon Coffee Shop", menu_items)

print(coffee_shop.add_order("Café"))  # Café ajouté à la commande !
print(coffee_shop.add_order("Sandwich"))  # Cet article est actuellement indisponible!
print(coffee_shop.fill_order())  # Le Café est prêt !
print(coffee_shop.list_orders())  # []
print(coffee_shop.due_amount())  # Montant total dû : $0.00
print(coffee_shop.cheap_item())  # Thé
print(coffee_shop.drinks_only())  # ['Café', 'Thé']
print(coffee_shop.food_only())  # ['Croissant']
