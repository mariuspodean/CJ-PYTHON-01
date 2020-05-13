

class Recipe:

    def __init__(self, recipe_name=None, recipe_ingredients=None):
        self._recipe = {recipe_name: recipe_ingredients}

    def __str__(self):
        key = list(self._recipe.keys())[0]
        print_string = (f'{key}: {self._recipe[key]}')
        return  print_string

    def __len__(self):
        return len(self._recipe)

    def __iter__(self):
        iter(self._recipe)

    def __getitem__(self, item):
        return self._recipe[item]


    def __setitem__(self, key, value):
        raise

    def __delitem__(self, key):
        raise


    def keys(self):
        return self._recipe.keys()

    def values(self):
        return self._recipe.values()


class RecipesBox:

    def __init__(self):
        self._recipebox_dict = {}

    def __str__(self):
        print_string = ''
        for key in self._recipebox_dict:
            keys = list(self._recipebox_dict[key].keys())
            values_print = ''
            for key2 in keys:
                values_line = f'{" " * (len(key) + 5) + key2} : {self._recipebox_dict[key][key2]}\n'
                values_print = ''.join((values_print, values_line))
            print_line = f'{key} - \n{values_print}\n'
            print_string = ''.join((print_string, print_line))
        return  print_string


    def update(self, *args, **kwargs):
        self._recipebox_dict.update(*args, **kwargs)

    def pick(self, name=None):
        pass


class Fridge:

    def __init__(self):
        self._fridge = {}

    def __str__(self):
        print_string = ''
        for key in self._fridge:
            print_line = f'{key} - {self._fridge[key]}\n'
            print_string = ''.join((print_string, print_line))
        return print_string

    def update(self, *args, **kwargs):
        self._fridge.update(*args, **kwargs)

    def check_recipe(self, recipe):
        pass

class PrittyPrinter:
    pass


def check_the_fridge(fridge, recipes_box):
    pass


def prepare_shopping_list(fridge, recipe):
    pass


burger_ingredients = {
    'bun': 1,
    'ground beef': 1,
    'ceedar cheese': 0.5,
    'onion' : 2,
    'salad': 1,
    'sauce': 2
}

hot_dog_ingredients = {
    'bun': 1,
    'sausage': 1,
    'mustard': 0.5,
    'ketchup': 0.5
}



burger = Recipe("Beef Burger", burger_ingredients)

print(burger)
print(list(burger.keys())[0])
print(burger.values())
print(burger['Beef Burger'])

print()
hot_dog = Recipe('Hot Dog', hot_dog_ingredients)

print(hot_dog)
print(list(hot_dog.keys())[0])
print(hot_dog.values())
print(hot_dog['Hot Dog'])

recipe_box = RecipesBox()
recipe_box.update(burger)
recipe_box.update(hot_dog)

print(recipe_box)

fridge = Fridge()
fridge.update([['mustar', 10]])
fridge.update([['ketchup', 10]])
fridge.update({'buns': 100})

print(fridge)


# ingredients = list(burger.keys())
#
# if 'milk' in fridge:
#     print('yap')
#



