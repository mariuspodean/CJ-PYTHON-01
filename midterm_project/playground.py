from midterm_project.shopping_list_archive import *

mac_and_cheese_ingredients = {
    'macaroni': 1,
    'cheese': 0.5,
    'butter': 1,
    'milk': 1
}

pizza_ingredients = {
    'flour': 1,
    'water': 1,
    'yeast': 0.5,
    'cheese': 2,
    'pepperoni': 1,
    'sauce': 2
}

burger_ingredients = {
    'bun': 1,
    'beef': 1,
    'mustard': 0.5,
    'ketchup': 0.5,
    "onion": 1
}


mac_and_cheese = Recipe("Famous Mac and Cheese", mac_and_cheese_ingredients)
burger = Recipe("Burger Lalala", burger_ingredients)
pizza = Recipe("Pizza", pizza_ingredients)

r = RecipeBox()
print(r.add(burger))
print(r.add(mac_and_cheese))
print(r.add(pizza))

f = Fridge()
