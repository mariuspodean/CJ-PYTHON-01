from midterm_project.midterm_project_marius_alex.shopping_list import Recipe, RecipeBox, Fridge, check_fridge, \
    prepare_shopping_list, shopping_archive

mac_and_cheese_ingredients = {'macaroni': 1, 'cheese': 0.5, 'sour cream': 0.25, 'ham': 0.5}
pizza_ingredients = {'pizza doe': 1, 'cheese': 0.5, 'peperoni': 0.5, 'tomato': 0.5}
salsa_chicken_ingredients = {'chicken': 1, 'seasoning mix': 0.1, 'salsa': 0.1, 'cheese': 1, 'sour cream': 0.5}
fruit_salad_ingredients = {'apple': 1, 'banana': 1, "grapes": 1, 'melon': 1}
garlic_chicken_ingredients = {'chicken': 1, 'butter': 0.5, 'garlic': 0.1, 'salt': 0.3, 'onion': 0.1}

fridge_content = {'macaroni': 1, 'cheese': 3, 'sour cream': 2, 'ham': 4, 'tomato': 6, 'milk': 1}

# showcasing Recipe class and implicitly the mixin class
mac_and_cheese = Recipe("Famous Mac & Cheese", mac_and_cheese_ingredients)
pizza = Recipe("Pizza", pizza_ingredients)
fruit_salad = Recipe("Fruit Salad", fruit_salad_ingredients)
garlic_chicken = Recipe("Garlic Chicken", garlic_chicken_ingredients)
salsa_chicken = Recipe("Salsa Chicken", salsa_chicken_ingredients)

print(mac_and_cheese)

ingredients = list(mac_and_cheese.keys())
print(ingredients)

# showcasing RecipeBox class
recipe_list = []
recipe_box = RecipeBox(recipe_list)
recipe_box.add_recipe(mac_and_cheese)
recipe_box.add_recipe(pizza)
recipe_box.add_recipe(fruit_salad)
recipe_box.add_recipe(garlic_chicken)
recipe_box.add_recipe(salsa_chicken)
recipe_box.del_recipe(fruit_salad)

random_recipe = recipe_box.pick()
print(f'Random recipe: \n{random_recipe}')
print(recipe_box.pick(name='Pizza'))
print(recipe_box)

# showcasing Fridge class and implicitly the mixin class
fridge = Fridge("fridge", fridge_content)
print(fridge)

fridge.add_ingredient({'mold': 3})
fridge.update_ingredient('mold', 10)
fridge.remove_ingredient('mold', 20)

fridge.check_product('milk')

fridge.check_recipe(pizza)

# showcasing check_the_fridge function

check_fridge(fridge, recipe_box)

# showcasing prepare_shopping_list function

prepare_shopping_list(fridge, salsa_chicken)
prepare_shopping_list(fridge, fruit_salad)

print(f'Shopping archive: {shopping_archive}')