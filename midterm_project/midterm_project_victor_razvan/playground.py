from shopping_list import *  # thanks to Mihaela for the recipes

mac_and_cheese = Recipe('Famous Mac and cheese', {'macaroni': 3, 'egg': 3, 'milk': 0.5, 'cheese': 1, 'sugar': 3})
print(mac_and_cheese)
cheesecake = Recipe('Cheesecake', {'flour': 1, 'milk': 1, 'egg': 3, 'cocoa': 1, 'sugar': 1, 'strawberry': 2})
banana_bread = Recipe('Banana bread', {'flour': 1, 'yogurt': 1, 'banana': 2, 'honey': 1, 'cocoa': 1, 'sugar': 1})
fries = Recipe('Fries', {'potato': 1, 'oil': 1, 'salt': 1, 'cheese': 1})
# print(fries)
# print(fries.values())
home_made_chocolate = Recipe('Home made chocolate', {'milk': 2, 'cocoa': 1, 'sugar': 2, 'vanilla': 1, 'nut': 1})
# print(mac_and_cheese)
# print(fries)

recipesbox = RecipeBox(cheesecake, banana_bread, home_made_chocolate, mac_and_cheese)
print(recipesbox)
recipesbox.add_recipe(fries)
print(recipesbox)
recipesbox.delete_recipe(cheesecake)
print(recipesbox)
#
print(recipesbox.pick(fries))

recipesbox.add_recipe(recipesbox.pick(cheesecake))
print(recipesbox)

fridge = Fridge({'milk': 4, 'potato': 3, 'egg': 2, 'banana': 10, 'sugar': 3, 'macaroni': 2, 'cocoa': 2})
print(fridge)
print(fridge.check_ingredient('milk'))

print(fridge.check_recipe(fries))


fridge = Fridge({'milk': 4, 'potato': 3, 'egg': 2, 'banana': 10, 'sugar': 3, 'macaroni': 2, 'cocoa': 2})

