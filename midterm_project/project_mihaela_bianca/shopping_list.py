from midterm_project.project_mihaela_bianca.playground import Recipe
from midterm_project.project_mihaela_bianca.playground import RecipesBox
from midterm_project.project_mihaela_bianca.playground import Fridge

mac_and_cheese = Recipe('Mac and cheese', {'macaroni': 3, 'egg': 3, 'milk': 0.5, 'cheese': 1})
mac_and_cheese.display()
cheesecake = Recipe('Cheesecake', {'flour': 1, 'milk': 1, 'egg': 3, 'cacao': 1, 'sugar': 1, 'strawberry': 2})
cheesecake.display()
banana_bread = Recipe('Banana bread', {'flour': 1, 'yogourt': 1, 'banana': 2, 'honey': 1})
banana_bread.display()
fries = Recipe('Fries', {'potato': 1, 'oil': 1, 'salt': 0.1, 'cheese': 0.1})
fries.display()
print(mac_and_cheese)
print(fries)

recipesbox=RecipesBox(['Fries', 'Cheesecake', 'home chocolate', 'Barbeque', 'carrotcake'])
recipesbox.add_recipe('Sweetbread')
recipesbox.delete_recipe('Fries')
recipesbox.pick()
print(recipesbox)

fridge=Fridge({'milk':4, 'potato':3, 'egg':2, 'banana':10, 'sugar':3})
print(fridge)


