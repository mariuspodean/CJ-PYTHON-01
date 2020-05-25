import random
import pprint

pp = pprint.PrettyPrinter(indent=4)

pp_list_header = r"""
   ______________________________
 / \                             \.
|   |     Shopping list:         |.
 \_ |                            |.
    |                            |.
"""

pp_list_tailer = r"""
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/vb__________________________/.
    """

shopping_list_archive = []


class PrittyPrinter():
    """a mixin class used by Fridge and Recipe to print nicely their contents"""
    
    def pp_print_recipe(self):
        pp.pprint(super().__str__())


class Recipe(PrittyPrinter):
    """a recipe created from a name and dictionary of ingredients and quantities"""

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    
    def __str__(self):
        result = ""
        for index, item in enumerate(self.ingredients, start=1):
            result += "{}. {}: {}\n".format(index, item, self.ingredients[item])
        return "{0}\n{1}\n{0}\n{2}\n{0}".format("*"*23, self.name, result)
    
    def __repr__(self):
        return self.ingredients

    def __getitem__(self, item):
        return self.ingredients[item]

    def __len__(self):
        return len(self.ingredients)
    
    def __iter__(self):
        self.x = 0
        return self
    
    def __next__(self):
        if self.x < len(self.ingredients):
            result = list(self.ingredients)[self.x]
            self.x += 1
            return result
        raise StopIteration
    
    def __contains__(self, item):
        return item in self.ingredients.keys()


class RecipesBox():
    """a mutable sequence that holds our recipes"""

    def __init__(self, recipies=[]):
        self.recipies = recipies

    def __getitem__(self, item):
        return self.recipies[item]
    
    def __setitem__(self, item, value):
        self.recipies[item] = value

    def __delitem__(self, item):
        del self.recipies[item]

    def __len__(self):
        return len(self.recipies)

    def __str__(self):
        result = ""
        for recipie in self.recipies:
            result += recipie.name + "\n"
        return result
    
    def insert(self, item, value):
        self.recipies.insert(item, value)

    def append(self, item):
        self.recipies.append(item)

    def pick(self, name=None):
        for recipie in self.recipies:
            if recipie.name == name:
                return recipie
            else:
                return random.choice(self.recipies)


class Fridge(PrittyPrinter):
    """a mutable mapping that holds some products together with their quantities"""

    def __init__(self, products={}):
        self.products = products

    def __getitem__(self, item):
        return self.products[item]
    
    def __setitem__(self, item, value):
        self.products[item] = value

    def __delitem__(self, item):
        del self.products[item]

    def __len__(self):
        return len(self.products)

    def __iter__(self):
        return iter(self.products)
    
    def __str__(self):
        result = ""
        for index, item in enumerate(self.products, start=1):
            result += "{}. {}: {}\n".format(index, item, self.products[item])
        return "{0}\n{1}\n{0}\n{2}\n{0}".format("*"*16, "Fridge contents", result)
    
    def __repr__(self):
        return self.products

    def __contains__(self, item):
        return item in self.products

    def update(self, item):
        self.products.update(item)
    
    def take(self, item, quantity):
        if item in self.products:
            if self.products[item] - quantity <= 0:
                quantity_taken = self.products[item]
                print("Warning: Ingredient {item} became out of stock and removed from fridge")
                del self.products[item]
                return quantity_taken
            else:
                return quantity
        else:
            return None
    
    def check_recipe(self, recipe):
        existing_items = list(filter(lambda x: x in self.products, recipe.ingredients))
        missing_items = list(filter(lambda x: x not in self.products, recipe.ingredients))
        return existing_items, missing_items


def check_the_fridge(fridge, recipies_box):
    """check the fridge and give a list of recipes for which the ingredients are required"""

    result = []
    for recipe in recipies_box:
        components = fridge.check_recipe(recipe)
        if len(recipe.ingredients)/2 <= len(components[0]):
            result.append(recipe.name)
    return result


def pretty_print_recipe(fct):
    """print a nice representation of the shopping list"""

    def inner(fridge, recipe):
        result = "    |  "
        for index, item in enumerate(fct(fridge, recipe), start=1):
            buffer = 22 - (len(str(index)) + len(item) + len(str(recipe.ingredients[item])))
            tail = " " * buffer
            result += "{}. {}: {}{}|.".format(index, item, recipe.ingredients[item], tail)
        return pp_list_header + result + pp_list_tailer
    return inner


def archive_shopping_list(fct):
    """get shopping list and add it to a list called shopping_list_archive"""

    def archive(fridge, recipe):
        global shopping_list_archive
        shopping_list_archive.append(fct(fridge, recipe))
        return fct(fridge, recipe)
    return archive


@pretty_print_recipe
@archive_shopping_list
def prepare_shopping_list(fridge, recipe):
    """return a dict with the items that we have to buy and their corresponding quantities"""

    components = fridge.check_recipe(recipe)
    missing_quantities = {}
    if len(components[1]):
        missing_quantities.update({item : recipe.ingredients[item] for item in components[1]})
    if len(components[0]):
        for item in components[0]:
            if recipe.ingredients[item] > fridge.products[item]:
                missing_quantities.update({item : recipe.ingredients[item]-fridge.products[item]})
    return missing_quantities
