# Midterm project


### We will build an application that will help us make the shopping list for our
favourite recipes!


##### We will start with a **mapping** that will help us describe a recipe:


```python
class Recipe(...):
    ...

```

A new recipe can be created starting from a name and dictionary of ingredients and quantities.


```python
mac_and_cheese_ingredients = {
    'macaroni': 1,
    'cheese': 0.5
}

mac_and_cheese = Recipe(
    "Famous Mac & Cheese",
    mac_and_cheese_ingredients
)

print(mac_and_cheese)
```

```
***********************
 Famous Mac & Cheese
***********************

1. Macaroni: 1
2. Cheese: 0.5


***********************
```

```python
ingredients = list(mac_and_cheese.keys())
```

Once a recipe has been created, it cannot be updated.

##### We will also have a RecipesBox that is a **mutable sequence** that holds our recipes.

```python
class RecipesBox(...):
    ...
    
    def pick(self, name=None):
        pass

```

We can add one by one a new recipe in the recipes box and, using the *pick* method we cat extract a recipe by name 
or get a random recipe from the recipe box.

We can add and delete recipes from the recipes box.

When printing the recipes box (using Python's builtin method **print**), the list of recipes 
(names only) is listed.


##### We also have a fridge that's a **mutable mapping** that holds some products together 
with their quantities.

```python
class Fridge(...):
    ...
    
    def check_recipe(self, recipe):
        ...
```
    
When printing the fridge object, it will print similar to a recipe, its contents.

We can also ask if a certain product is in the fridge.  

```python
if 'milk' in fridge:
    print('yap')
```

We can add new items in the fridge or remove existing ones. We can also update the quantities 
for the items present in the fridge. 
When we alter the quantity for an item and that becomes 0, we should get a notification 
that the product will be removed completely from the fridge.

We can use the **check_recipe** method to see if we have all the required ingredients 
from a recipe. This method will return two lists: 
one with the items from the recipe that we have in the fridge, and another one with 
the ones that we don't.

##### We will have a mixin class called **PrittyPrinter** that will be used by 
**Fridge** and **Recipe** to print nicely their contents.

```python
class PrittyPrinter:
    ...
    
```

##### We will also two functions called **check_the_fridge** and **prepare_shopping_list**

```python
def check_the_fridge(fridge, recipes_box):
    ...
    
```

The function **check_the_fridge** will look in the fridge and give us a list of recipes 
(names only) for which we have some of the ingredients required (min. 50% of the ingredients 
- check only the ingredient's presence but not the quantity)

```python
def prepare_shopping_list(fridge, recipe):
    ...
    
```

The function **prepare_shopping_list** will take a recipe, and based on the items we have 
in the fridge, 
will return a dictionary with the items that we have to buy and the corresponding quantities. 
This method will check ingredients by presence and quantity and compute the missing quantity 
that will be added to the shopping list.

For the function **prepare_shopping_list** we will have two decorators:
* **pretty_print_recipe**: this decorator will take the returned values from the 
**prepare_shopping_list** and will print a nice representation of the 
shopping list;

* **archive_shopping_list**: will take the returned shopping list and add 
it to a list called **shopping_list_archive** that resides in the global scope.

You can have fun with the **pretty_print_recipe** decorator and be creative with 
the shopping list representation; 
you can also use [ascii art](https://www.asciiart.eu/art-and-design/borders) 
to make it more fun, but this is not mandatory.

```
                     ,---.           ,---.
                    / /"`.\.--"""--./,'"\ \
                    \ \    _       _    / /
                     `./  / __   __ \  \,'
                      /    /_O)_(_O\    \
                      |  .-'  ___  `-.  |
                   .--|       \_/       |--.
                 ,'    \   \   |   /   /    `.
                /       `.  `--^--'  ,'       \
             .-"""""-.    `--.___.--'     .-"""""-.
.-----------/         \------------------/         \--------------.
| .---------\         /----------------- \         /------------. |
| |          `-`--`--'                    `--'--'-'             | |
| |                    Shopping list:                           | |
| |                                                             | |
| |                                                             | |
| |  1. Milk: 1                                                 | |
| |  2. Eggs: 5                                                 | |
| |                                                             | |
| |                                                             | |
| |                                                             | |
| |                                                             | |
| |                                                             | |
| |                                                             | |
| |                                                             | |
| |_____________________________________________________________| |
|_________________________________________________________________|
                   )__________|__|__________(
                  |            ||            |
                  |____________||____________|
                    ),-----.(      ),-----.(
                  ,'   ==.   \    /  .==    `.
                 /            )  (            \
                 `==========='    `==========='
```



**Important!** For each component that we build we have to add use cases and some tests to showcase the functionality and test that it meets all the requirements. We will organize our code as follows: in one file called **shopping_list.py** we will keep all our classes and methods and in another one, called **playground.py** we will have the tests and the showcasing.
f
The showcase will have at least 5 recipes with a minimum of 4 ingredients and 5 five items in the fridge. We will have to fully exhibit each component's functionality.


#### Submission deadline: Saturday 16 May 2020, 23.00

#### Teams:

> Alexandru Turcu
> 
> Ilas Lorena


> Alexandru Roman
> 
> Marius Dragla


> Mihai Farcas
>
> Edmond Sabou


> Razvan Zoldi
> 
> Victor Pop


> Vlad Butulan
>
> Cristian Zaganeanu


> Vaida Mihaela
> 
> Bianca Daniela Bucur


> Sorin Mosut
> 
> Adrian Filimon
