import random
import logging

from contextlib import contextmanager
import pprint

pp = pprint.PrettyPrinter(indent=4)
logger = logging.getLogger(__name__)

__header = r'''
   ____________________________________
 / \                                   \.
|   |                                   |.
 \_ |                                   |.
    |                                   |.
'''
__footer = r'''
    |                                   |.
    |   _______________________________ |___
    |  /                                 /.
    \_/_________________________________/.
'''


class WellDisplayMixin:

    def __str__(self):
        dash = '*' * 40
        if hasattr(self, 'name'):
            header_name = '{} for {}'.format(self.__class__.__name__, self.name)
        else:
            header_name = self.__class__.__name__

        header = '{} :'.format(header_name)

        result = '\n\n{} \n{}\n{} \n '.format(dash, header, dash)
        for index, book in enumerate(self.info, start=1):
            result += '\n{}. {} : {} \n '.format(index, book.ljust(22, ' '), self.info[book])
        result += '\n{}'.format(dash)
        return result


class Book(WellDisplayMixin):
    def __init__(self, name, info):
        """
        Book infos should be a Dictionary:
        {"autor": "author_name",
         "edition": ".."}
        """
        self.name = name
        self.info = info

    def __iter__(self):
        yield from iter(self.info.items())

    def __getitem__(self, item):
        return self.info[item]

    def __len__(self):
        return len(self.info)

    def __repr__(self):
        return self.name


class DuplicatedBook(Book):
    def __init__(self, name, info, copies_no, price):
        super().__init__(name, info)
        self.copies_no = copies_no
        self.price = price



    """
    Using the overload operator, prices from DuplicatedBook and Expensive Book, can be added, 
    or compared if they are equals or not!
    """

    def __add__(self, other):
        return f'Prices for the  books {self.name} and {other.name} are' \
               f' {self.price * self.copies_no + other.price * other.copies_no} .'

    def __radd__(self, other):
        return f'Prices for the  books {other.name} and {self.name} are {other.price * other.copies_no + self.price * self.copies_no} .'

    def __eq__(self, other):
        return self.price * self.copies_no == other.price * other.copies_no


class ExpensiveBook(Book):
    def __init__(self, name, info, copies_no, price):
        super().__init__(name, info)
        self.copies_no = copies_no
        self.price = price


class BooksCollection:
    books = None

    def __init__(self, *args):
        """
        BooksCollection should be a list that holds my books
        """
        self.books = list(args)

    def __iter__(self):
        # generator
        yield from iter(self.books)

    def __repr__(self):
        return self.books

    def __str__(self):
        return ', \n'.join(repr(book) for book in self.books)

    def __getitem__(self, item):
        return self.books[item]

    def __setitem__(self, key, value):
        self.books[key] = value

    def __delitem__(self, key):
        del self.books[key]

    def __len__(self):
        return len(self.books)

    def insert(self, index, book):
        return self.books.insert(index, book)

    def get_by_name(self, book_name):
        for book in self.books:
            if book.name == book_name:
                return book
        else:
            return

    def pick(self, book_name=None):
        result = self.get_by_name(book_name)
        if not result:
            result = random.choice(self.books)
        return result


class Library(WellDisplayMixin):
    def __init__(self, info):
        """
        Books info from Library  shoud be stored in a dictionary
        {"name ": "author",...
        }
        """
        self.info = info

    def __getitem__(self, item):
        return self.info[item]

    def __setitem__(self, key, value):
        self.info[key] = value

    def __delitem__(self, key):
        del (self.info[key])

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.info)

    def __contains__(self, item):
        return item in self.info

    def check_book(self, name):
        if name in self.info:
            return "Yes"
        else:
            return "Nope"


class ManageSomeExceptions:
    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is IndexError:
            print("This is an IndexError exception")
        elif exc_type is KeyError:
            print("This is an KeyError exception")
        elif exc_type is ZeroDivisionError:
            print("This is a ZeroDivision exception")
        return


@contextmanager
def some_exceptions():
    logger.debug('running log is starting ...')
    error = "  "
    try:
        yield " Only some exceptions are managed here!"
    except KeyError:
        error = "This is an KeyError exception"
    except IndexError:
        error = "This is an IndexError exception"
    except ZeroDivisionError:
        error = "This is a ZeroDivisionError"
    finally:
        print(error)
        logger.debug(
            'running log is closing and returning value ')


def nice_display(fnc):
    def wrapper(library, collection):
        listing = fnc(library, collection)
        middle_width = 29
        list_str = "\n".join(["    |   {0} |.".format(
            book.name.ljust(20, '.'))
            for book in listing])

        print("".join([
            __header,
            "    |{}         |. \n".format(" Existing books:".center(middle_width)),
            "    |{}         |.\n".format("".center(middle_width)),
            list_str,

            __footer
        ]))
        return fnc(library, collection)

    return wrapper


@nice_display
def check_the_library_books(library, collection):
    existing_books = []

    for book in collection:
        if book.name in library.info.keys():
            existing_books.append(book)

    return existing_books
