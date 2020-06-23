from shopping_list import Recipe, RecipeBox, Fridge
from shopping_list import check_the_fridge, prepare_shopping_list, shopping_list_archive

# Recipe
print("\n CREATE NEW RECIPES: \n")

spaghetti_amatriciana = Recipe(
    "Spaghetti all'Amatriciana",
    {
        'Spaghetti': 1,
        'Salt': 1,
        'Pancetta': 2,
        'Tomato sauce': 1,
        'garlic': 1
    }
)

print(spaghetti_amatriciana)

spaghetti_amatriciana_ingredients = list(spaghetti_amatriciana.keys())

montana_cake = Recipe(
    "Montana Cake",
    {
        'eggs': 5,
        'flour': 15,
        'sugar': 15,
        'yeast': 10,
        'oil': 15
    }
)
print(montana_cake)
montana_cake_ingredients = list(montana_cake.keys())

omelette = Recipe(
    "Omelette",
    {
        'eggs': 2,
        'ham': 5,
        'cheese': 5,
        'vegetables': 5
    }
)
print(omelette)
omelette_ingredients = list(omelette.keys())

apple_pie = Recipe(
    "Apple Pie",
    {
        'apples': 6,
        'flour': 3,
        'eggs': 4,
        'sugar': 20,
        'yogurt': 9,
        'butter': 10,
        'yeast': 16
    }
)
print(apple_pie)
apple_pie_ingredients = list(apple_pie.keys())

tiramisu = Recipe(
    "Tiramisù",
    {
        'Eggs': 4,
        'sugar': 20,
        'mascarpone': 5,
        'coffee': 1,
        'savoiardi': 40
    }
)
print(tiramisu)
tiramisu_ingredients = list(tiramisu.keys())

# RecipeBox


recipes = RecipeBox()

recipes.append(montana_cake)
recipes.append(spaghetti_amatriciana)
recipes.append(omelette)
recipes.append(apple_pie)
recipes.append(tiramisu)

print("\n PRINT RECIPE BOX: \n")
print(recipes)

recipes.delete(tiramisu)
print("\n REMOVE ONE RECIPE FROM RECIPE BOX: \n")
print(recipes)

recipe_by_name = recipes.pick(name="Omelette")
print("\n EXTRACT RECIPE BY NAME FROM RECIPE BOX: \n")
print(recipe_by_name)

random_recipe = recipes.pick()
print("\n EXTRACT RANDOM RECIPE FROM RECIPE BOX: \n")
print(random_recipe)

recipes.append(tiramisu)
print("\n ADD RECIPE TO RECIPE BOX: \n")
print(recipes)

fridge = Fridge()

fridge.append('eggs', 11)
fridge.append('sugar', 300)
fridge.append('pasta', 300)
fridge.append('cheese', 50)
fridge.append('vegetables', 50)
fridge.append('apples', 0)
fridge.append('coffee', 1)
fridge.append('savoiardi', 1)

print("\n CREATE A NEW FRIDGE: \n")
print(fridge)

print("\n CHECK IF AN ITEM IS IN THE FRIDGE: \n")
if 'eggs' in fridge:
    print('yap')
if 'milk' in fridge:
    print('yap')
else:
    print('nope')

print("\n DELETE AN ITEM FROM THE FRIDGE: \n")
del fridge['apples']
print(fridge)

print("\n UPDATE QUANTITY OF A PRODUCT IN FRIDGE: \n")
fridge['vegetables'] = 10
print(fridge)

print("\n UPDATE A PRODUCT WITH QUANTITY 0: \n")
fridge['pasta'] = 0
print(fridge)

in_fridge, not_in_fridge = fridge.check_recipe(apple_pie)
print('Available ingredients: {0}'.format(in_fridge))
print('Not available ingredients: {0}'.format(not_in_fridge))

print("\n CHECK IF RECIPES' INGREDIENTS IN THE FRIDGE: \n")
in_fridge_recipes = check_the_fridge(fridge, recipes)
print('Fridge has ingredients for recipes: {0}'.format(in_fridge_recipes))

print("\n PREPARE SHOPPING LIST:\n")
shopping_list = prepare_shopping_list(fridge, apple_pie)
print('\nShopping list: {0}'.format(shopping_list_archive))
