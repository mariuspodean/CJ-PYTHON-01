from random import choice


class PrettyPrinterMixin:

    def __str__(self):
        dash = '*' * 5
        return f'{dash}'


class Recipe(PrettyPrinterMixin):

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        dash = PrettyPrinterMixin.__str__(self)
        display_recipe = [f'{dash} \n{self.name} \n{dash}']
        for idx, ing in enumerate(self.ingredients, start=1):
            display_recipe.append(f'{idx}. {ing.capitalize()}: {self.ingredients[ing]}')
        display_recipe.append(dash)

        return '\n'.join(display_recipe)

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
                    pass

    def __str__(self):
        print_list = str("Recipes in the box: ")
        for recipe in self.recipes:
            print_list += f'{recipe.name}, '
        return print_list

    def __iter__(self):
        return iter(self.recipes)


class Fridge(PrettyPrinterMixin):

    def __init__(self, products):
        self.products = products

    def __str__(self):
        dash = PrettyPrinterMixin.__str__(self)
        fridge_content = [f'{dash}\nFridge content: \n{dash}']

        for prod in self.products:
            for product, quantity in self.products.items():
                fridge_content.append(f'{product.capitalize()}: {quantity}')
            return '\n'.join(fridge_content)

    def __contains__(self, product):
        return product in self.products.keys()

    def add_ingredient(self, product):
        return self.products.update(product)

    def update_ingredient(self, name, qty):
        if name in self.products.keys():
            self.products[name] += qty
        else:
            print("('{} is not in the fridge!'.format(name))")

    def remove_ingredient(self, name, qty):
        if name in self.products.keys():
            self.products[name] -= qty
            if self.products[name] <= 0:
                del self.products[name]
                return '{} was removed from the fridge !'.format(name)

    def __delitem__(self, product):
        del self.products[product]

    def check_product(self, product):
        if product in self.products.keys():
            print('yap, we got milk!')
        else:
            raise ValueError('nop')

    def check_recipe(self, recipe):
        available_ingredients = []
        missing_ingredients = []
        for ingred, qty in recipe.items():
            if ingred in self.products.keys() and qty <= self.products[ingred]:
                available_ingredients.append(ingred)
            else:
                missing_ingredients.append(ingred)
        print(f'Available ingredients: {available_ingredients} \nMissing ingredients: {missing_ingredients}')


def check_fridge(fridge, recipe_box):
    recipes_possible = []
    for recipe in recipe_box:
        available_ing = 0
        for ing, qty in recipe.ingredients.items():
            if ing in fridge.products.keys():
                available_ing += 1
        if available_ing >= len(recipe.ingredients) / 2:
            recipes_possible += [recipe.name]
    print(f'Possible recipes: {recipes_possible}')


shopping_archive = []


def pretty_print_recipe(fnc):
    def wrapper(fridge, recipe):
        ingredients = fnc(fridge, recipe)
        dash = '*' * 5
        result = '{}\nShopping list:\n'.format(dash)
        for ing, qty in ingredients.items():
            result += '{}: {}\n'.format(ing, qty)
        result += '\n{}'.format(dash)
        print(result)

    return wrapper


def archive_shopping_list(fnc):
    def inner_fnc(fridge, recipe):
        shopping_list = fnc(fridge, recipe)
        shopping_archive.append(shopping_list)
        return shopping_archive

    return inner_fnc


@archive_shopping_list
@pretty_print_recipe
def prepare_shopping_list(fridge, recipe):
    shopping_list = {}
    for ing, qty in recipe.ingredients.items():
        if ing not in fridge.products.keys() or qty > fridge.products[ing]:
            shopping_list.update({ing: qty})
    return shopping_list
