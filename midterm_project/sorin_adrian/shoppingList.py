from random import randrange
import time

# creating a paragraph for nice printing recipe and fridge content
class PrettyPrinterMixin:

    def __init__(self, recipe_name=None, recipe_ingredients=None):
        self.recipe_name = recipe_name
        self.recipe_ingredients = recipe_ingredients

    def __str__(self, dict_in):
        # select the right title to print
        if self.__class__.__name__ == "Fridge":
            title = self.__class__.__name__
        else:
            title = self.recipe_name

        # geting the value of the longest ingredient name or title for setting the width of paragraph
        keys_list = list(dict_in.keys())
        keys_list.append(title)
        max1 = len(max(keys_list, key=len)) + 8

        # formating the header/footer
        header = footer = f'{"*" * (max1 + 6)}'

        # create the print title
        print_string = f'\n{header}\n*{title.center(max1 + 4)}*\n{header}\n*{" " * (max1 + 4)}*\n'

        # adding the ingredients for printing
        ingredients_dict = dict_in.items()
        for counter, ingred_quant in enumerate(ingredients_dict, 1):

            ingred_quant_print = f'{ingred_quant[0].title()} : {ingred_quant[1]}'
            print_string = ''.join(
                (
                    print_string,
                    f'* {counter}. {ingred_quant_print.ljust(max1)}*\n'
                )
            )

        # text format (colr, font style) and footer adding
        print_string = f'\033[90m\x1B[3m{print_string}*{" " * (max1 + 4)}*\n{footer}\033[0m'

        return print_string

# class instantiate each recipe
class Recipe(PrettyPrinterMixin):

    def __init__(self, recipe_name=None, recipe_ingredients=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recipe_name = recipe_name
        self.recipe_ingredients = recipe_ingredients
        self._recipe = {self.recipe_name: self.recipe_ingredients}

    def __repr__(self):
        print_string = f'{self.recipe_name}: {self.recipe_ingredients}'
        return print_string

    def __str__(self, *args):
        # create the string for printing with mixin class and for the proper data in
        print_string = PrettyPrinterMixin.__str__(self, self.recipe_ingredients)

        return print_string

    def __len__(self):
        return len(self._recipe)

    def __iter__(self):
        iter(self._recipe)

    def __getitem__(self, item):
        return self._recipe[item]

    def __contains__(self, item):
        return item in self._recipe

    def keys(self):
        return self._recipe.keys()

    def values(self):
        return self._recipe.values()

    def items(self):
        return self._recipe.items()

    def __get__(self, instance, owner):
        return self._recipe

    def __eq__(self, other):
        return self.recipe_name == other.recipe_name and self.recipe_ingredients == other.recipe_igredients


# class instantiate a recipe_box instance for archive all the recipes created
class RecipesBox:

    def __init__(self):
        self._recipebox_list = []

    def __str__(self):
        print_string = ''

        for recipe in self._recipebox_list:
            recipe_title = f'{recipe.recipe_name}\n'
            print_string = ''.join((print_string, recipe_title))

        return print_string

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

    # eliminate a recipe from recipes_box list by its index
    def pop(self, index=None):
        if index:
            return self._recipebox_list.pop(index)
        else:
            return self._recipebox_list.pop()

    # method get a recipe as argument, extract the recipe from recipes_box and print it
    def pick(self, recipe=None):
        if recipe:
            index = self._recipebox_list.index(recipe)
        else:
            max_rand_no = len(self._recipebox_list)
            index = randrange(0, max_rand_no, 1)

        return self._recipebox_list.pop(index)


# class create a instance for archive ingredients for recipes
class Fridge(PrettyPrinterMixin):

    def __init__(self):
        self._fridge = {}
        super().__init__()

    def __str__(self, *args):
        # create the string for printing with mixin class and for the proper data in
        print_string = PrettyPrinterMixin.__str__(self, self._fridge)

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

    def items(self):
        return self._fridge.items()

    def __get__(self, instance, owner):
        pass

    def __delitem__(self, key):
        del self._fridge[key]

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


"""
function check the fridge, for all recipes, if there are in the fridge at least half of the ingredients required
and print the list with all the recipes that satisfies the condition
"""
def check_the_fridge(fridge, recipes_box):
    viable_recipes_list = RecipesBox()
    # ingredients_fridge_list = list(fridge.keys())

    for recipe in recipes_box:
        # geting the rcipe ingredients list and their count
        recipe_ingredients = recipe[recipe.recipe_name]
        ingredients_recipe_list = list(recipe_ingredients.keys())
        ingredients_recipe_no = len(ingredients_recipe_list)

        # geting the list of igredients in the fridge for a specified recipe , and how many are in stock
        ingredients_recipe_in, _ = fridge.check_recipe(recipe)
        ingredients_in_no = len(ingredients_recipe_in)

        # check in if there are in the fridge at least half of recipe ingredients
        if ingredients_in_no >= ingredients_recipe_no / 2:
            viable_recipes_list.append(recipe)

    return viable_recipes_list


# decorator for nicely print the shopping list
def pretty_print_recipe(fnc):
    def inner_func(fridge, recipe):

        ingredients_dict = fnc(fridge, recipe)
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
            result = f'\nFor {recipe.recipe_name} all ingredients are in fridge'

        return result

    return inner_func


# decorator for archiving all the shiping list
def c(fnc):
    def inner_func_2(fridge, recipe):
        shopping_list = fnc(fridge, recipe)
        time_now = time.localtime()
        date_today = time.strftime('%d %m %Y', time_now)
        # shopping_list = Recipe(recipe.recipe_name, missing_ingredients)
        if type(shopping_list) == dict:
            shopping_list_archive.append((date_today, recipe.recipe_name, shopping_list))

        return shopping_list

    return inner_func_2


# function that creates a shopping list containing all the missing ingrediants for a recipe
@pretty_print_recipe
@c
def prepare_shopping_list(fridge, recipe):
    shopping_list = {}
    recipe_ingred_dict = recipe[recipe.recipe_name]
    message = ''

    for ingredient, quantity in recipe_ingred_dict.items():

        if ingredient in fridge and quantity > fridge[ingredient]:

            missing_quantity = quantity - fridge[ingredient]
            shopping_list.update({ingredient: missing_quantity})

        elif ingredient not in fridge:

            shopping_list.update({ingredient: quantity})

        message += f'For {recipe.recipe_name} there are all the ingredients in the fridge'

    return shopping_list if shopping_list else message

# list as a database for archiving all the shopping lists
shopping_list_archive = []
