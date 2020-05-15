import random


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
        except ValueError as err:
            print(f"Oops!! {err} occurred. Item no longer in the Recipe Box")

    def list_recipes(self):
        for recipe in self.recipes:
            print(recipe.name, "\n")
