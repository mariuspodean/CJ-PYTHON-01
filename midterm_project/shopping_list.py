import random

annotations = ["-", "*", "+", "-"]
annotate = random.choice(annotations) * 25

mac_and_cheese_ingredients = {
    'macaroni': 1,
    'cheese': 0.5,
    'butter': 1,
    'milk': 1
}


class Recipe:

    def __init__(self, name, ingredients):
        self._name = name
        self._ingredients = ingredients

    @property
    def name(self):
        return self._name

    @property
    def ingredients(self):
        return self._ingredients

    def keys(self):
        return self._ingredients.keys()

    def __iter__(self):
        return self._ingredients

    def __len__(self):
        return len(self._ingredients)

    def __contains__(self, item):
        return item in self._ingredients

    def __str__(self):
        print("{}\n {}\n{}".format(annotate, self._name, annotate))

        for index, values in enumerate(self._ingredients, start=1):
            print("{}. {}: {}".format(index, values.title(), self._ingredients[values]))

        print('{}'.format(annotate))
        return ""


class RecipeBox(Recipe):

    def __init__(self, name, ingredients):
        super().__init__(name, ingredients)
        self.recipes = []

    # using the pick method we can
    # extract a recipe by name or get
    # a random recipe from the recipe box

    def pick(self, name=None):
        if name and name in self.recipes:
            return name
        else:
            return self.recipes[random.choice(self.recipes)]

    def __str__(self):
        return f"{self.name}"
        # prints name only

    def add(self, recipe):
        self.recipes.append(recipe)

    def __delitem__(self, key):
        del self.name[key]


class Fridge:
    # mutable mapping __getitem__,  __setitem__,__delitem__,__iter__,__len__,
    # pop, popitem,clear, update, setdefault
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def check_recipe(self, recipe):
        pass

    # see if we have all the requireed ingredients from fridge
    # return 1 list with items from recipe that we have in fridge
    # return 1 list with items we don't have in fridge'
    def add_item_in_fridge(item, quantity):
        return Fridge(item, quantity)

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, item):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __str__(self):
        return "{}".format(self.item)


class PrittyPrinter:
    # mixin class will be used by Fridge and Recipe
    # to print nicely their contents

    def check_the_fridge(fridge, recipes_box):
        pass


# @archive_shopping_list
# @pretty_print_recipe
def prepare_shopping_list(fridge, recipe):
    pass
# @archive_shopping_list