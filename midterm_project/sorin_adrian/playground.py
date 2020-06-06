from midterm_project.sorin_adrian.shoppingList import Recipe, RecipesBox, Fridge, check_the_fridge, \
    prepare_shopping_list, shopping_list_archive

# create the ingredients dict for multiple recipes, containing name an quantity of an ingredient
burger_ingredients = {
    'bun': 1,
    'ground_beef': 1,
    'ceedar_cheese': 0.5,
    'onion': 2,
    'salad': 1,
    'smoked_sauce': 2
}
hot_dog_ingredients = {
            'bun': 1,
            'sausage': 1,
            'mustard': 0.5,
            'ketchup': 0.5
}
ribs_and_potato_ingredients = {
    'ribs': 2,
    'potato': 1,
    'chilli_sauce': 0.5,
    'garlic_sauce': 0.5,
    'pickles': 1
}
english_breakfast_ingredients = {
    'ham': 1,
    'egg': 2,
    'beans': 0.5,
    'cheese': 1,
    'tomatos': 1,
    'salad': 0.5
}
pizza_ingredients = {
    'dough': 1,
    'tomato_sauce': 1,
    'mozzarela': 2,
    'prosciutto': 4,
    'rucola': 0.5
}
pasta_carbonara_ingredients = {
    'pasta': 2,
    'bacon': 1,
    'sour_cream': 0.5,
    'egg': 1,
    'parmegiano': 0.5,
    'olivee_oil': 0.5
}

# create instances for each recipe by its title and dict of ingredients
print('\n\033[34m RECIPES \033[0m\n')

burger = Recipe("Beef Burger", burger_ingredients)
print(burger)
# print(burger.__repr__())

hot_dog = Recipe('Hot Dog', hot_dog_ingredients)
print(hot_dog)
# print(hot_dog.__repr__())

ribs_and_poato = Recipe('Ribs and Potato', ribs_and_potato_ingredients)
print(ribs_and_poato)
# print(ribs_and_poato.__repr__())

english_breakfast = Recipe('English Breakfast', english_breakfast_ingredients)
print(english_breakfast)
# print(english_breakfast.__repr__())

pizza = Recipe('Pizza Prociutto Crudo', pizza_ingredients)
print(pizza)
# print(pizza.__repr__())

pasta_carbonara = Recipe('Pasta carbonara', pasta_carbonara_ingredients)
print(pasta_carbonara)
# print(pasta_carbonara.__repr__())

# create the recipes_box database as a RecipesBox instance , and add recipes in
print('\n\033[34m RECIPES BOX \033[0m\n')

recipes_box = RecipesBox()
recipes_box.append(burger)
recipes_box.append(hot_dog)
recipes_box.append(ribs_and_poato)
recipes_box.append(english_breakfast)
recipes_box.append(pizza)
recipes_box.append(pasta_carbonara)
print(recipes_box)

# create the fridge, as an instance of Frige, and add ingredients in
print('\n\033[34m FRIDGE \033[0m\n')

fridge = Fridge()
fridge.update({'mustard': 10})
fridge.update({'ketchup': 10})
fridge.update({'bun': 100})
fridge.update({'sausage': 100})
fridge.update({'onion': 100})
fridge.update({'salad': 100})
fridge.update({'potato': 50})
fridge.update({'garlic_sauce': 35})
fridge.update({'ribs': 1})
fridge.update({'pasta': 10})
fridge.update({'bacon': 15})
fridge.update({'egg': 30})
print(fridge)

# test if an intredient is in the fridge
print('\n\033[34m IS ... IN THE FRIDGE ? \033[0m\n')

ingredient_test_list = ['mustard', 'onion', 'ground beef']
for ingredient in ingredient_test_list:
    print(f'Is {ingredient} in the fridge?')
    if ingredient in fridge:
        print('yap')
    else:
        print('nope')

# add and extract ingredients in/from the fridge , and test the case when the quantity is 0
print('\n\033[34m UPDATE INGREDIENTS IN FRIGE \033[0m\n')

print('Fridge intial: ', fridge)
fridge.update_quantity('bun', 15)
fridge.update_quantity('potato', 100)
print('+ 15 buns and + 100 potato : ', fridge)
print('- 100 onion: ')
fridge.update_quantity('onion', -100)
print(fridge)

# check if there are ingredients for a recipe in the fridge and
# return list with presnt ingredients and with misiing ingredients
print('\n\033[34m CHECK RECIPE \033[0m\n')

fridge.update({'bun': 100})
for recipe in recipes_box:
    print('\ncheck_recipe for ', recipe.recipe_name)
    print(recipe)
    print(fridge)
    ingred_in, ingred_off = fridge.check_recipe(recipe)
    print('\nIngredients present: ', ingred_in)
    print('Ingredients missing: ', ingred_off)

# check the fridge if has ingredients for recipes, return a list of recipes
# for wich there are at lest half of ingredients im the fridge
print('\n\033[34m CHECK THE FRIDGE \033[0m\n')

viable_recipes_box = check_the_fridge(fridge, recipes_box)
print(f'For next recipes there has at least half of ingredients in the fridge:\n')
for recipe in viable_recipes_box:
    print(f'- {recipe}')

# test pick a recipe
print('\n\033[34m PICK A RECIPE \033[0m\n')

recipe = recipes_box.pick(english_breakfast)
print(f'You pick {recipe.recipe_name} recipe =>\n{recipe}')

# test pick a random recipe
print('\n\033[34m PICK A RANDOM RECIPE 2 TIMES \033[0m\n')
for x in range(2):
    random_recipe = recipes_box.pick()
    print(f'Pick a random recipe =>\n{random_recipe}\n')

# check the fridge if contains all the necessary ingredients for a recipe,
# if not print a fancy shopping list, and add this to a archive
print('\n\033[34m PREPARE SHOPPING LIST FOR ALL RECIPES \033[0m\n')

for recipe in recipes_box:
    print(f'\nShopping List for {recipe.recipe_name}:\n')
    prepare_shopping_list(fridge, recipe)

# print the sopping lists archive
print('\n\033[34m SHOPPING LIST ARCHIVE \033[0m\n')

for shopping_list in shopping_list_archive:
    print(shopping_list)
