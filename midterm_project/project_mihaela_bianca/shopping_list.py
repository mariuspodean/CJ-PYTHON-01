import random


# class PrettyPrinter:
#     def __init__(self,*args,**kwargs):
#         self.args = args
#         self.kwargs = kwargs
#     def __iter__(self):
#         return self.kwargs
#     def __str__(self):
#         message='ceva '
#         dash = '*' * 30
#         result = ' {} \n{} \n{} \n '.format(dash, message, dash)
#         for index, ingred in enumerate(self.kwargs, start=1):
#             result += '\n{}  {} :{} \n '.format(index, ingred, self.kwargs[ingred])
#         result += '\n {}'.format(dash)
#         return result


class Recipe:

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
        return self.ingredients

    def __str__(self):
        dash = '*' * 30
        result = ' {} \n{} \n{} \n '.format(dash, 'Famous ' + self.name, dash)

        for index, ingredients in enumerate(self.ingredients, start=1):
            result += '\n{}  {} :{} \n '.format(index, ingredients, self.ingredients[ingredients])
        result += '\n {}'.format(dash)
        return result

    def display(self):
        print('{} = \n {} \n '.format(self.name + '_ingredients', self.ingredients))


class RecipesBox:

    def __init__(self, recipe):
        """
             RecipesBox should be a list that holds our recipes
             [...]
        """
        self.recipe = recipe

    def __iter__(self):
        return self

    def __repr__(self):

        return str(self)

    def __getitem__(self, item):
        return self.recipe[item]

    def add_recipe(self, name):
        self.recipe.append(name)
        # return self.recipes_list

    def delete_recipe(self, name):
        if len(self.recipe) >= 6:
            self.recipe.remove(name)
        #   return self.recipes_list
        else:
            raise ValueError('The recipe cannot be deleted from the RecipeBox!')

    def pick(self, recipe=None):
        if recipe:
            return Recipe(recipe.name, recipe.ingredients)
        else:
            return random.choice(self.recipe)

    def __str__(self):
        return '{} '.format(self.recipe)


class Fridge:
    def __init__(self, ingredients):
        """
        Ingredients should be a dictionary
        {egg:3, milk:3, flour:2, sugar:1}
        """
        self.ingredients = ingredients
        if len(self.ingredients) < 5:
            raise Exception('The ingredients number should be  at least 5 !')

    def __str__(self):
        dash = '*' * 30
        result = ' {} \n{} \n{} \n '.format(dash, 'The fridge contains: ', dash)
        for index, ingred in enumerate(self.ingredients, start=1):
            result += '\n{}  {} :{} \n '.format(index, ingred, self.ingredients[ingred])
        result += '\n {}'.format(dash)
        return result

    def check_ingredient(self, name):
        if name in self.ingredients.keys():
            return 'Yes'
        else:
            return 'Nope'

    def check_recipe(self, recipe):

        ingred_in = []
        recipe = Recipe(recipe.name, recipe.ingredients)

        if recipe in RecipesBox.recipe:
            for ingredient in list(recipe.ingredients.keys()):
                self.check_ingredient(ingredient)
                ingred_in.append(self.check_ingredient(ingredient))
                if ingred_in.count('Yes') / len(ingred_in) > 0.5:
                    return 'The recipe {} can be  cooked!'.format(recipe)
                else:
                    return 'Not  enough ingredients for the recipe {} !'.format(recipe)
