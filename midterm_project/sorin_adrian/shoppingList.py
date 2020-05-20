from random import randrange
import time


# creating a paragraph for nice printing recipe and fridge content
class PrettyPrinterMixin:

    def __str__(self):
        # select the proper title to print
        if self.__class__.__name__ == "Fridge":
            title = self.__class__.__name__
        else:
            title = self.recipe_name

        # geting the value of the longest ingredient name or title for setting the width of paragraph
        keys_list = list(self.keys())
        keys_list.append(title)
        max1 = len(max(keys_list, key=len)) + 10

        # formating the header/footer/title
        header = footer = f'{"*" * (max1 + 6)}'
        title_ready = f'*\033[1m\033[90m{title.center(max1 + 4)}\033[0m*'
        empty_line = f'*{" " * (max1 + 4)}*'
        header_with_title = '\n'.join(('', header, title_ready, header, empty_line, ''))

        # adding the ingredients for printing
        body = ''
        for counter, ingred_quant in enumerate(self.items(), 1):
            space = ''
            x = 0
            if counter < 10:
                space = ' '
            else:
                x = 1
            ingred_quant_print = f'{ingred_quant[0].title()} : {ingred_quant[1]}'
            body = ''.join(
                (
                    body,
                    f'* {space}\033[90m\x1B[3m{counter}. {ingred_quant_print.ljust(max1 - len(space) - x)}\033[0m*\n'
                )
            )
        # text format (colr, font style) and footer adding
        empty_line_footer = f'{empty_line}\n{footer}'
        print_string = ''.join((header_with_title, body, empty_line_footer))

        return print_string


# class instantiate each recipe
class Recipe(PrettyPrinterMixin):

    def __init__(self, recipe_name=None, recipe_ingredients=None):
        self.recipe_name = recipe_name
        self.recipe_ingredients = recipe_ingredients
        # self._recipe = {self.recipe_name: self.recipe_ingredients}

    def __repr__(self):
        print_string = f'{self.recipe_name}: {self.recipe_ingredients}'
        return print_string

    def __len__(self):
        return len(self.recipe_ingredients)

    def __iter__(self):
        return self.recipe_ingredients

    def __getitem__(self, item):
        return self.recipe_ingredients[item]

    def __contains__(self, item):
        return item in self.recipe_ingredients

    def keys(self):
        return self.recipe_ingredients.keys()

    def values(self):
        return self.recipe_ingredients.values()

    def items(self):
        return self.recipe_ingredients.items()


# class instantiate a recipe_box instance for archive all the recipes created
class RecipesBox:

    def __init__(self):
        self._recipesbox_list = []

    def __str__(self):
        print_string = ''

        for recipe in self._recipesbox_list:
            recipe_title = f'{recipe.recipe_name}\n'
            print_string = ''.join((print_string, recipe_title))

        return print_string

    def __len__(self):
        return len(self._recipesbox_list)

    def __getitem__(self, index):
        return self._recipesbox_list[index]

    def __contains__(self, item):
        return item in self._recipesbox_list

    def __setitem__(self, index, value):
        self._recipesbox_list[index] = value

    def __delitem__(self, index):
        del self._recipesbox_list[index]

    def remove(self, item):
        self._recipesbox_list.remove(item)

    def append(self, item):
        self._recipesbox_list.append(item)

    # eliminate a recipe from recipes_box list by its index
    def pop(self, index=None):
        if index:
            return self._recipesbox_list.pop(index)
        else:
            return self._recipesbox_list.pop()

    # method get a recipe as argument, extract the recipe from recipes_box and print it
    def pick(self, recipe=None):
        if recipe:
            index = self._recipesbox_list.index(recipe)
        else:
            max_rand_no = len(self._recipesbox_list)
            index = randrange(0, max_rand_no, 1)

        return self._recipesbox_list[index]


# class create a instance for archive ingredients for recipes
class Fridge(PrettyPrinterMixin):

    def __init__(self):
        self._fridge = {}

    def __getitem__(self, item):
        return self._fridge[item]

    def __iter__(self):
        return iter(self._fridge)

    def __len__(self):
        return len(self._fridge)

    def __contains__(self, item):
        return item in self._fridge

    def __delitem__(self, key):
        del self._fridge[key]

    def keys(self):
        return self._fridge.keys()

    def values(self):
        return self._fridge.values()

    def items(self):
        return self._fridge.items()

    def update(self, *args, **kwargs):
        self._fridge.update(*args, **kwargs)

    # methode allow to update the quantity of one existing ingredient from the fridge
    def update_quantity(self, ingredient, quantity):
        updated_quantity = self._fridge[ingredient] + quantity
        if updated_quantity > 0:
            self._fridge[ingredient] = updated_quantity
        else:
            print(f'There is no more \033[31m\033[01m{ingredient}\033[0m in the fridge, go shopping !!!\n')
            del self._fridge[ingredient]

    # methode check if there are in the frig all the required ingredients for a recipe
    def check_recipe(self, recipe):
        recipe_ingredients = set(recipe.recipe_ingredients)
        fridge_ingredients = set(self._fridge.keys())
        ingredients_in = recipe_ingredients.intersection(fridge_ingredients)
        ingredients_off = recipe_ingredients.difference(fridge_ingredients)

        message = f'There are no missing ingredients for preparing the {recipe.recipe_name}'
        message_2 = ['No ingredients in fridge']

        return ingredients_in if ingredients_in else message_2, ingredients_off if ingredients_off else message


"""
function check the fridge, for all recipes, if there are in the fridge at least half of the ingredients required
and print the list with all the recipes that satisfies the condition
"""


def check_the_fridge(fridge, recipes_box):
    viable_recipes_list = [
        recipe.recipe_name
        for recipe in recipes_box
        for ingredients_recipe_in, x in [fridge.check_recipe(recipe)]
        if len(ingredients_recipe_in) >= len(recipe.recipe_ingredients) / 2
    ]

    return viable_recipes_list


# decorator for archiving all the shiping list
def archive_shopping_list(fnc2):
    def inner_func_2(fridge, recipe):
        shopping_list = fnc2(fridge, recipe)
        time_now = time.localtime()
        date_today = time.strftime('%d %m %Y', time_now)
        # shopping_list = Recipe(recipe.recipe_name, missing_ingredients)
        if type(shopping_list) == dict:
            shopping_list_archive.append((date_today, recipe.recipe_name, shopping_list))

        return shopping_list

    return inner_func_2


# decorator for nicely print the shopping list
def pretty_print_recipe(fnc_1):
    def inner_func_1(fridge, recipe):

        ingredients_dict = fnc_1(fridge, recipe)
        time_now = time.localtime()
        date_today = time.strftime('%d %m %Y', time_now)

        if type(ingredients_dict) == dict:

            title = f'{recipe.recipe_name}-Shopping List'

            header = f"""
                    \r  /{"= =" * 12}\\
                    \r /={"= =" * 12}=\\
                    \r|| {"  " * 18} ||
                    \r|| \033[34m\033[01m{title.center(36)}\033[0m ||
                    \r|| {"= " * 18}=||
                    \r|| {"  " * 18} ||\n"""

            body = ''
            empty_lines = 0

            for counter, ingred_quant in enumerate(ingredients_dict, 1):
                ingred_quant_print = f'{ingred_quant} : {ingredients_dict[ingred_quant]}'
                body = ''.join(
                    (
                        body,
                        f'|| \033[90m\x1B[3m{counter}. {ingred_quant_print.ljust(34)}\033[0m||\n'
                    )
                )
                empty_lines = 16 - counter

            empty_part = f'||{" " * 38}||\n'
            empty_part = empty_part * empty_lines
            logo = f"""||{" " * 38}||
                     \r||{" " * 19} // ""--.._        ||
                     \r||{" " * 19}||  (_)  _ "-._    ||
                     \r||{" " * 19}||    _ (_)    '-_ ||
                     \r||{" " * 19}||   (_)   __..-'  ||
        \r|| {date_today}{" " * 8} \__..--""         ||
                    """
            footer = f"""\r \={"= =" * 12}=/  
                         \r  \{"= =" * 12}/
                     """
            result_tuple = (header, body, empty_part, logo, footer)
            result = ''.join(result_tuple)

        else:
            result = ingredients_dict

        print(result)

        return ingredients_dict

    return inner_func_1


# function that creates a shopping list containing all the missing ingrediants for a recipe
@archive_shopping_list
@pretty_print_recipe
def prepare_shopping_list(fridge, recipe):
    shopping_list = {}

    for ingredient, quantity in recipe.recipe_ingredients.items():

        if ingredient in fridge and quantity > fridge[ingredient]:

            missing_quantity = quantity - fridge[ingredient]
            shopping_list.update({ingredient: missing_quantity})

        elif ingredient not in fridge:

            shopping_list.update({ingredient: quantity})

        message = f'For {recipe.recipe_name} there are all the ingredients in the fridge'

    return shopping_list if shopping_list else message


# list as a database for archiving all the shopping lists
shopping_list_archive = []
