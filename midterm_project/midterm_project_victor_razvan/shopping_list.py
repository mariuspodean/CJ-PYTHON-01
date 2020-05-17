from random import randrange
from collections.abc import Mapping, MutableSequence, MutableMapping

# establish width of print
width = 30

class PrettyPrinter:
    def __init__(self, recipe_name, recipe_ingredients):
        self.recipe_name = recipe_name
        self.recipe_ingredients = recipe_ingredients

    def __str__(self):  # to print header of recipe
        global width
        # center recipe name into box
        if len(self.recipe_name) % 2 == 0:
            x0 = int((width - 2 - len(self.recipe_name)) / 2)
        else:
            x0 = int((width - 2 - len(self.recipe_name) + 1) / 2)
        # width = 30  # width on list
        # space_right = width - len(self.recipe_name) - 1
        x1 = ' +' + '-' * 28 + ' +'  # upper header line 1
        x2 = '|' + ' ' * 28 + ' |'  # upper header line 2
        x3 = '|' + (' ' * x0) + self.recipe_name + (' ' * x0) + '|'
        x4 = x2  # bottom header line 1
        x5 = '+' + '-' * 28 + ' +'  # bottom header line 2

        return '{} \n {} \n {} \n {} \n {}'.format(x1, x2, x3, x4, x5)

    def printing_header(self):
        x0 = int((30 - 16) / 2)
        x1 = ' +' + '-' * 28 + ' +'  # upper header line 1
        x2 = '|' + ' ' * 28 + ' |'  # upper header line 2
        x3 = '|' + (' ' * x0) + 'Fridge contain' + (' ' * x0) + ' |'
        x4 = x2  # bottom header line 1
        x5 = '+' + '-' * 28 + ' +'  # bottom header line 2

        return '{} \n {} \n {} \n {} \n {}'.format(x1, x2, x3, x4, x5)


class Recipe(PrettyPrinter):

    def __init__(self, recipe_name, recipe_ingredients):
        super().__init__(recipe_name, recipe_ingredients)
        self.recipe_name = recipe_name
        self.recipe_ingredients = recipe_ingredients
        self.recipe = {self.recipe_name: self.recipe_ingredients}
        no_of_ingredients = len(self.recipe_ingredients)
        if no_of_ingredients < 4:
            print('There should be at least 4 ingredients')

    def __iter__(self):
        return self.recipe

    def __getitem__(self, item):
        return self.recipe[item]

    def __len__(self):
        return len(self.recipe)

    def keys(self):
        return self.recipe.keys()

    def values(self):
        return self.recipe.values()

    def items(self):
        return self.recipe.items()

    def __str__(self):
        global width
        x0 = PrettyPrinter.__str__(self)
        x1 = '+' + '-' * 28 + '+'  # bottom line
        print_recipe = x0
        for index, recipe_ingred in enumerate(self.recipe_ingredients, start=1):
            y = ' ' * (width - 9 - len(recipe_ingred) - len(str(self.recipe_ingredients[recipe_ingred])))
            print_recipe += f'\n | {index}.  {recipe_ingred} :{self.recipe_ingredients[recipe_ingred]} ' \
                            f'{y}|\n '
        print_recipe += '\n {}'.format(x1)
        return print_recipe


class RecipeBox:

    def __init__(self, *args):
        self.recipe_box = [*args]

    def __iter__(self):
        return iter(self.recipe_box)

    def __getitem__(self, recipe):
        return self.recipe_box[recipe]

    def __delitem__(self, recipe):
        del self.recipe_box[recipe]

    def __setitem__(self, key, value):
        self.recipe_box[key] = value

    def __len__(self):
        return len(self.recipe_box)

    def add_recipe(self, name):
        self.recipe_box.append(name)
        return self.recipe_box

    def delete_recipe(self, name):
        if len(self.recipe_box) >= 1:
            self.recipe_box.remove(name)
        else:
            raise Exception('You cannot delete last recipe from the RecipeBox!')

    def pick(self, recipe):
        return Recipe(recipe.recipe_name, recipe.recipe_ingredients)

    def __str__(self):
        recipe_box = []
        for recipe in self.recipe_box:
            recipe_box.append(recipe.recipe_name)
        return str(recipe_box)


class Fridge(PrettyPrinter):

    def __init__(self, ingredients):
        self.fridge_ingredients = ingredients
        no_of_ingredients = len(self.fridge_ingredients)
        if no_of_ingredients < 5:
            print('Fridge should contain also (some) food not only beer !!')

    def __getitem__(self, item):
        return self.recipe[item]

    def __setitem__(self, key, value):
        self.recipe[key] = value

    def __delitem__(self, key):
        del self.recipe_ingredients[key]

    def __iter__(self):
        return self.recipe

    def __len__(self):
        return len(self.recipe)

    def __str__(self):
        global width
        x0 = PrettyPrinter.printing_header(self)
        x1 = '+' + '-' * 28 + '+'  # bottom line
        print_fridge = x0
        for index, fridge_ingred in enumerate(self.fridge_ingredients, start=1):
            y = ' ' * (width - 9 - len(fridge_ingred) - len(str(self.fridge_ingredients[fridge_ingred])))
            print_fridge += f'\n | {index}.  {fridge_ingred} :{self.fridge_ingredients[fridge_ingred]} ' \
                            f'{y}|\n '
        print_fridge += '\n {}'.format(x1)
        return print_fridge

    def dict_keys(self):
        return self.fridge_ingredients.keys()

    def dict_values(self):
        return self.fridge_ingredients.values()

    def dict_items(self):
        return self.fridge_ingredients.items()

    def check_ingredient(self, ingredient):
        # print(self.fridge_ingredients)
        if ingredient in self.fridge_ingredients.keys():
            return f'We have it'
        else:
            return 'We do not have it, but that is OK: we have beer !'

    def add_ingredient(self, ingredient):
        self.fridge_ingredients.update(ingredient)
        return self.fridge_ingredients

    def remove_ingredient(self, ingredient, qty):
        if ingredient in self.fridge.keys():
            self.fridge[ingredient] -= qty
            if self.fridge[ingredient] == 0:
                del self.fridge[ingredient]
                return f'{ingredient} ingredient is removed from fridge'
        else:
            return f'{ingredient} is not in the fridge'

    def check_recipe(self, recipe_ingredients):
        # build two list to compare
        what_we_have = list(self.fridge_ingredients.keys())
        # from tuple(str, dict) to list(dict)
        temp_list = list(recipe_ingredients.values())
        recipe_name_imp = list(recipe_ingredients.keys())
        # from list(dict) to list(item1, item2, item3..)
        what_we_should_have = list(temp_list[0].keys())
        comparison = set(what_we_have).intersection(what_we_should_have)  # what we have in the fridge for recipe
        comparison2 = set(what_we_should_have).difference(what_we_have)  # what we still need for recipe

        return f'In the fridge we have {what_we_have} \nFor the "{recipe_name_imp}" we need: {what_we_should_have} ' \
               f'\nFrom the "{recipe_name_imp}" recipe we have: {comparison} \nWe still need {comparison2} ' \
               f'for the recipe'
