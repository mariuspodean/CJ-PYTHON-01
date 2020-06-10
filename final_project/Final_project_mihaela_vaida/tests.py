from application import *
from playground import *
import unittest


class TestBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Start testing!')

    @classmethod
    def tearDownClass(cls) -> None:
        print('End Testing!')

    def test_book_init(self):
        book1 = Book("Contele de Monte-Cristo", {"author": "Alexandre Dumas", "edition": 1985})
        self.assertIsInstance(book1, Book)

    def test_book_has_attributes(self):
        name = 'Contele de Monte-Cristo'
        info = {"author": "Alexandre Dumas", "edition": 1985}
        book1 = Book(name, info)
        assert hasattr(book1, 'name'), 'Book is missing name attribute !'
        assert hasattr(book1, 'info'), 'Book  is missing info attribute!'


class TestDuplicatedBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Start testing!')

    @classmethod
    def tearDownClass(cls) -> None:
        print('End Testing!')

    def test_duplicated_book_init(self):
        duplicated1 = DuplicatedBook("Numele trandafirului",
                                     {"author": "Umberto Eco"}, 2, 33)
        self.assertIsInstance(duplicated1, DuplicatedBook)

    def test_duplicated_attributes(self):
        name = "Numele trandafirului"
        info = {"author": "Umberto Eco"}
        copies_no = 2
        price = 33
        duplicated1 = DuplicatedBook(name, info, copies_no, price)
        assert hasattr(duplicated1, 'name'), 'DuplicatedBook is missing name attribute!'
        assert hasattr(duplicated1, 'info'), 'DuplicatedBook is missing info attribute!'
        assert hasattr(duplicated1, 'copies_no'), 'DuplicatedBook is missing copies_no attribute!'
        assert hasattr(duplicated1, 'price'), 'DuplicatedBook is missing price attribute!'

    def test_add(self):
        duplicated1 = DuplicatedBook("Numele trandafirului", {"author": "Umberto Eco"}, 2, 33)
        exp_book1 = ExpensiveBook("La Rascruce de vanturi", {'author': "Emily Bronte", "edition": 'limited'}, 1, 250)
        self.assertEqual(duplicated1+exp_book1, 'Prices for the  books Numele trandafirului and'
                                                ' La Rascruce de vanturi are 316 .')
    def test_equal(self):
        duplicated1 = DuplicatedBook("Numele trandafirului", {"author": "Umberto Eco"}, 2, 33)
        exp_book1 = ExpensiveBook("La Rascruce de vanturi", {'author': "Emily Bronte"}, 1,1000)

        self.assertEqual(duplicated1==exp_book1, False)



class Test_ExpensiveBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Start testing!')

    @classmethod
    def tearDownClass(cls) -> None:
        print('End Testing!')

    def test_expensive_init(self):
        exp_book1 = ExpensiveBook("La Rascruce de vanturi",
                                  {'author': "Emily Bronte", "edition": 'limited'}, 1, 250)
        self.assertIsInstance(exp_book1, ExpensiveBook)

    def test_expensive_attributes(self):
        name = "Numele trandafirului"
        info = {"author": "Umberto Eco"}
        copies_no = 2
        price = 3300
        expensive1 = ExpensiveBook(name, info, copies_no, price)
        assert hasattr(expensive1, 'name'), 'ExpensiveBook is missing name attribute!'
        assert hasattr(expensive1, 'info'), 'ExpensiveBook is missing info attribute!'
        assert hasattr(expensive1, 'copies_no'), 'ExpensiveBook is missing copies_no attribute!'
        assert hasattr(expensive1, 'price'), 'ExpensiveBook is missing price attribute!'


class TestBookCollection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Start testing!')

    @classmethod
    def tearDownClass(cls) -> None:
        print('End Testing!')

    def test_collection_init(self):
        books = book1, book2, book3, book4
        collection = BooksCollection(books)
        assert hasattr(collection,'books'), 'Collection has no books attribute!'
        self.assertIsInstance(collection, BooksCollection)

    def test_pick_named(self):
        book1 =Book("Ocolul pamantului in 80 de zile", {"author": "Jules Verne"})
        my_books_collection = BooksCollection(book1, book2, book3)
        self.assertEqual(my_books_collection.pick(book1.name), book1)

    def test_pick_random(self):
        book1 = Book("Contele de Monte-Cristo", {"author": "Alexandre Dumas", "edition": 1985})
        book2 = Book("Ocolul pamantului in 80 de zile", {"author": "Jules Verne"})
        book3 = Book("Marile sperante", {"author": "Charles Dickens"})
        my_books_collection = BooksCollection(book1, book2, book3)
        random_name = my_books_collection.pick()
        self.assertIn(random_name, my_books_collection)

class TestLibrary(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Start testing!')

    @classmethod
    def tearDownClass(cls) -> None:
        print('End Testing!')

    def test_library_init(self):
        info = {"Ocolul pamantului in 80 de zile": "Jules Verne",
                   "Marile sperante": "Umberto Eco",
                   "La Rascruce de vanturi": "Emily Bronte"}
        library= Library(info)
        assert isinstance(library, Library)
        assert hasattr( library, "info"), 'Info attribute is missing!'

    def test_check(self):
        info = {"Ocolul pamantului in 80 de zile": "Jules Verne",
                    "La Rascruce de vanturi":"Emily Bronte"}
        library = Library (info)

        self.assertNotEqual(library.check_book("Fluturi"), "Yes")
        self.assertEqual(library.check_book("Fluturi"), "Nope")

class TestIndependentFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start testing!')

    @classmethod
    def tearDownClass(cls):
        print('End testing!')

    def test_check_the_library(self):
        book1 = Book("Contele de Monte-Cristo", {"author": "Alexandre Dumas", "edition": 1985})
        book2 = Book("Ocolul pamantului in 80 de zile", {"author": "Jules Verne"})
        book3 = Book("Marile sperante", {"author": "Charles Dickens"})
        my_books_collection = BooksCollection(book1, book2, book3)
        library = Library({"Marile sperante": "Umberto Eco",
                           "La Rascruce de vanturi": "Emily Bronte",
                           "Muntele vrajit": "John Fowles",
                           "Călătoriile lui Gulliver": "Jonathan Swift",
                           "Portretul lui Dorian Gray": "Oscar Wilde",
                           "Ocolul pamantului in 80 de zile":"Charles Dickens"})

        self.assertEqual(type(check_the_library_books(library, my_books_collection)), list)


if __name__ == '__main__':
    unittest.main(verbosity=2)
