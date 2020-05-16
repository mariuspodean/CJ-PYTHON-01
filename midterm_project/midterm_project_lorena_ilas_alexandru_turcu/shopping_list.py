import random


class PrittyPrinterMixin:

    def display(self):
        return ["{0}. {1}: {2}".format(index + 1, key, value)
                for index, (key, value) in enumerate(self.contents())]

    # we made an executive decision to call this function bambucea after many errors ;)
    def bambucea(self):
        separator = "*" * 25
        return "\n".join([
            separator, self.name, separator + "\n", *self.display(), "\n", separator, "\n"
        ])


class Recipe(PrittyPrinterMixin):

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def contents(self):
        return self.ingredients.items()

    def __str__(self):
        return self.bambucea()

    def __iter__(self):
        return self.ingredients

    def __len__(self):
        return len(self.ingredients)

    def keys(self):
        return self.ingredients.keys()

    def __eq__(self, other):
        return self.name == other

    def name(self):
        return self.name


class RecipeBox:

    def __init__(self):
        self.recipes = []

    def contents(self):
        return self.recipes

    def __delitem__(self, key):
        del self.recipes[key]

    def __len__(self):
        return len(self.recipes)

    def __str__(self):
        return str([recipe.name for recipe in self.recipes])

    def append(self, recipe):
        return self.recipes.append(recipe)

    def delete(self, recipe):
        self.recipes.remove(recipe)

    def pick(self, name=None):
        if not name:
            return self.recipes[random.randint(0, len(self) - 1)]
        elif name not in self.recipes:
            return NameError(f'Recipe with the {name} does not exist.')

        for recipe in self.recipes:
            if name == recipe.name:
                return recipe


class Fridge(PrittyPrinterMixin):

    def __init__(self):
        self.name = "Fridge"
        self.products = {}

    def contents(self):
        return self.products.items()

    def __str__(self):
        return self.bambucea()

    def __setitem__(self, key, value):
        if value:
            self.products[key] = value
            return
        print('Product {} will be removed completely from the fridge!\n'
              .format(key))
        del self.products[key]

    def __delitem__(self, key):
        del self.products[key]

    def __iter__(self):
        return self.products

    def __len__(self):
        return len(self.products)

    def __contains__(self, key):
        return key in self.products.keys()

    def append(self, product, quantity):
        self.products[product] = quantity
        if not product or not quantity:
            pass

    def check_recipe(self, recipe):
        available, not_available = [], []
        for item in recipe.keys():
            product = available if item in self else not_available
            product.append(item)

        return available, not_available

    def check_is_enough_quantity(self, item, value):
        if item not in self:
            return 0
        if value > self.products[item]:
            return value - self.products[item]

        return None


def check_the_fridge(fridge, recipes_box):
    return [recipe.name for recipe in recipes_box.contents()
            if len(fridge.check_recipe(recipe)[0]) > len(recipe) / 2]


def archive_shopping_list(func):
    def wrapper(fridge, recipe):
        shopping_list_archive.append(func(fridge, recipe))

    return wrapper


def pretty_print_recipe(func):
    def wrapper(fridge, recipe):
        shopping_list = func(fridge, recipe).items()
        list_str = "\n".join(["\t| {0}. {1}: {2} {3}|.".format(
            index + 1, key, value, (22 - (len(str(index + 1)) + len(str(key)) + len(str(value)))) * " ")
            for index, (key, value) in enumerate(shopping_list)])
        print("".join([
            __header__,
            "\t| \t\tShopping list: \t\t |. \n",
            "\t| \t\t\t\t\t\t\t |.\n",
            "\t| \t\t\t\t\t\t\t |.\n",
            list_str,
            __footer__
        ]))
        return func(fridge, recipe)

    return wrapper


@archive_shopping_list
@pretty_print_recipe
def prepare_shopping_list(fridge, recipe):
    shopping_list = {}
    for item, value in recipe.contents():
        fridge_check = fridge.check_is_enough_quantity(item, value)
        if fridge_check is not None:
            shopping_list.update({item: value})
        else:
            pass

    return shopping_list


shopping_list_archive = []

__header__ = '''
   ______________________________
 / \                             \.
|   |                            |.
 \_ |                            |.
    |                            |.
'''
__footer__ = r'''
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/dc__________________________/.
'''
