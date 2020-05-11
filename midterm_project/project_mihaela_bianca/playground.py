from midterm_project.project_mihaela_bianca.shopping_list import Recipe
from midterm_project.project_mihaela_bianca.shopping_list import RecipesBox
from midterm_project.project_mihaela_bianca.shopping_list import Fridge


mac_and_cheese = Recipe('Mac and cheese', {'macaroni': 3, 'egg': 3, 'milk': 0.5, 'cheese': 1})
mac_and_cheese.display()
cheesecake = Recipe('Cheesecake', {'flour': 1, 'milk': 1, 'egg': 3, 'cocao': 1, 'sugar': 1, 'strawberry': 2})
cheesecake.display()
banana_bread = Recipe('Banana bread', {'flour': 1, 'yogourt': 1, 'banana': 2, 'honey': 1})
banana_bread.display()
fries = Recipe('Fries', {'potato': 1, 'oil': 1, 'salt': 1, 'cheese': 1})
fries.display()
home_made_chocolate = Recipe('Home made chocolate', {'milk': 2, 'cocao': 1, 'sugar': 2, 'vanilla': 1, 'nut': 1})
print(mac_and_cheese)
print(fries)

recipesbox = RecipesBox([fries, cheesecake, banana_bread, home_made_chocolate])
recipesbox.add_recipe(fries)
recipesbox.add_recipe(fries)
recipesbox.add_recipe(home_made_chocolate)
recipesbox.delete_recipe(home_made_chocolate)
#recipesbox.pick()
for i in range(len(recipesbox.recipe)):
    print(recipesbox.recipe[i])
#print(recipesbox.delete_recipe(recipesbox.pick()))
#recipesbox.add_recipe(recipesbox.pick())

fridge = Fridge({'milk': 4, 'potato': 3, 'egg': 2, 'banana': 10, 'sugar': 3, 'macaroni':2, 'cocoa':2})
print(fridge)
ingredients_in_the_fridge = fridge.ingredients
ingredients_in_the_fridge['butter'] = 3
print(fridge)

#fridge.check_recipe(recipesbox.pick())


