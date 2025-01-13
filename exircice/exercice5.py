class Smoothie:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        ingredient_costs = {
            'Strawberry': 1.50,
            'Banana': 0.50,
            'Mango': 2.50,
            'Blueberry': 1.00,
            'Raspberry': 1.00,
            'Apple': 1.75,
            'Pineapple': 3.50
        }

        total_cost = sum(ingredient_costs[ingredient] for ingredient in self.ingredients)
        return total_cost

    def get_price(self):
        cost = self.get_cost()
        price = cost + cost * 1.5
        return price
 
    def __str__(self):
        sorted_ingredients = sorted(self.ingredients)
        ingredient_string = ', '.join(sorted_ingredients)

        if len(sorted_ingredients) > 1:
            return f"{ingredient_string} Fusion"
        else:
            return f"{ingredient_string} Smoothie"


# Exemple d'utilisation de la classe Smoothie
ingredients_list = ['Apple', 'Blueberry', 'Pineapple']
my_smoothie = Smoothie(ingredients_list)

print(f"Ingredients: {my_smoothie.ingredients}")
print(f"Cost: ${my_smoothie.get_cost():.2f}")
print(f"Price: ${my_smoothie.get_price():.2f}")
print(f"Representation: {my_smoothie}")
