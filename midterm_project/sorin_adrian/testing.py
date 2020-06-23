from midterm_project.sorin_adrian.shoppingList import Recipe, RecipesBox, Fridge, check_the_fridge
# prepare_shopping_list, shopping_list_archive
import unittest
from collections.abc import Collection


class TestRecipe(unittest.TestCase):

    def test_recipe_class_has_proper_atributes(self):
        # arange
        recipe_name = ''
        recipe_ingredients = ''
        # act
        test_recipe = Recipe(recipe_name, recipe_ingredients)
        # assert
        assert hasattr(test_recipe, 'recipe_name'), 'recipe_name missing from Recipe obj'
        assert hasattr(test_recipe, 'recipe_ingredients'), 'recipe_ingredients missing from Recipe obj'

    def test_recipe_class_atributes_type(self):
        # arange
        burger_title = "Beef Burger"
        burger_ingredients = {
            'bun': 1,
            'ground beef': 1,
            'ceedar cheese': 0.5,
            'onion': 2,
            'salad': 1,
            'smoked_sauce': 2
        }
        # act
        test_recipe = Recipe(burger_title, burger_ingredients)
        # assert
        assert isinstance(test_recipe.recipe_name, str), 'recipe_name is not the proper type'
        assert isinstance(test_recipe.recipe_ingredients, dict), 'recipe_ingredients is not the proper type'

    def test_recipe_instance_print(self):
        # arange
        burger_title = "Beef Burger"
        burger_ingredients = {
            'bun': 1,
            'ground beef': 1,
            'ceedar cheese': 0.5,
            'onion': 2,
            'salad': 1,
            'smoked_sauce': 2
        }
        # act
        test_recipe = Recipe(burger_title, burger_ingredients)
        # assert
        assert isinstance(test_recipe.__str__(), str), 'return of __str__ is not a string'

    def test_recipe_instance_lenght(self):
        # arange
        burger_title = "Beef Burger"
        burger_ingredients = {
            'bun': 1,
            'ground beef': 1,
            'ceedar cheese': 0.5,
            'onion': 2,
            'salad': 1,
            'smoked_sauce': 2
        }
        # act
        test_recipe = Recipe(burger_title, burger_ingredients)
        # assert
        assert len(test_recipe) == len(burger_ingredients), '__len__ method not working in the right way'

    def test_recipe_instance_contains_method(self):
        # arange
        burger_title = "Beef Burger"
        burger_ingredients = {
            'bun': 1,
            'ground beef': 1,
            'ceedar cheese': 0.5,
            'onion': 2,
            'salad': 1,
            'smoked_sauce': 2
        }
        ingredient = 'ground beef'
        # act
        test_recipe = Recipe(burger_title, burger_ingredients)
        # assert
        assert ingredient in test_recipe, '__contains__ method not working in the right way'

    def test_recipes_box_instance_type(self):
        # arange
        burger_title = "Beef Burger"
        burger_ingredients = {
            'bun': 1,
            'ground beef': 1,
            'ceedar cheese': 0.5,
            'onion': 2,
            'salad': 1,
            'smoked_sauce': 2
        }
        test_recipesbox = RecipesBox()
        # act
        test_recipe = Recipe(burger_title, burger_ingredients)
        test_recipesbox.append(test_recipe)
        # assert
        assert isinstance(test_recipesbox, Collection), 'test_recipesbox is not a Collection'

    def test_recipes_box_instance_append_method(self):
        # arange
        burger_title = "Beef Burger"
        burger_ingredients = {
            'bun': 1,
            'ground beef': 1,
            'ceedar cheese': 0.5,
            'onion': 2,
            'salad': 1,
            'smoked_sauce': 2
        }
        test_recipesbox = RecipesBox()
        # act
        test_recipe = Recipe(burger_title, burger_ingredients)
        test_recipesbox.append(test_recipe)
        # assert
        assert test_recipe in test_recipesbox, 'append method does not work properly'

    def test_recipes_box_instance_pick_method(self):
        # arange
        burger_title = "Beef Burger"
        burger_ingredients = {
            'bun': 1,
            'ground beef': 1,
            'ceedar cheese': 0.5,
            'onion': 2,
            'salad': 1,
            'smoked_sauce': 2
        }
        test_recipesbox = RecipesBox()
        # act
        test_recipe = Recipe(burger_title, burger_ingredients)
        test_recipesbox.append(test_recipe)
        test_pick = test_recipesbox.pick(test_recipe)
        # assert
        assert test_pick == test_recipe, 'pick methode does not work properly'

    def test_fridge_instance_update_and_contains_methods(self):
        # arange
        susage = {'sausage': 5}
        poatato = {'potato': 10}
        egg = {'egg': 25}
        test_fridge = Fridge()
        # act
        test_fridge.update(susage)
        test_fridge.update(poatato)
        test_fridge.update(egg)
        test_fridge.update_quantity('sausage', 30)
        test_fridge.update_quantity('potato', -15)
        sausage_quantity = 35
        # assert
        assert 'egg' in test_fridge, 'update method does not work properly'
        assert sausage_quantity == test_fridge['sausage'], 'update_quantity method does not work properly'
        assert 'potato' not in test_fridge, 'update_quantity method does not work properly'

    def test_fridge_instance_check_recipes_method(self):
        # arange
        burger_title = "Beef Burger"
        burger_ingredients = {
            'bun': 1,
            'ground_beef': 1,
            'ceedar_cheese': 0.5,
            'onion': 2,
            'salad': 1,
            'smoked_sauce': 2
        }
        bun = {'bun': 5}
        onion = {'onion': 10}
        salad = {'salad': 25}
        test_fridge = Fridge()
        ingred_in = {'bun', 'onion', 'salad'}
        ingred_off = {'ground_beef', 'ceedar_cheese', 'smoked_sauce'}
        # act
        test_recipe = Recipe(burger_title, burger_ingredients)
        test_fridge.update(bun)
        test_fridge.update(onion)
        test_fridge.update(salad)
        test_ingreds_in, test_ingreds_off = test_fridge.check_recipe(test_recipe)
        # assert
        assert test_ingreds_in == ingred_in, 'check_recipes method does not work properly'
        assert test_ingreds_off == ingred_off, 'check_recipes method does not work properly'

    def test_check_the_fridge_function(self):
        # arange
        burger_title = "Beef Burger"
        hot_dog_tile = 'Hot Dog'
        burger_ingredients = {
            'bun': 1,
            'ground_beef': 1,
            'ceedar_cheese': 0.5,
            'onion': 2,
            'salad': 1,
            'smoked_sauce': 2
        }
        hot_dog_ingredients = {
            'bun': 1,
            'sausage': 1,
            'mustard': 0.5,
            'ketchup': 0.5
        }
        bun = {'bun': 5}
        onion = {'onion': 10}
        salad = {'salad': 25}
        mustard = {'mustard': 15}
        test_fridge = Fridge()
        test_recipesbox = RecipesBox()
        # act
        test_burger_recipe = Recipe(burger_title, burger_ingredients)
        test_hot_dog_recipe = Recipe(hot_dog_tile, hot_dog_ingredients)
        test_fridge.update(bun)
        test_fridge.update(onion)
        test_fridge.update(salad)
        test_fridge.update(mustard)
        test_recipesbox.append(test_hot_dog_recipe)
        test_recipesbox.append(test_burger_recipe)
        test_check_the_fridge_result = check_the_fridge(test_fridge, test_recipesbox).sort()
        refrence_results = ['Beef Burger', 'Hot Dog'].sort()
        # assert
        assert test_check_the_fridge_result == refrence_results, 'function check_the_ridge not working prprely'


if __name__ == '__main__':
    unittest.main()
