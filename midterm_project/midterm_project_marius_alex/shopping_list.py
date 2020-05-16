from random import randrange


class PrettyPrinterMixin:
    def __str__(self):
        dash = '*' * 3
        return '{} PrettyPrinter {} \n '.format(dash, dash)


class Recipe(PrettyPrinterMixin):

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        if len(self.ingredients) < 4:
            raise Exception('4 Ingredients at the min!')

    def __iter__(self):
        return self.ingredients

    def __getitem__(self, key):
        return self.__dict__[key]

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        dash = '*' * 20
        more_stars = PrettyPrinterMixin.__str__(self)
        result = '{} \n{} \n{} \n '.format(dash, self.name, dash)
        for index, ingredients in enumerate(self.ingredients, start=1):
            result += '\n{}.  {} :{} \n '.format(index, ingredients, self.ingredients[ingredients])
        result += '\n {}'.format(dash)
        result += '\n {}'.format(more_stars)
        return result

    def keys(self):
        return self.ingredients.keys()

    def values(self):
        return self.ingredients.values()


class RecipesBox:
    def __init__(self, iterable):
        self.recipes_list = list(iterable)

    def __iter__(self):
        return iter(self.recipes_list)

    def __len__(self):
        return len(self.recipes_list)

    def __getitem__(self, index):
        return self.recipes_list[index]

    def __next__(self):
        if self.x <= self.num:
            odd_num = self.x
            self.x += 1
            return odd_num
        else:
            raise StopIteration

    def add_recipe(self, recipe):
        self.recipes_list.append(recipe)
        return self.recipes_list

    def delete_recipe(self, recipe):
        self.recipes_list.remove(recipe)
        return self.recipes_list

    def pick(self, name=None):
        if name is None:
            random_index = randrange(0, stop=len(self.recipes_list))
            print(self.recipes_list[random_index])
        else:
            for recipe in self.recipes_list:
                if str(name) == str(recipe.name):
                    print(recipe)

    # What happens if the recipe doesnt exist?

    def __str__(self):
        print_list = str('The recipes are:')
        for recipe in self.recipes_list:
            print_list += '{}, '.format(recipe.name)
        return print_list


class Fridge(PrettyPrinterMixin):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __iter__(self):
        return self.ingredients

    def __getitem__(self, key):
        return self.__dict__[key]

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        more_stars = PrettyPrinterMixin.__str__(self)
        dash = '*' * 20
        result = ' {} \n{} \n{} \n '.format(dash, 'bla fridge bla: ', dash)
        for index, item in enumerate(self.ingredients, start=1):
            result += '\n{}  {} :{} \n '.format(index, item, self.ingredients[item])
        result += '\n {}'.format(dash)
        result += '\n {}'.format(more_stars)
        return result

    def add_ingredient(self, ingredient):
        self.ingredients.update(ingredient)
        return self.ingredients

    def remove_ingredient(self, name, qty):
        if name in self.ingredients.keys():
            self.ingredients[name] -= qty
            if self.ingredients[name] <= 0:
                del self.ingredients[name]
                return '{} was removed from the fridge !'.format(name)

    def update_ingredient(self, name, qty):
        if name in self.ingredients.keys():
            self.ingredients[name] += qty
        else:
            print("('{} is not in the fridge!'.format(name))")

    def delete_recipe(self, ingredient):
        self.ingredients.pop(ingredient)
        return self.ingredients

    def check_ingredient(self, name):
        if name in self.ingredients.keys():
            return 'Bla {} bla bla !'.format(name)
        else:
            raise ValueError('bla {} is not bla bla!'.format(name))

    def check_recipe(self, recipe):
        available_ingredients = []
        missing_ingredients = []
        for key, value in recipe.ingredients.items():
            if key in self.ingredients.keys() and value <= self.ingredients[key]:
                available_ingredients.append(key)
            else:
                missing_ingredients.append(key)
        print(available_ingredients, missing_ingredients)


def check_the_fridge(fridge_container, recipe_container):
    available_recipes = []
    for recipe in recipe_container:
        available_ingredients = 0
        for key, value in recipe.ingredients.items():
            if key in fridge_container.ingredients.keys() and value <= fridge_container.ingredients[key]:
                available_ingredients += 1
            if available_ingredients >= len(recipe.ingredients):
                available_recipes += [recipe.name]
    return available_recipes


def shopping_list_archive(fnc):
    def func_wrapper(recipe):
        shopping_list = fnc(recipe)
        if type(shopping_list) == dict:
            shopping_archive.append(shopping_list)
        return shopping_list

    return func_wrapper


def pretty_print_recipe(func):
    def func_wrapper_2(recipe):
        ingredients = func(recipe)
        dash = '*' * 20
        result = '{} \n{} \n{} \n '.format(dash, recipe, dash)
        for index, values in enumerate(ingredients, start=1):
            result += '\n{}.  {} :{} \n '.format(index, ingredients, ingredients[values])
        result += '\n {}'.format(dash)
        return result

    return func_wrapper_2


@pretty_print_recipe
@shopping_list_archive
def prepare_shopping_list(recipe):
    shopping_list = {}
    for key, value in recipe.ingredients.items():
        if key not in fridge.ingredients.keys() or value > fridge.ingredients[key]:
            shopping_list.update({key: value})
    return shopping_list


