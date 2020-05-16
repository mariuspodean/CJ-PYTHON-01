import random

shopping_list_archive=list()
class PrintMixin:

    def display_print(self):
        print("{}\n {}\n{}".format(annotate, self._name, annotate))

        for index, values in enumerate(self._ingredients, start=1):
            print("{}. {}: {}".format(index, values.title(), self._ingredients[values]))

        print('{}'.format(annotate))


class Recipe(PrintMixin):

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


class RecipeBox:

    def __init__(self):
        self.recipes = []

    # using the pick method we can
    # extract a recipe by name or get
    # a random recipe from the recipe box

    def pick(self, name):
        if name in self.recipes:
            return name
        else:
            return self.recipes[random.choice(self.recipes)]

    def add(self, recipe):
        self.recipes.append(recipe)

    def delete(self, name):
        try:
            self.recipes.remove(name)
            # return self.recipes
        except ValueError as err:
            print(f"Oops!! {err} occurred. Item no longer in the Recipe Box")

    def list_recipes(self):
        for recipe in self.recipes:
            print(recipe.name, "\n")


class Fridge(PrintMixin):

    def __init__(self,ingredients={}):
        self.ingredients = ingredients

    def check_recipe(self,recipe):
        pass

    def add_item(self,ingredinent,quantity):
        self.ingredients.update(ingredinent)
        self.quantity.update(quantity)
        return "Add {} with {} quantity".format(self.ingredient,self.quantity)

    def delete_item(self,ingredient):
        if ingredient in self.ingredients:
            self.quantity =0
            return self.ingredients.remove(ingredient)
        else:print("Ingredient not found, can't delete ")

    def update_quantity(self,ingredient,quantity):
        if ingredient in self.ingredients:
            self.quantity = quantity
            if self.quantity <=0:
                return self.ingredients.remove(ingredient)
            else: return self.ingredients


    def __contains__(self, item):
        return item in self.ingredients

    def check_the_fridge(fridge,recipe_box):
        pass

    @pretty_print_recipe
    @archive_shopping_list
    def prepare_shopping_list(self):
        pass

    def pretty_print_recipe(fnc):

        pass

    def archive_shopping_list(fnc):
        return shopping_list_archive.update(fnc)
        pass