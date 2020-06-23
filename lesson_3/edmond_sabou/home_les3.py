# HOBBY SHOP
# shirts = [("shirt", "S"), ("shirt", "M"), ("shirt", "L"), ("shirt", "XL"), ("shirt", "XXL")]

# article_shirts = ["shirt"]
# shirts_sizes = ["S", "M", "L", "XL", "XXL"]
# all_shirts = []

import sys

##### CREATE A FULL STOCK FROM ZERO

shirts = [(shirt, sizes) for shirt in ["Shirt"] for sizes in ["S", "M", "L", "XL", "XXL"] * 4]
scarfs = [(scarf, sizes) for scarf in ["Scarf"] for sizes in ["S", "M", "L", "XL", "XXL"] * 4]
gloves = [(gloves, sizes) for gloves in ["Gloves"] for sizes in ["S", "M", "L", "XL", "XXL"] * 4]
heats = [(heat, sizes) for heat in ["Heats"] for sizes in ["S", "M", "L", "XL", "XXL"] * 4]


### MAIN MENU

def mainMenu():
    """This is where the fun starts."""

    print("\n### WELCOME TO THE HOBBY SHOP ###")
    print("\nWhat do you wish to do?\n")
    print("1. Buy something")
    print("2. Add item to the list")
    print("3. View list")
    print("4. Nothing/Quit")
    answer = input("\nAnswer: ")
    if answer > "0" and not answer > "4":
        if answer == "1":
            buySomething()
        elif answer == "2":
            addItem()
        elif answer == "3":
            viewList()
        elif answer == "4":
            quit()
        else:
            mainMenu()
    else:
        print("\n##### Invalid input, choose between 1 -> 4. Thanks! #####")
        mainMenu()


##### BUY SHIRTS MENU
def buySomething():
    """Basically a menu for the BUY screen."""

    print("\nWhat item type do you wish to buy?")
    print("1. Shirts")
    print("2. Scarfs")
    print("3. Gloves")
    print("4. Heats")
    print("\n5. Go Back")
    answer = input("\nItem: ")
    if answer > "0" and not answer > "5":
        if answer == "1":
            buyShirts()
        elif answer == "2":
            buyScarfs()
        elif answer == "3":
            buyGloves()
        elif answer == "4":
            buyHeats()
        else:
            mainMenu()
    else:
        print("\n##### Invalid input, choose between 1 -> 4. Thanks! #####")
        buySomething()


### FOR BUYING SHIRTS

def buyShirts():
    """You buy shirts based on size and remove them from the stock."""

    print("\nYou have", len(shirts), "shirts available to purchase")
    print("\nWhat size you wish to buy?")
    print("\nSizes: ")
    print("S")
    print("M")
    print("L")
    print("XL")
    print("XXL")
    answer_shirt_size = input("\nSize: ")

    if answer_shirt_size.upper() == "S":
        if shirts.count(("Shirt", "S")) > 0:  ##### VALIDATE IF YOU HAVE ENOUGH STOCK FIRST!!!
            shirts.remove(("Shirt", "S"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Shirt, size S")
        print("\nThere are ", (shirts.count(("Shirt", "S"))), " Shirts size S remaining")
        anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
        else:
            mainMenu()

    elif answer_shirt_size.upper() == "M":
        if shirts.count(("Shirt", "M")) > 0:
            shirts.remove(("Shirt", "M"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your shirt Shirt, size M")
        print("\nThere are ", (shirts.count(("Shirt", "M"))), " Shirts size M remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_shirt_size.upper() == "L":
        if shirts.count(("Shirt", "L")) > 0:
            shirts.remove(("Shirt", "L"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your shirt Shirt, size L")
        print("\nThere are ", (shirts.count(("Shirt", "L"))), " Shirts size L remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_shirt_size.upper() == "XL":
        if shirts.count(("Shirt", "XL")) > 0:
            shirts.remove(("Shirt", "XL"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your shirt Shirt, size XL")
        print("\nThere are ", (shirts.count(("Shirt", "XL"))), " Shirts size XL remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_shirt_size.upper() == "XXL":
        if shirts.count(("Shirt", "XXL")) > 0:
            shirts.remove(("Shirt", "XXL"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your shirt Shirt, size XXL")
        print("\nThere are ", (shirts.count(("Shirt", "XXL"))), " Shirts size XXL remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()
    else:
        print("\n##### Invalid input, choose between S, M, L, XL, XXL. Thanks! #####")
        buyShirts()


def buyScarfs():
    """Same as shirts, only different"""

    print("\nYou have", len(scarfs), "scarfs available to purchase")
    print("\nWhat size you wish to buy?")
    print("\nSizes: ")
    print("S")
    print("M")
    print("L")
    print("XL")
    print("XXL")
    answer_scarf_size = input("\nSize: ")

    # CHOOSE SIZE AND REMOVE ITEM BASED ON SIZE
    if answer_scarf_size.upper() == "S":
        if scarfs.count(("Scarf", "S")) > 0:
            scarfs.remove(("Scarf", "S"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your scarf, size S")
        print("\nThere are ", (scarfs.count(("Scarf", "S"))), " scarfs size S remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_scarf_size.upper() == "M":
        if scarfs.count(("Scarf", "M")) > 0:
            scarfs.remove(("Scarf", "M"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your scarf, size M")
        print("\nThere are ", (scarfs.count(("Scarf", "M"))), " scarfs size M remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            sys.exit()

    elif answer_scarf_size.upper() == "L":
        if scarfs.count(("Scarf", "L")) > 0:
            scarfs.remove(("Scarf", "L"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your scarf scarf, size L")
        print("\nThere are ", (scarfs.count(("Scarf", "L"))), " scarfs size L remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_scarf_size.upper() == "XL":
        if scarfs.count(("Scarf", "XL")) > 0:
            scarfs.remove(("Scarf", "XL"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your scarf scarf, size XL")
        print("\nThere are ", (scarfs.count(("Scarf", "XL"))), " scarfs size XL remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_scarf_size.upper() == "XXL":
        if scarfs.count(("Scarf", "XXL")) > 0:
            scarfs.remove(("Scarf", "XXL"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your scarf scarf, size XXL")
        print("\nThere are ", (scarfs.count(("Scarf", "XXL"))), " scarfs size XXL remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()
    else:
        print("\n##### Invalid input, choose between S, M, L, XL, XXL. Thanks! #####")
        buyScarfs()


def buyGloves():
    """Same as shirts, only different"""

    print("\nYou have", len(gloves), "gloves available to purchase")
    print("\nWhat size you wish to buy?")
    print("\nSizes: ")
    print("S")
    print("M")
    print("L")
    print("XL")
    print("XXL")
    answer_gloves_size = input("\nSize: ")

    if answer_gloves_size.upper() == "S":
        if gloves.count(("Gloves", "S")) > 0:
            gloves.remove(("Gloves", "S"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Gloves, size S")
        print("\nThere are ", (gloves.count(("Gloves", "S"))), " gloves size S remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_gloves_size.upper() == "M":
        if gloves.count(("Gloves", "M")) > 0:
            gloves.remove(("Gloves", "M"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Gloves, size M")
        print("\nThere are ", (gloves.count(("Gloves", "M"))), " gloves size M remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_gloves_size.upper() == "L":
        if gloves.count(("Gloves", "L")) > 0:
            gloves.remove(("Gloves", "L"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Gloves, size L")
        print("\nThere are ", (gloves.count(("Gloves", "L"))), " gloves size L remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_gloves_size.upper() == "XL":
        if gloves.count(("Gloves", "XL")) > 0:
            gloves.remove(("Gloves", "XL"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Gloves, size XL")
        print("\nThere are ", (gloves.count(("Gloves", "XL"))), " gloves size XL remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_gloves_size.upper() == "XXL":
        if gloves.count(("Gloves", "XXL")) > 0:
            gloves.remove(("Gloves", "XXL"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Gloves, size XXL")
        print("\nThere are ", (gloves.count(("Gloves", "XXL"))), " gloves size XXL remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()
    else:
        print("\n##### Invalid input, choose between S, M, L, XL, XXL. Thanks! #####")
        buyGloves()


def buyHeats():
    """Same as shirts, only different"""

    print("\nYou have", len(heats), "heats available to purchase")
    print("\nWhat size you wish to buy?")
    print("\nSizes: ")
    print("S")
    print("M")
    print("L")
    print("XL")
    print("XXL")
    answer_heats_size = input("\nSize: ")

    if answer_heats_size.upper() == "S":
        if gloves.count(("Heats", "S")) > 0:
            gloves.remove(("Heats", "S"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Heats, size S")
        print("\nThere are ", (heats.count(("Heats", "S"))), " heats size S remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_heats_size.upper() == "M":
        if gloves.count(("Heats", "M")) > 0:
            gloves.remove(("Heats", "M"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Heats, size M")
        print("\nThere are ", (heats.count(("Heats", "M"))), " heats size M remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_heats_size.upper() == "L":
        if gloves.count(("Heats", "L")) > 0:
            gloves.remove(("Heats", "L"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Heats, size L")
        print("\nThere are ", (heats.count(("Heats", "L"))), " heats size L remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_heats_size.upper() == "XL":
        if gloves.count(("Heats", "XL")) > 0:
            gloves.remove(("Heats", "XL"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Heats, size XL")
        print("\nThere are ", (heats.count(("Heats", "XL"))), " heats size XL remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()

    elif answer_heats_size.upper() == "XXL":
        if gloves.count(("Heats", "XXL")) > 0:
            gloves.remove(("Heats", "XXL"))
        else:
            print("There are no more items remaining in stock.")
            anotherBuy = input("\nDo you wish to make another buy? Yes/No ")
            if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
                buySomething()  # ANOTHER HANDLING FOR WRONG ANSWER
            else:
                mainMenu()
        print("\nCongratulations for your Heats, size XXL")
        print("\nThere are ", (heats.count(("Heats", "XXL"))), " heats size XXL remaining")
        anotherBuy = input("\nDo you wish to make another buy? ")
        if anotherBuy.lower() == "yes" or anotherBuy.lower() == "y" or anotherBuy.lower() == "ye":
            buySomething()
        else:
            mainMenu()
    else:
        print("\n##### Invalid input, choose between S, M, L, XL, XXL. Thanks! #####")
        buyHeats()


def addItem():
    """This is a long one. Unfortunately I could not find a way to make this shorter but basically it adds an additional
    item to the end of the desired list"""

    print("\nWhat do you wish to restock?\n")
    print("1. Shirt")
    print("2. Scarf")
    print("3. Gloves")
    print("4. Heats")
    print("\n5. Go back")
    answer = input("\nAnswer: ")
    if answer > "0" and not answer > "5":
        if answer == "1":
            size = input("\nWhat size? ")
            if size.upper() == "S":
                shirts.append(("Shirt", "S"))
                print("\nShirt added!")
                addItem()
            if size.upper() == "M":
                shirts.append(("Shirt", "M"))
                print("\nShirt added!")
                addItem()
            if size.upper() == "L":
                shirts.append(("Shirt", "L"))
                print("\nShirt added!")
                addItem()
            if size.upper() == "XL":
                shirts.append(("Shirt", "XL"))
                print("\nShirt added!")
                addItem()
            if size.upper() == "XXL":
                shirts.append(("Shirt", "XXL"))
                print("\nShirt added!")
                addItem()

        if answer == "2":
            size = input("\nWhat size? ")
            if size.upper() == "S":
                shirts.append(("Scarf", "S"))
                print("\nScarf added!")
                addItem()
            if size.upper() == "M":
                shirts.append(("Scarf", "M"))
                print("\nScarf added!")
                addItem()
            if size.upper() == "L":
                shirts.append(("Scarf", "L"))
                print("\nScarf added!")
                addItem()
            if size.upper() == "XL":
                shirts.append(("Scarf", "XL"))
                print("\nScarf added!")
                addItem()
            if size.upper() == "XXL":
                shirts.append(("Scarf", "XXL"))
                print("\nScarf added!")
                addItem()

        if answer == "3":
            size = input("\nWhat size? ")
            if size.upper() == "S":
                shirts.append(("Gloves", "S"))
                print("\nGloves added!")
                addItem()
            if size.upper() == "M":
                shirts.append(("Gloves", "M"))
                print("\nGloves added!")
                addItem()
            if size.upper() == "L":
                shirts.append(("Gloves", "L"))
                print("\nGloves added!")
                addItem()
            if size.upper() == "XL":
                shirts.append(("Gloves", "XL"))
                print("\nGloves added!")
                addItem()
            if size.upper() == "XXL":
                shirts.append(("Gloves", "XXL"))
                print("\nGloves added!")
                addItem()

        if answer == "4":
            size = input("\nWhat size? ")
            if size.upper() == "S":
                shirts.append(("Heats", "S"))
                print("\nHeats added!")
                addItem()
            if size.upper() == "M":
                shirts.append(("Heats", "M"))
                print("\nHeats added!")
                addItem()
            if size.upper() == "L":
                shirts.append(("Heats", "L"))
                print("\nHeats added!")
                addItem()
            if size.upper() == "XL":
                shirts.append(("Heats", "XL"))
                print("\nHeats added!")
                addItem()
            if size.upper() == "XXL":
                shirts.append(("Heats", "XXL"))
                print("\nHeats added!")
                addItem()
        if answer == "5":
            mainMenu()
    else:
        print("\n##### Invalid input, choose between 1 --> 5. Thanks! #####")
        addItem()


# make it more user friendly and display the list in a more compact way. e.g.: Shirt, S -- 5 items; Gloves, M -- 2
def viewList():
    """Here you just view the existing list. When the program is launched the stock is always full. Luckily while the
    program is running stock is remembered"""

    print("\nWhich products you wish to browse through?")
    print("1. Shirts")
    print("2. Scarfs ")
    print("3. Gloves")
    print("4. Heats")
    print("\n5. Go back")
    answer = input("\nAnswer: ")
    if answer > "0" and not answer > "5":
        if answer == "1":
            print("\nShirt, size S --> ", shirts.count(("Shirt", "S")), "samples")
            print("Shirt, size M --> ", shirts.count(("Shirt", "M")), "samples")
            print("Shirt, size L --> ", shirts.count(("Shirt", "L")), "samples")
            print("Shirt, size XL --> ", shirts.count(("Shirt", "XL")), "samples")
            print("Shirt, size XXL --> ", shirts.count(("Shirt", "XXL")), "samples")
            print("\nViewing, ", len(shirts), "items total.")
            input("\nPress ANY key to go Back.")
            viewList()
        elif answer == "2":
            print("\nScarf, size S --> ", scarfs.count(("Scarf", "S")), "samples")
            print("Scarf, size M --> ", scarfs.count(("Scarf", "M")), "samples")
            print("Scarf, size L --> ", scarfs.count(("Scarf", "L")), "samples")
            print("Scarf, size XL --> ", scarfs.count(("Scarf", "XL")), "samples")
            print("Scarf, size XXL --> ", scarfs.count(("Scarf", "XXL")), "samples")
            print("\nViewing, ", len(scarfs), "items total.")
            input("\nPress ANY key to go Back")
            viewList()
        elif answer == "3":
            print("\nGloves, size S --> ", gloves.count(("Gloves", "S")), "samples")
            print("Gloves, size M --> ", gloves.count(("Gloves", "M")), "samples")
            print("Gloves, size L --> ", gloves.count(("Gloves", "L")), "samples")
            print("Gloves, size XL --> ", gloves.count(("Gloves", "XL")), "samples")
            print("Gloves, size XXL --> ", gloves.count(("Gloves", "XXL")), "samples")
            print("\nViewing, ", len(gloves), "items total.")
            input("\nPress ANY key to go Back.")
            viewList()
        elif answer == "4":
            print("\nHeats, size S --> ", heats.count(("Heats", "S")), "samples")
            print("Heats, size M --> ", heats.count(("Heats", "M")), "samples")
            print("Heats, size L --> ", heats.count(("Heats", "L")), "samples")
            print("Heats, size XL --> ", heats.count(("Heats", "XL")), "samples")
            print("Heats, size XXL --> ", heats.count(("Heats", "XXL")), "samples")
            print("\nViewing, ", len(heats), "items total.")
            input("\nPress ANY key to go Back.")
            viewList()
        elif answer == "5":
            mainMenu()
    else:
        print("\n##### Invalid input, choose between 1 --> 5. Thanks! #####")
        viewList()


def quit():
    """Just do it!"""
    print("\nThank you for visiting the SHOP!")
    sys.exit()


mainMenu()
buySomething()
buyShirts()
buyScarfs()
buyGloves()
buyHeats()
