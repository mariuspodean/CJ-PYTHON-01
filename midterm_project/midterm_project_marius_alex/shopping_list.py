from random import choice


class PrettyPrinterMixin:

    def pretty_print(self):
        dash = '*' * 5
        display = [f'{dash} \n{self.name.capitalize()} \n{dash}']
        for idx, ing in enumerate(self.ingredients, start=1):
            for ing, qty in self.ingredients.items():
                display.append(f'{idx}. {ing.capitalize()}: {qty}')
            display.append(dash)
            return '\n'.join(display)


class Recipe(PrettyPrinterMixin):

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return self.pretty_print()

    def items(self):
        return self.ingredients.items()

    def keys(self):
        return self.ingredients.keys()

    def values(self):
        return self.ingredients.values()

    def __iter__(self):
        return iter(self.ingredients)

    def __getitem__(self, index):
        return self.ingredients[index]

    def __len__(self):
        return len(self.ingredients)


class RecipeBox:

    def __init__(self, recipes):
        self.recipes = list(recipes)

    def __str__(self):
        dash = "*" * 5
        print_list = [f'{dash} \nRecipes in the box: \n{dash}']
        for recipe in self.recipes:
            print_list.append(recipe.name)
        return '\n'.join(print_list)

    def __iter__(self):
        return iter(self.recipes)

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def del_recipe(self, recipe):
        self.recipes.remove(recipe)

    def pick(self, name=None):
        if name is None:
            return choice(self.recipes)
        else:
            for recipe in self.recipes:
                if name == recipe.name:
                    return recipe
                else:
                    return ('Recipe not found')



class Fridge(PrettyPrinterMixin):

    def __init__(self, name, ingredients):
        self.ingredients = ingredients
        self.name = name

    def __str__(self):
        return self.pretty_print()

    def __contains__(self, product):
        return product in self.ingredients.keys()

    def add_ingredient(self, product):
        return self.ingredients.update(product)

    def update_ingredient(self, name, qty):
        if name in self.ingredients.keys():
            self.ingredients[name] += qty
        else:
            print("('{} is not in the fridge!'.format(name))")

    def remove_ingredient(self, name, qty):
        if name in self.ingredients.keys():
            self.ingredients[name] -= qty
            if self.ingredients[name] <= 0:
                del self.ingredients[name]
                return '{} was removed from the fridge !'.format(name)

    def check_product(self, product):
        if product in self.ingredients.keys():
            print('yap, we got milk!')
        else:
            raise ValueError('nop')

    def check_recipe(self, recipe):
        available_ingredients = []
        missing_ingredients = []
        for ing, qty in recipe.items():
            if ing in self.ingredients.keys() and qty <= self.ingredients[ing]:
                available_ingredients.append(ing)
            else:
                missing_ingredients.append(ing)
        print(f'Available ingredients for: {available_ingredients} \nMissing ingredients: {missing_ingredients}')


def check_fridge(fridge, recipe_box):
    recipes_possible = []
    for recipe in recipe_box:
        available_ing = 0
        for ing, qty in recipe.ingredients.items():
            if ing in fridge.ingredients.keys():
                available_ing += 1
        if available_ing >= len(recipe.ingredients) / 2:
            recipes_possible += [recipe.name]
    print(f'Possible recipes: {recipes_possible}')


shopping_archive = []


def pretty_print_recipe(fnc):
    def wrapper(fridge, recipe):
        ingredient = fnc(fridge, recipe)
        dash = '*' * 5
        result = f'{dash}\nShopping List \n{recipe.name}:\n'
        for ing, qty in ingredient.items():
            result += '{}: {}\n'.format(ing, qty)
        result += '\n{}'.format(dash)
        print(result)

    return wrapper


def archive_shopping_list(fnc):
    def inner_fnc(fridge, recipe):
        shopping_list = fnc(fridge, recipe)
        for ing, qty in shopping_list.items():
            shopping_archive.append({ing: qty})
        return shopping_list

    return inner_fnc


@pretty_print_recipe
@archive_shopping_list
def prepare_shopping_list(fridge, recipe):
    shopping_list = {}
    for ing, qty in recipe.ingredients.items():
        if ing not in fridge.ingredients.keys() or qty > fridge.ingredients[ing]:
            shopping_list.update({ing: qty})
    return shopping_list
