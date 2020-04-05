# HobbyShop
# Requirements:
# Have at least 400 articles in the shop
# Have at least four types of articles (shirt, scarf, glove, heat)
# Have at least five sizes (S M L XL XXL) for each type of article
# To be able to sell the latest article that was added to the shop
# To be able to sell any item that is in the shop
# To restock the shop with new items

# define empty list to put all articles
shop = []

# define different list to have more flexibility when adding or removing from them
type_list = ['shirt', 'scarf', 'glove', 'hat']
size_list = ['S', 'M', 'L', 'XL', 'XXL']
color_list = ['blue', 'red', 'green', 'yellow', 'black']
item_number_list = range(4)

# loop into types of articles (5)
for x in type_list:
    # loop into size of articles (4 x 5 = 20)
    for y in size_list:
        # loop into color of articles (5 x 20 = 100)
        for z in color_list:
            # create 4 articles of each type (4 x 100 = 400)
            for t in item_number_list:
                # add articles
                shop.append((x, y, z))

# check how many articles we have in shop list
print(f'Total number of articles we (still) have {len(shop)}')

# add empty row so output to be easy to read
print('              ')

item_to_search = None
item_1_1 = shop[-1][0]
item_1_2 = shop[-1][1]
item_1_3 = shop[-1][2]


# add CHECK ITEM FUNCTION
def check_item(item_to_search):
    if shop.count(item_to_search) > 0:
        print(f'We (still) have {shop.count(item_to_search)} x {item_1_1}, {item_1_2}, {item_1_3} on stock')
    else:
        print(f'There is no {item_to_search} on the stock. Please restock')


def QuestionOne():
    # check (search) if some item is in list; let user choose what is searching for
    print('What article are you searching for?')
    for number, item in enumerate(type_list):
        print(f'{number + 1}: {item}')


def QuestionTwo():
    print('What size you are searching for?')
    for number, item in enumerate(size_list):
        print(f'{number + 1}: {item}')


def QuestionThree():
    print('What color you are searching for?')
    for number, item in enumerate(color_list):
        print(f'{number + 1}: {item}')


def QuestionZero():
    # check (and sell?) last article from shop list
    print(f'Last item in stock is type: {shop[-1][0]}, size: {shop[-1][1]} and color: {shop[-1][2]}.')
    print('              ')
    print('Do you want to sell this one? (y/Y or n/N): ')


def main():
    global item_1_3, item_1_2, item_1_1, item_to_search
    QuestionZero()
    question_zero_input = str.upper(input())
    if question_zero_input == 'Y':
        no_of_items_to_sell = int(
            input(f'How many {item_1_1}, size {item_1_2} and color {item_1_3} do you want to sell: '))
        item_to_search = (item_1_1, item_1_2, item_1_3)
        for t in range(no_of_items_to_sell):
            shop.pop()
        # print(len(shop))
    elif question_zero_input == 'N':
        QuestionOne()
        question_one_input = int(input())
        if question_one_input == 1:
            item_1_1 = 'shirt'
        if question_one_input == 2:
            item_1_1 = 'scarf'
        if question_one_input == 3:
            item_1_1 = 'glove'
        if question_one_input == 4:
            item_1_1 = 'hat'
        if question_one_input != 1 and question_one_input != 2 and question_one_input != 3 and question_one_input != 4:
            print("Please select one answer from list. Let's do it again")
            main()
        QuestionTwo()
        question_two_input = int(input())
        if question_two_input == 1:
            item_1_2 = 'S'
        if question_two_input == 2:
            item_1_2 = 'M'
        if question_two_input == 3:
            item_1_2 = 'L'
        if question_two_input == 4:
            item_1_2 = 'XL'
        if question_two_input == 5:
            item_1_2 = 'XXL'
        if question_two_input != 1 and question_two_input != 2 and question_two_input != 3 and question_two_input != 4 and question_two_input != 5:
            print("Please select one answer from list. Let's do it again !")
            main()
        QuestionThree()
        question_three_input = int(input())
        if question_three_input == 1:
            item_1_3 = 'blue'
        if question_three_input == 2:
            item_1_3 = 'red'
        if question_three_input == 3:
            item_1_3 = 'green'
        if question_three_input == 4:
            item_1_3 = 'yellow'
        if question_three_input == 5:
            item_1_3 = 'black'
        if question_three_input != 1 and question_three_input != 2 and question_three_input != 3 and question_three_input != 4 and question_three_input != 5:
            print("Please select one answer from list. Let's do it again !")
            main()

        item_to_search = (item_1_1, item_1_2, item_1_3)
        print(f'You are searching for {item_1_1}, {item_1_2}, {item_1_3}. We have {shop.count(item_to_search)} items '
              f'on stock')
        # sell the previous checked item and check how many item we still have in shop
        print('              ')
        no_of_items_to_sell = int(
            input(f'How many {item_1_1}, size {item_1_2} and color {item_1_3} do you want to sell: '))
        print('              ')

        for X in range(no_of_items_to_sell):
            if 0 <= no_of_items_to_sell <= 4:
                shop.remove(item_to_search)
            elif no_of_items_to_sell == 0:
                print("You do not want to sell? Let's do it again !")
                main()
            elif no_of_items_to_sell > 4:
                print("You request more than we have on stock")
    elif question_zero_input != 'Y' and question_zero_input != 'N':
        print("Please select one answer from list. Let's do it again !")
        main()
main()

# add empty row so output to be easy to read
print('              ')

check_item(item_to_search)

# add empty row so output to be easy to read
print('              ')


# restock with previous sell item1

def restock(Y):
    if shop.count(Y) == 4:
        print(f'We still have {shop.count(Y)} x {Y} on stock')
        # add empty row to be readable
        print('              ')
    else:
        if shop.count(Y) == 0:
            for t in range(4):
                shop.append(Y)
            print(f'We restock with 4 x {Y} ')
            print('                 ')
        elif shop.count(Y) == 1:
            for t in range(3):
                shop.append(Y)
            print(f'We restock with 3 x {Y} ')
            print('                  ')
        elif shop.count(Y) == 2:
            for t in range(2):
                shop.append(Y)
            print(f'We restock with 2 x {Y} ')
            print('                  ')
        elif shop.count(Y) == 3:
            for t in range(1):
                shop.append(Y)
            print(f'We restock with 1 x {Y} ')
            print('                   ')


restock(item_to_search)
print('     ')

print(f'Total number of articles we (still) have {len(shop)}. Back in business !')
