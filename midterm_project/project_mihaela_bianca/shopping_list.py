import random
import pprint

from copy import deepcopy

archived_list = []

pp = pprint.PrettyPrinter(indent=4)

__header = r'''
   ______________________________
 / \                             \.
|   |                            |.
 \_ |                            |.
    |                            |.
'''
__footer = r'''
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/.
'''


class PrettyPrinterMixin:

    def __str__(self):
        dash = '*' * 30

        if hasattr(self, 'name'):
            header_name = '{} for {}'.format(self.__class__.__name__, self.name)
        else:
            header_name = self.__class__.__name__

        header = '{} contains:'.format(header_name)

        result = '\n\n{} \n{}\n{} \n '.format(dash, header, dash)
        for index, ingred in enumerate(self.ingredients, start=1):
            result += '\n{}. {} : {} \n '.format(index, ingred.ljust(22, ' '), self.ingredients[ingred])
        result += '\n{}'.format(dash)
        return result


class Recipe(PrettyPrinterMixin):

    def __init__(self, name, ingredients):
        """
        Ingredients should be a dictionary
        {egg:3, milk:3, flour:2, sugar:1}
        """
        self.name = name
        self.ingredients = ingredients

        if len(self.ingredients) < 4:
            raise Exception('The ingredients number should be  at least 4 !')

    def __iter__(self):
        yield from iter(self.ingredients.items())

    def __getitem__(self, index):
        return self.ingredients[index]

    def __len__(self):
        return len(self.ingredients)

    def __repr__(self):
        return self.name

    def keys(self):
        return self.ingredients.keys()

    def values(self):
        return self.ingredients.values()

    def display(self):
        print('{} = \n {} \n '.format(self.name + '_ingredients', self.ingredients))


class RecipesBox:
    recipes = None

    def __init__(self, *args):
        """
         RecipesBox should be a list that holds our recipes
         [...]
        """
        self.recipes = list(args)

    def __iter__(self):
        yield from iter(self.recipes)

    def __repr__(self):
        return ', '.join(repr(rec) for rec in self.recipes)

    def __getitem__(self, item):
        return self.recipes[item]

    def __setitem__(self, key, value):
        self.recipes[key] = value

    def __delitem__(self, key):
        del self.recipes[key]

    def __len__(self):
        return len(self.recipes)

    def insert(self, index, recipe):
        return self.recipes.insert(index, recipe)

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        # return self.recipes_list

    def delete_recipe(self, recipe):
        if len(self.recipes) >= 6:
            self.recipes.remove(recipe)
        else:
            raise ValueError('The recipe cannot be deleted from the RecipeBox!')

    def get_by_name(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                return recipe
        else:
            return

    def pick(self, recipe_name=None):
        result = self.get_by_name(recipe_name)
        if not result:
            result = random.choice(self.recipes)
        return result

    def __str__(self):
        return ', '.join(recipe.name for recipe in self.recipes)


class Fridge(PrettyPrinterMixin):
    def __init__(self, ingredients):
        """
        Ingredients should be a dictionary
        {egg:3, milk:3, flour:2, sugar:1}
        """

        self.ingredients = ingredients
        if len(self.ingredients) < 5:
            raise Exception('The ingredients number should be at least 5!')

    def __getitem__(self, item):
        return self.ingredients[item]

    def __setitem__(self, key, value):
        self.ingredients[key] = value

    def __delitem__(self, key):
        del (self.ingredients[key])

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.ingredients)

    def __contains__(self, key):
        return key in self.ingredients

    def check_ingredient(self, name):
        if name in self.ingredients:
            return 'Yes'
        else:
            return 'Nope'

    def add_ingredient(self, name, qty):
        if name in self.ingredients:
            self.ingredients[name] += qty
        else:
            self.ingredients[name] = qty

    def remove_ingredient(self, name, qty):
        if name in self.ingredients:
            self.ingredients[name] -= qty
            if self.ingredients[name] <= 0:
                del self.ingredients[name]
                print('The ingredient {} is completely removed from the fridge !'.format(name))
        else:
            print('The ingredient {} is not in the fridge at all !'.format(name))

    def check_recipe(self, recipe):
        existing_items, missing_items = [], []
        for x in recipe.ingredients:
            (missing_items, existing_items)[x in self.ingredients].append(x)
        return existing_items, missing_items


def check_the_fridge(fridge, recipesbox):
    recipes_list = []
    for recipe in recipesbox:
        present_ingredients = [ingred for ingred in recipe.ingredients if ingred in fridge]
        if len(present_ingredients) / len(recipe.ingredients) >= 0.5:
            recipes_list.append(recipe.name)

    print(recipes_list)
    return recipes_list


def archive_shopping_list(fnc):
    def archive_list(fridge, recipe):
        missing_ingredients = fnc(fridge, recipe)
        archived_list.append(missing_ingredients)
        return missing_ingredients

    return archive_list


def pretty_print_recipe(fnc):
    def wrapper(fridge, recipe):
        shopping_list = fnc(fridge, recipe).items()
        middle_width = 28
        list_str = "\n".join(["    | {0}. {1}: {2}|.".format(
            str(index).rjust(4), key.ljust(14, '.'), str(value).ljust(5))
            for index, (key, value) in enumerate(shopping_list, 1)])

        print("".join([
            __header,
            "    |{}|. \n".format("Shopping list:".center(middle_width)),
            "    |{}|.\n".format("".center(middle_width)),
            "    |{}|.\n".format("".center(middle_width)),
            list_str,
            __footer
        ]))
        return shopping_list

    return wrapper


@pretty_print_recipe  # fnc = archive_shopping_list
@archive_shopping_list  # fnc = prepare_shopping_list
def prepare_shopping_list(fridge, recipe):
    shopping_list = {}

    existing_items, missing_items = fridge.check_recipe(recipe)

    shopping_list.update({item: recipe.ingredients[item] for item in missing_items})

    for item in existing_items:
        fridge_qty = fridge.ingredients[item]
        recipe_qty = recipe.ingredients[item]
        if recipe_qty > fridge_qty:
            shopping_list.update({item: recipe_qty - fridge_qty})
    return shopping_list


@pretty_print_recipe
@archive_shopping_list
def prepare_shopping_list_for_recipebox(fridge, recipebox):
    shopping_list = {}
    back_fridge_ingredients = deepcopy(fridge.ingredients)

    for recipe in recipebox:
        existing_items, missing_items = fridge.check_recipe(recipe)

        for item in missing_items:
            if item in shopping_list:
                shopping_list[item] += recipe.ingredients[item]
            else:
                shopping_list.update({item: recipe.ingredients[item]})

        for item in existing_items:
            fridge_qty = fridge.ingredients[item]
            recipe_qty = recipe.ingredients[item]
            if recipe_qty > fridge_qty:
                missing_qty = recipe_qty - fridge_qty
                fridge.remove_ingredient(item, recipe_qty)
            else:
                fridge.remove_ingredient(item, recipe_qty)
                missing_qty = 0

            if not missing_qty:
                continue

            if item in shopping_list:
                shopping_list[item] += missing_qty
            else:
                shopping_list.update({item: missing_qty})

    fridge.ingredients = back_fridge_ingredients
    return shopping_list
