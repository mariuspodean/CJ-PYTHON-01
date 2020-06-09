from application import *

print("*********************************************")
print(" My personal books:")
book1 = Book("Contele de Monte-Cristo", {"author": "Alexandre Dumas", "edition": 1985})
book2 = Book("Ocolul pamantului in 80 de zile", {"author": "Jules Verne"})
book3 = Book("Marile sperante", {"author": "Charles Dickens"})
book4 = Book("Numele trandafirului", {"author": "Umberto Eco"})
book5 = Book("Idiotul", {"author": "Dostoeveski"})
book6 = Book("Maestrul si Margareta", {"author": "Mihail Bulgakov"})
book7 = Book("O mie  noua sute optzeci si patru", {"author": "George Orwell"})
book8 = Book("Jane Eyre", {"author": "Charlotte Bronte"})
book9 = Book("La Rascruce de vanturi", {"author": "Emily Bronte"})
book10 = Book("Muntele vrajit", {"author": "John Fowles "})
print(book1)
print(book2)
print(book3)
print("*********************************************")
print("My personal duplicated books :")
duplicated1 = DuplicatedBook("Numele trandafirului", {"author": "Umberto Eco"},2, 33)
duplicated2 = DuplicatedBook("La Rascruce de vanturi", {"author": "Emily Bronte"},3, 40)
duplicated3 = DuplicatedBook("Ocolul pamantului in 80 de zile", {"author": "Jules Verne"},2, 15)
print(duplicated1)
print(duplicated2)
print(duplicated3)
exp_book1 = ExpensiveBook("La Rascruce de vanturi", {'author':"Emily Bronte", "edition":'limited'}, 1, 250)
exp_book2 = ExpensiveBook("Biblia", {"author": None}, 1, 1000)
print(exp_book1)
print(exp_book2)
print("*********************************************")
print("Let's check the adding  prices for  some books:")
print(duplicated1+exp_book2)
print(exp_book1+duplicated3 )
print("Let's compare the prices for some books")
print(duplicated1==exp_book1)
print(duplicated1==exp_book2)
print("*********************************************")
print("My personal   books collection :")
print("*********************************************")
my_books_collection = BooksCollection(book1, book2, book3, book4, book6, book7, book8, book9)
my_books_collection.__delitem__(0)
my_books_collection.insert(0, book1)
my_books_collection.__delitem__(0)
my_books_collection.insert(10, book10)
my_books_collection.insert(10, book3)
#my_books_collection.insert(10, duplicated1)

print(my_books_collection)

print("Pick a random book : ", my_books_collection.pick())
print("Pick a nominated book:", my_books_collection.pick("Contele de Monte-Cristo"))
print("*********************************************")
print("Creating the Library instance:")

print("*********************************************")

library = Library({"Ocolul pamantului in 80 de zile": "Jules Verne",
                   "Marile sperante": "Umberto Eco",
                   "La Rascruce de vanturi": "Emily Bronte",
                   "Muntele vrajit": "John Fowles",
                   "Călătoriile lui Gulliver": "Jonathan Swift",
                   "Portretul lui Dorian Gray": "Oscar Wilde",
                   " Un veac de singurătate": "Gabriel Garcia Marquez",
                   "La răsărit de Eden": "John Steinbeck",
                   "Invitație la vals ": "Mihail Drumeș",
                   "Lolita": "Vladimir Nabokov",
                   "Fahrenheit 451": "Ray Bradbury",
                   "Marele Gatsby": "Francis Scott Fitzgerald",
                   "Zece negri mititei": "Agatha Christie",
                   "Mizerabilii": "Victor Hugo ",
                   " Aventurile lui Huckleberry Finn": "Mark Twain",
                   "Contele de Monte-Cristo": "Alexandre Dumas"
                   }
                  )
print(library)
print("Check if  the book 'Singur pe lume ' este in Library:",
      library.check_book("Singur pe lume "))

print("Check if  the book 'Lolita ' este in Library:",
      library.check_book("Lolita"))
print("Check if  {}  este in Library:".format(book3.name), library.check_book(book3.name))
print("Check if  {}  este in Library:".format(book1.name), library.check_book(book1.name))
print("*********************************************")
print("Let's handle some exceptions using a Context Manager")
print("Context managers are a powerful tool that is kind of particular to Python. There are cases where we want "
      "to always perform some operation after a block of code.")
print("*********************************************")
with some_exceptions() as check:
    library.info["Unknown book"]
    print(check)

with some_exceptions() as check:
    list(library.info.keys())[100]
    print(check)

with some_exceptions() as check:
    len(list(library.info.keys())) / 0
    print(check)

print("*********************************************")

print("*********************************************")

print(check_the_library_books(library, my_books_collection))
