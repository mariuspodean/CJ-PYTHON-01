from shopping_list import *

# global archived_list
# archived_list = []

mac_and_cheese = Recipe('Mac and cheese', {'macaroni': 3, 'egg': 3, 'milk': 0.5, 'cheese': 1, 'sugar': 3})

mac_and_cheese.display()
cheesecake = Recipe('Cheesecake', {'flour': 1, 'milk': 1, 'egg': 3, 'cocoa': 1, 'sugar': 1, 'strawberry': 2})
cheesecake.display()
banana_bread = Recipe('Banana bread', {'flour': 1, 'yogourt': 1, 'banana': 2, 'honey': 1, 'cocoa': 1, 'sugar': 1})
banana_bread.display()
fries = Recipe('Fries', {'potato': 1, 'oil': 1, 'salt': 1, 'cheese': 1})
fries.display()
home_made_chocolate = Recipe('Home made chocolate', {'milk': 2, 'cocoa': 1, 'sugar': 2, 'vanilla': 1, 'nut': 1})
print(mac_and_cheese)
print(fries)

recipesbox = RecipesBox(fries, cheesecake, banana_bread, home_made_chocolate, mac_and_cheese)
recipesbox.add_recipe(fries)
recipesbox.add_recipe(fries)
recipesbox.add_recipe(home_made_chocolate)

recipesbox.delete_recipe(home_made_chocolate)
print(recipesbox.pick())

print(recipesbox.pick('Fries'))

for i in range(len(recipesbox.recipes)):
    print(recipesbox.recipes[i].name)

recipesbox.add_recipe(recipesbox.pick())
recipesbox.delete_recipe(recipesbox.pick())
recipesbox.add_recipe(recipesbox.pick('Cheesecake'))
recipesbox.add_recipe(recipesbox.pick())

fridge = Fridge({'milk': 4, 'potato': 3, 'egg': 2, 'banana': 10, 'sugar': 3, 'macaroni': 2, 'cocoa': 2})
print(fridge)

if 'milk' in fridge:
    print('yap')

fridge.check_ingredient('milk')
ingredients_in_the_fridge = fridge.ingredients
ingredients_in_the_fridge['butter'] = 3
print(fridge)
fridge.remove_ingredient('milk', 4)
fridge.remove_ingredient('milk', 4)

# recipes_box= recipesbox.recipe
# for recipe in recipes_box:
#     print('Recipesbox contains: ', recipe.name)
fridge.check_recipe(fries)

fridge.check_recipe(banana_bread)

fridge.check_recipe(cheesecake)

fridge.check_recipe(mac_and_cheese)

print(recipesbox)
print('************************')
check_the_fridge(fridge, recipesbox)
print('************************')

prepare_shopping_list(fridge, fries)
print(archived_list)  # archive  shopping list decorator

print('************************')
prepare_shopping_list(fridge, cheesecake)
print(archived_list)

# to test that we always get the same list
fridge = Fridge({'milk': 4, 'potato': 3, 'egg': 2, 'banana': 10, 'sugar': 3, 'macaroni': 2, 'cocoa': 2})
recipesbox = RecipesBox(fries, cheesecake, banana_bread, home_made_chocolate, mac_and_cheese)

print('************************')
prepare_shopping_list_for_recipebox(fridge, recipesbox)
print(archived_list)
