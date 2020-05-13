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
        self.recipe = {self.name: self.ingredients}
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

    def keys(self):
        return self.recipe.keys()

    def values(self):
        return self.recipe.values()


    def display(self):
        print('{} = \n {} \n '.format(self.name + '_ingredients', self.ingredients))


class RecipesBox:
    recipe = None

    def __init__(self, *args):
        """
             RecipesBox should be a list that holds our recipes
             [...]
        """
        self.recipe = list(args)

    def __iter__(self):
        return RecipesBox(self.recipe)

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
        keys_list = []
        for recipe in self.recipe:
            keys_list.append(recipe.name)
        print_string = ''
        for recipe_name in keys_list:
            print_string='\n '.join((print_string, recipe_name))

        return print_string


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

    def add_ingredient(self, name, qty):
        if name in self.ingredients.keys():
            self.ingredients[name] += qty

        else:
            self.ingredients[name] = qty

    def remove_ingredient(self, name, qty):
        if name in self.ingredients.keys():
            self.ingredients[name] -= qty
            if self.ingredients[name] <= 0:
                del self.ingredients[name]
                return 'The ingredient {} is completely removed from the fridge !'.format(name)
        else:
            return 'The ingredient {} is not in the fridge at all !'.format(name)

    def check_recipe(self, recipe):
        ingred_list=list(recipe.values())
        ingred_recipe=list(ingred_list[0].keys())
        ingred_in_fridge= list(self.ingredients.keys())
        existing_ingredients = []
        missing_ingredients = []
        print('The recipe  ingredients are :', ingred_recipe)
        print('Ingredients in the fridge are :', ingred_in_fridge)

        for ingredient in ingred_recipe:
            if ingredient in ingred_in_fridge:
                existing_ingredients.append(ingredient)
            else:
                missing_ingredients.append(ingredient)

        print('Existing ingredients are :', existing_ingredients)
        print('The missing ingredients are:', missing_ingredients)




# def check_the_fridge(fridge, recipesbox):
#     ingred_in = []
#     recipe = Recipe(name, ingredients)
#     fridge = Fridge(ingredients)
#     recipesbox = RecipesBox(recipe)
#     for recipe in recipesbox.recipe:
#         for ingredient in list(recipe.ingredients.keys()):
#             fridge.check_ingredient(ingredient)
#             ingred_in.append(fridge.check_ingredient(ingredient))
#         if ingred_in.count('Yes') / len(ingred_in) > 0.5:
#             return 'The recipe {} can be  cooked!'.format(recipe.name)
#         else:
#             return 'Not  enough ingredients for the recipe  !'

# def prepare_shopping_list(fridge, recipe):
