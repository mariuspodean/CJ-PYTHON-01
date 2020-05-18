class PrittyPrinterAndMoreMixin:

    def __getitem__(self, item):
        return self.items[item]

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __eq__(self, other):
        return self.items == other

    def __ne__(self, other):
        return self.items != other

    def keys(self):
        return self.items.keys()

    def items(self):
        return self.items.items()

    def values(self):
        return self.items.values()

    def get(self, item):
        return self.items[item]

    def __repr__(self):
        return f'{self.items}'

    def __str__(self):
        pprow = '*'*(len(self.name)+14)
        the_text = pprow + f'\n* {self.name} - {len(self.items)} items *\n' +pprow + '\n'
        for nr, key in enumerate(self.items, start=1):
            the_text += f'* {nr}. {key} - {self.items[key]}\n'
        the_text += pprow
        return the_text


class Recipe(PrittyPrinterAndMoreMixin):

    def __init__(self, name='noname', ingredients=None):
        if len(ingredients) < 4:
            raise KeyError('Please enter a minimum 4 ingredients')
        self.name = name
        self.items = ingredients


class RecipeBox:

    def __init__(self, *args):
        self.recipe = list(args)

    def __getitem__(self, item):
        return self.recipe[item]

    def __setitem__(self, key, value):
        self.recipe[key] = value

    def __delitem__(self, key):
        del (self.recipe[key])

    def __iter__(self):
        return iter(self.recipe)

    def __len__(self):
        return len(self.recipe)

    def append(self, item):
        self.recipe.append(item)

    def reverse(self):
        self.recipe.reverse()

    def extend(self, other):
        return self.recipe.extend(other)

    def pop(self):
        return self.recipe.pop()

    def remove(self, item):
        self.recipe.remove( item)

    def __add__(self, other):
        return self.recipe.extend(other)

    def __iadd__(self, other):
        return self.recipe.extend(other)

    def __repr__(self):
        return f'{[recipes.name for recipes in self.recipe]}'

    def __str__(self):
        return ' - '.join(self)
        # return f'{[recipes.name for recipes in self.recipe]}'

    def pick(self, name=None):
        pass


class Fridge(PrittyPrinterAndMoreMixin):

    def __init__(self, container):
        if len(container) < 4:
            raise KeyError('Fridge should contain also (some) food not only beer !!')
        self.items = container
        self.name = 'Fridge'

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del self.items[key]

    def pop(self):
        pass

    def popitem(self):
        pass

    def clear(self):
        pass

    def update(self, other):
        self.items.update(other)

    def setdefault(self):
        pass

    def check_recipe(self, recipe):
        missing = list(recipe.items.keys() - self.items.keys())
        rest = list(set(recipe.items.keys()) - set(missing))
        return rest, missing


def check_the_fridge(fridge, recipes_box):
    the_list = []
    for recipe in recipes_box:
        counter = 0
        for ingredient in recipe:
            if ingredient in fridge:
                counter += 1
        if counter/len(recipe) > 0.5:
            the_list += [recipe.name]
    return the_list


def prepare_shopping_list(fridge, recipe):
    the_list = {}
    for ingredient in recipe:
        if ingredient in fridge:
            qty = recipe.items[ingredient] - fridge.items[ingredient]
            if qty > 0 :
                the_list.update({ingredient: qty})
        else:
            the_list.update({ingredient: recipe.items[ingredient]})
    return the_list


