from random import randrange

class PrettyPrinterMixin:

    def __str__(self, dict_in):
        # geting the value of the longest ingredient name
        keys_list = list(dict_in.keys())
        max1 = len(max(keys_list, key=len)) + 8

        return (f'{"*" * (max1 + 6)}\n'), max1


class Recipe(PrettyPrinterMixin):

    def __init__(self, recipe_name=None, recipe_ingredients=None):
        self.recipe_name = recipe_name
        self.recipe_ingredients = recipe_ingredients
        self._recipe = {self.recipe_name: self.recipe_ingredients}

    def __repr__(self):
        print_string = f'{self.recipe_name}: {self.recipe_ingredients}'
        return  print_string

    def __str__(self):
        header, max1 = PrettyPrinterMixin.__str__(self, self.recipe_ingredients)
        ingredients_dict = self._recipe[self.recipe_name].items()
        # heder , title of recipe
        print_string = ''.join(
            (
                '\n',
                header,
                '*',
                self.recipe_name.center(max1 + 4),
                '*\n',
                header,
                '*',
                ' ' * (max1 + 4),
                '*',
                '\n'
            )
        )
        # content of recipe
        for counter, ingred_quant in enumerate(ingredients_dict, 1):
            ingred_quant_print = f'{ingred_quant[0].title()} : {ingred_quant[1]}'

            print_string = ''.join(
                (
                    print_string,
                    f'* {counter}. {ingred_quant_print.ljust(max1)}*\n'
                )
            )
        # text format and footer
        print_string = f'\033[90m\x1B[3m{print_string}*{" " * (max1 + 4)}*\n{header}\033[0m'

        return print_string

    def __len__(self):
        return len(self._recipe)

    def __iter__(self):
        iter(self._recipe)

    def __getitem__(self, item):
        return self._recipe[item]

    def __contains__(self, item):
        pass

    def keys(self):
        return self._recipe.keys()

    def values(self):
        return self._recipe.values()

    def items (self):
        return self._recipe.items()

   # def __get__(self, instance, owner):


class RecipesBox:

    def __init__(self):
        self._recipebox_list = []

    def __str__(self):

        print_string = ''
        for recipe in self._recipebox_list:
            recipe_print = f'{recipe.recipe_name}\n'
            print_string = ''.join((print_string, recipe_print))

        # for key in self._recipebox_dict:
        #     keys = list(self._recipebox_dict[key].keys())
        #     values_print = ''
        #     for key2 in keys:
        #         values_line = f'{" " * (len(key) + 5) + key2} : {self._recipebox_dict[key][key2]}\n'
        #         values_print = ''.join((values_print, values_line))
        #     print_line = f'{key} - \n{values_print}\n'
        #     print_string = ''.join((print_string, print_line))
        return  print_string


    # def update(self, *args, **kwargs):    #     self._recipebox_dict.update(*args, **kwargs)

    def __len__(self):
        return len(self._recipebox_list)

    # def __iter__(self):
    #     self.counter = 0
    #     return self
    #
    # def __next__(self):
    #     if self.counter <= len(self._recipebox_list):
    #         next_step = self._recipebox_list[self.counter-1]
    #         self.counter += 1
    #         return next_step
    #     else:
    #         raise StopIteration

    def __getitem__(self, index):
        return self._recipebox_list[index]

    def __contains__(self, item):
        return item in self._recipebox_list

    def __setitem__(self, index, value):
        self._recipebox_list[index] = value

    def __delitem__(self, index):
        del self._recipebox_list[index]

    def remove(self, item):
        self._recipebox_list.remove(item)

    def append(self, item):
        self._recipebox_list.append(item)

    def pop(self, index=None):
        if index:
            return self._recipebox_list.pop(index)
        else:
            return self._recipebox_list.pop()

    def pick(self, name=None):
        if name:
            index = self._recipebox_list.index(name)
        else:
            max_rand_no = len(self._recipebox_list)
            index = randrange(0, max_rand_no, 1)
            print(index)

        return self._recipebox_list.pop(index)



class Fridge(PrettyPrinterMixin):

    def __init__(self):
        self._fridge = {}

    def __str__(self):
        header, max1 = PrettyPrinterMixin.__str__(self, self._fridge)
        ingredients_dict = self._fridge.items()
        # heder , title of recipe
        print_string = ''.join(
            (
                '\n',
                header,
                '*',
                self.__class__.__name__.center(max1 + 4),
                '*\n',
                header,
                '*',
                ' ' * (max1 + 4),
                '*',
                '\n'
            )
        )
        # content of recipe
        for counter, ingred_quant in enumerate(ingredients_dict, 1):
            ingred_quant_print = f'{ingred_quant[0].title()} : {ingred_quant[1]}'

            print_string = ''.join(
                (
                    print_string,
                    f'* {counter}. {ingred_quant_print.ljust(max1)}*\n'
                )
            )
        # text format and footer
        print_string = f'\033[90m\x1B[3m{print_string}*{" " * (max1 + 4)}*\n{header}\033[0m'

        return print_string

    def __getitem__(self, item):
        return self._fridge[item]

    def __iter__(self):
        iter(self._fridge)

    def __len__(self):
        return len(self._fridge)

    def __contains__(self, item):
        return item in self._fridge

    def keys(self):
        return self._fridge.keys()

    def values(self):
        return self._fridge.values()

    def items (self):
        return self._fridge.items()

    def __get__(self, instance, owner):
        pass

    def __delitem__(self, key):
        del self._fridge[key]

    def update(self, *args, **kwargs):
        self._fridge.update(*args, **kwargs)

    def update_quantity(self, ingredient, quantity):
        updated_quantity = self._fridge[ingredient] + quantity
        if updated_quantity > 0:
            self._fridge[ingredient] = updated_quantity
        else:
            print(f'There is no more \033[31m\033[01m{ingredient}\033[0m in the fridge, go shopping !!!\n')
            del self._fridge[ingredient]

    def check_recipe(self, recipe):

        recipe_ingredients = list(recipe.recipe_ingredients)
        fridge_ingredients = list(self._fridge.keys())

        ingredients_in = []
        ingredients_off = []

        for ingredient in recipe_ingredients:

            if ingredient in fridge_ingredients:
                ingredients_in.append(ingredient)
            else:
                ingredients_off.append(ingredient)

        message = f'There are no missing ingredients for preparing the {recipe.recipe_name}'

        return ingredients_in, ingredients_off if ingredients_off else message


def check_the_fridge(fridge, recipes_box):

    viable_recipes_list = RecipesBox()
    ingredients_fridge_list = list(fridge.keys())

    for recipe in recipes_box:

        recipe_ingredients = recipe[recipe.recipe_name]
        ingredients_recipe_list = list(recipe_ingredients.keys())
        ingredients_recipe_no = len(ingredients_recipe_list)

        ingredients_recipe_in, _ = fridge.check_recipe(recipe)
        ingredients_in_no = len(ingredients_recipe_in)

        if ingredients_in_no >= ingredients_recipe_no / 2:
            viable_recipes_list.append(recipe)

    return viable_recipes_list

def prepare_shopping_list(fridge, recipe):

    shopping_list = Fridge()
    recipe_ingred_dict = recipe[recipe.recipe_name]

    print('fridge:', fridge)
    print('recipe:', recipe_ingred_dict)

    for ingredient, quantity in recipe_ingred_dict.items():

        if ingredient in fridge and quantity > fridge[ingredient]:

            missing_quantity = quantity - fridge[ingredient]
            shopping_list.update({ingredient: missing_quantity})

        elif ingredient not in fridge:

            shopping_list.update({ingredient: quantity})

    return shopping_list if shopping_list else f'For {recipe.recipe_name} there are all the ingredients'





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

ribs_and_potato_ingredients = {
    'ribs': 2,
    'potato': 1,
    'chilli_sauce': 0.5,
    'garlic_sauce': 0.5,
    'pickles': 1
}

print('\n\033[34m RECIPES \033[0m\n')

burger = Recipe("Beef Burger", burger_ingredients)
print(burger)
#print(burger.__repr__())

hot_dog = Recipe('Hot Dog', hot_dog_ingredients)
print(hot_dog)
#print(hot_dog.__repr__())

ribs_and_poato = Recipe('Ribs and Potato', ribs_and_potato_ingredients)
print(ribs_and_poato)
#print(ribs_and_poato.__repr__())

print('\n\033[34m RECIPES BOX \033[0m\n')

recipes_box = RecipesBox()
recipes_box.append(burger)
recipes_box.append(hot_dog)
recipes_box.append(ribs_and_poato)
print(recipes_box)


print('\n\033[34m FRIDGE \033[0m\n')


fridge = Fridge()
fridge.update([['mustard', 10]])
fridge.update([['ketchup', 10]])
fridge.update({'bun': 100})
fridge.update({'sausage': 100})
fridge.update({'onion': 100})
fridge.update({'salad': 100})
fridge.update({'potato': 50})
fridge.update({'garlic_sauce': 35})
fridge.update({'ribs': 1})

print(fridge)

print('\n\033[34m IS ... IN THE FRIDGE ? \033[0m\n')

ingredient_test_list = ['mustard', 'onion', 'ground beef']
for ingredient in ingredient_test_list:
    print(f'Is {ingredient} in the fridge?')
    if ingredient in fridge:
        print('yap')
    else:
        print('nope')

print('\n\033[34m UPDATE INGREDIENTS IN FRIGE \033[0m\n')

print('Fridge intial: ', fridge)

fridge.update_quantity('bun', 15)
fridge.update_quantity('potato', 100)
print('+ 15 buns and + 100 potato : ', fridge)

print('- 150 buns: ')
fridge.update_quantity('bun', -150)
print(fridge)

print('\n\033[34m CHECK RECIPE \033[0m\n')

fridge.update({'bun': 100})
for recipe in recipes_box:
    #print(recipe)
    print('\ncheck_recipe for ', recipe.recipe_name)
    print(recipe)
    print(fridge)
    ingred_in, ingred_off = fridge.check_recipe(recipe)
    print('\nIngred present: ', ingred_in)
    print('Ingred missing: ', ingred_off)


# print('***')
# print(recipe_box)
# # for x in recipe_box:
# #     print(x)
# print(burger)
# print(hot_dog)
# print(fridge)
# print(check_the_fridge(fridge, recipe_box))
# print("www")
# print('Sh.L:', prepare_shopping_list(fridge, burger))
#
#
# # print(len(hot_dog))
# # print('aaa', recipe_box)
# #
# # #recipe_box.remove(hot_dog)
# # a = recipe_box.pick()
# # print(a)
# # print(type(a))
# # print('aaa', recipe_box)
#
#
#
# # ingredients = list(burger.keys())
# #
# # if 'milk' in fridge:
# #     print('yap')
# #
#
#

