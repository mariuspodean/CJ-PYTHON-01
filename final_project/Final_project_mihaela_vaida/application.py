import random
import logging

class WellDisplayMixin:
    def __str__(self):
        dash = '*'*40
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
    def __init__(self, name, info, copies_no):
        super().__init__(name, info)
        self.copies_no = copies_no


class BooksCollection():
    books = None

    def __init__(self, *args):
        """
        BooksCollection should be a list that holds my books
        """
        self.books = list(args)

    def __iter__(self):
        yield from iter(self.books)

    def __repr__(self):
        return ', \n'.join(repr(book)  for book in self.books)

    def __str__(self):
        return repr(self)

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


