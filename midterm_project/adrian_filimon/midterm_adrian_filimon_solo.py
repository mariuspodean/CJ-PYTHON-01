
class Recipe:
    def __init__(self, name, ingredients):
        self._name = name
        self._ingredients = ingredients

    @property
    def name(self):
        return self._name

    @property
    def ingredients(self):
        return self._ingredients

    def keys(self):
        return self._ingredients.keys()


class RecipesBox:
    def __init__(self):
        self.recipes = []

    def __getitem__(self, index):
        return self.recipes[index]

    def __len__(self):
        return len(self.recipes)

    def add(self, recipe):
        self.recipes.append(recipe)

    def delete(self, name=None):
        if name:
            self.recipes.remove(name)
        else:
            print('What do you want to remove?')

    def list_recipes(self):
        for recipe in self.recipes:
            print(recipe.name, "\n")


class Fridge:
    def __init__(self):
        self.items = {}

    def add(self, item_name, item_quantity):
        self.items[item_name] = item_quantity

    def remove(self, item_name):
        del self.items[item_name]

    def search(self, ingredient):
        if self.items.get(ingredient):
            return True
        else:
            return False



cheesee_burger_ingredients = {
    'bun': 1,
    'beef_porc': 1,
    'cedar cheese': 0.5,
    'onion': 2,
    'salad': 1,
    'sauce': 2
}

submarine_sandwich_ingredients = {
    'long_roll': 1,
    'pork_veal_mince_meatballs': 3,
    'parmesan': 0.25,
    'tomato_passata': 0.5,
    'garlic_cloves': 2,
    'egg': 1
}

cheese_burger = Recipe('Beef Burger', cheesee_burger_ingredients)
submarine_sandwich = Recipe('Submarine Sandwich', submarine_sandwich_ingredients)

recipes_box = RecipesBox()
recipes_box.add(cheese_burger)
recipes_box.add(submarine_sandwich)

fridge = Fridge()
fridge.add('garlic', 1)
print(fridge.search('garlic'))


