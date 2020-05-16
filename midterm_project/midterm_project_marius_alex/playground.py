from shopping_list import *

# showcasing Recipe class and implicitly the mixin class

mac_and_cheese_ingredients = {'macaroni': 1, 'cheese': 0.5, 'sour cream': 0.25, 'ham': 0.5}
mac_and_cheese = Recipe("Famous Mac & Cheese", mac_and_cheese_ingredients)

print(mac_and_cheese)
q = list(mac_and_cheese.keys())
print(q)

# **********************************************************************************************************************
# showcasing RecipeBox class

pizza_ingredients = {'pizza doe': 1, 'cheese': 0.5, 'peperoni': 0.5, 'tomato': 0.5}
pizza = Recipe("Pizza", pizza_ingredients)

fruit_salad_ingredients = {'apple': 1, 'banana': 1, "grapes": 1, 'melon': 1}
fruit_salad = Recipe("Fruit Salad", fruit_salad_ingredients)

salsa_chicken_ingredients = {'chicken': 1, 'seasoning mix': 0.1, 'salsa': 0.1, 'cheese': 1, 'sour cream': 0.5}
salsa_chicken = Recipe("Salsa Chicken", salsa_chicken_ingredients)

garlic_chicken_ingredients = {'chicken': 1, 'butter': 0.5, 'garlic': 0.1, 'salt': 0.3, 'onion': 0.1}
garlic_chicken = Recipe("Garlic Chicken", garlic_chicken_ingredients)

recipes_list = [
    Recipe("Famous Mac & Cheese", mac_and_cheese_ingredients),
    Recipe("Pizza", pizza_ingredients),
    Recipe("Salsa Chicken", salsa_chicken_ingredients),
    Recipe("Garlic Chicken", garlic_chicken_ingredients),
    ]

recipe_box = RecipesBox(recipes_list)

recipe_box.add_recipe(fruit_salad)
recipe_box.delete_recipe(fruit_salad)
print(recipe_box)


# **********************************************************************************************************************
# showcasing Fridge class and implicitly the mixin class

fridge_ingredients = {'macaroni': 5, 'cheese': 6, 'sour cream': 3, 'ham': 4, 'tomato': 2}
fridge = Fridge(fridge_ingredients)
fridge.check_recipe(mac_and_cheese)
fridge.check_recipe(pizza)

print(fridge)
fridge.add_ingredient({'mold': 3})
fridge.update_ingredient('mold', 10)
fridge.remove_ingredient('mold', 20)

# **********************************************************************************************************************
# showcasing check_the_fridge function

check_the_fridge(fridge, recipe_box)
shopping_archive = []


# **********************************************************************************************************************
# showcasing prepare_shopping_list function

prepare_shopping_list(mac_and_cheese)
prepare_shopping_list(pizza)