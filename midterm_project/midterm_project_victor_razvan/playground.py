from shopping import *


mac_and_cheese_ingredients = {
    'macaroni': 1,
    'soft cheese': 0.5,
    'cheddar': 0.5,
    'salt': 0.1,
}

mac_and_cheese = Recipe(
    "Famous Mac & Cheese",
    mac_and_cheese_ingredients
)

print(mac_and_cheese)

ingredients = list(mac_and_cheese.keys())
print(ingredients)
print(list(mac_and_cheese.values()))
print(list(mac_and_cheese.items))
print(('salt' in mac_and_cheese))
print(len(mac_and_cheese))

mac = Recipe(
    "Not so Famous Mac & Cheese",
    {
        'bun': 1,
        'meat': 1,
        'mustard': 0.1,
        'mayo': 0.2,
        'cheddar': 0.3,
    }
)

print((mac_and_cheese == mac))
print((mac_and_cheese != mac))
print(mac_and_cheese['salt'])
print(mac_and_cheese.get('salt'))

retetar = RecipeBox(mac_and_cheese, mac)
retetar.append(mac)
print('the end')

un_frigider = Fridge({
    'macaroni': 0.5,
    'soft cheese': 2,
    'cheddar': 0.5,
    'yeast': 0.1,
    'mustard': 0.1,
    'mayo': 0.2,
})
print(un_frigider)

if 'milk' in un_frigider:
    print('yap - milk')
if 'salt' in un_frigider:
    print('yap - salt')

un_frigider.update({'water':11, 'onions':4})
print(un_frigider)

print('check_recipe')
print(un_frigider.check_recipe(mac_and_cheese))

print('prepare_shopping_list')
print(prepare_shopping_list(un_frigider, mac_and_cheese))

print('check_the_fridge')
print(check_the_fridge(un_frigider, retetar))
