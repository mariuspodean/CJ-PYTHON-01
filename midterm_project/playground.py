from shopping_list_archive import *

mac_and_cheese = Recipe("Famous Mac and cheese", mac_and_cheese_ingredients)
mac_test = Recipe("test", mac_and_cheese_ingredients)
print(mac_and_cheese)

ingredients = list(mac_and_cheese_ingredients.keys())
print(ingredients)

i = RecipeBox.pick("asd")
print(i)

# A new recipe can be created starting from a
# name and dictionary of ingredients and quantities.

a = Recipe('test', {'unt': 1, 'marmelada': 23, 'oua': 3, 'cafea': 4})
if "milk" in fridge:
    print('yap')