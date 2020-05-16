import unittest
from midterm_project.project_mihaela_bianca.playground import *
from midterm_project.project_mihaela_bianca.shopping_list import *


class Test_Recipe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start testing!')

    @classmethod
    def tearDownClass(cls):
        print('End testing!')

    def setUp(self) -> None:
        self.mac_and_cheese = Recipe('Mac and cheese', {'macaroni': 3, 'egg': 3, 'milk': 0.5, 'cheese': 1, 'sugar': 3})
        self.banana_bread = Recipe('Banana bread',
                                   {'flour': 1, 'yogourt': 1, 'banana': 2, 'honey': 1, 'cocoa': 1, 'sugar': 1})

    def tearDown(self) -> None:
        mac_and_cheese.display()
        banana_bread.display()

    def test_recipe_init(self):
        banana_bread = Recipe('Banana bread',
                              {'flour': 1, 'yogourt': 1, 'banana': 2, 'honey': 1, 'cocoa': 1, 'sugar': 1})

        self.assertIsInstance(banana_bread, Recipe)

    def test_recipe_has_attributes(self):
        name = 'Banana bread'
        ingredients = {'flour': 1, 'yogourt': 1, 'banana': 2, 'honey': 1, 'cocoa': 1, 'sugar': 1}
        banana_bread = Recipe(name, ingredients)
        assert hasattr(banana_bread, 'name'), 'Recipe is missing name attribute!'
        assert hasattr(banana_bread, 'ingredients'), 'Recipe is missing ingredients attribute!'


class Test_RecipesBox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start testing!')

    @classmethod
    def tearDownClass(cls):
        print('End testing!')

    def test_recipesbox_init(self):
        recipe = [fries, cheesecake, banana_bread, home_made_chocolate, mac_and_cheese]
        recipesbox = RecipesBox(recipe)
        assert hasattr(recipesbox, 'recipe'), 'Recipesbox has no recipe attributes'

    def test_pick_named_recipe(self):
        fries = Recipe('Fries', {'potato': 1, 'oil': 1, 'salt': 1, 'cheese': 1})
        recipesbox = RecipesBox([fries, cheesecake, banana_bread])
        fries = recipesbox.pick(fries)
        assert isinstance(fries, Recipe)

    # def test_pick_random_recipe(self):
    #     recipesbox = RecipesBox([fries, cheesecake, banana_bread])
    #     random_recipe = recipesbox.pick()
    #     if random_recipe in recipesbox.recipe:
    #         assert isinstance(random_recipe, Recipe)


class Test_Fridge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start testing!')

    @classmethod
    def tearDownClass(cls):
        print('End testing!')

    def test_fridge_init(self):
        ingredients = {'milk': 4, 'potato': 3, 'egg': 2,
                       'banana': 10, 'sugar': 3, 'macaroni': 2, 'cocoa': 2}
        fridge = Fridge(ingredients)
        assert isinstance(fridge, Fridge)
        assert hasattr(fridge, 'ingredients'), \
            'Ingredients attribute is missing!'

    def test_check_ingredient(self):
        ingredients = {'milk': 4, 'potato': 3, 'egg': 2,
                       'banana': 10, 'sugar': 3, 'macaroni': 2, 'cocoa': 2}
        fridge = Fridge(ingredients)

        self.assertEqual(fridge.check_ingredient('milk'), 'Yes')
        self.assertEqual(fridge.check_ingredient('white chocolate'), 'Nope')

    def test_check_recipe(self):
        ingredients = {'milk': 4, 'potato': 3, 'egg': 2,
                       'banana': 10, 'sugar': 3, 'macaroni': 2, 'cocoa': 2}
        fridge = Fridge(ingredients)
        fries = Recipe('Fries', {'potato': 1, 'oil': 1, 'salt': 1, 'cheese': 1})

        self.assertEqual(fridge.check_recipe(fries), 'The recipe cannot be prepared!')


class Test_IndependentFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start testing!')

    @classmethod
    def tearDownClass(cls):
        print('End testing!')

    def test_check_the_fridge(self):
        mac_and_cheese = Recipe('Mac and cheese', {'macaroni': 3, 'egg': 3, 'milk': 0.5, 'cheese': 1, 'sugar': 3})

        cheesecake = Recipe('Cheesecake', {'flour': 1, 'milk': 1, 'egg': 3, 'cocoa': 1, 'sugar': 1, 'strawberry': 2})

        banana_bread = Recipe('Banana bread',
                              {'flour': 1, 'yogourt': 1, 'banana': 2, 'honey': 1, 'cocoa': 1, 'sugar': 1})
        fries = Recipe('Fries', {'potato': 1, 'oil': 1, 'salt': 1, 'cheese': 1})

        home_made_chocolate = Recipe('Home made chocolate', {'milk': 2, 'cocoa': 1, 'sugar': 2, 'vanilla': 1, 'nut': 1})

        ingredients = {'milk': 4, 'potato': 3, 'egg': 2,
                       'banana': 10, 'sugar': 3, 'macaroni': 2, 'cocoa': 2}
        fridge= Fridge(ingredients)
        recipesbox=recipesbox = RecipesBox(fries, cheesecake, banana_bread, home_made_chocolate, mac_and_cheese)
        self.assertNotIsInstance(check_the_fridge(fridge,recipesbox),list)

    def test_prepare_shopping_list(self):
        mac_and_cheese = Recipe('Mac and cheese', {'macaroni': 3, 'egg': 3, 'milk': 0.5, 'cheese': 1, 'sugar': 3})
        ingredients = {'milk': 4, 'potato': 3, 'egg': 2,
                       'banana': 10, 'sugar': 3, 'macaroni': 2, 'cocoa': 2}
        fridge = Fridge(ingredients)
        self.assertNotIsInstance(prepare_shopping_list(fridge,mac_and_cheese), dict)



if __name__ == '__main__':
    unittest.main(verbosity=2)
