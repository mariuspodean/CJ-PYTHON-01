#creare tuple cu tipuri de aticole si marimi
articles = ("shirt", "scarf", "glove", "heat")
sizes = ("S", "M", "L", "XL", "XXL")

#numarul din fiecare articol cu fiecare marime
nr_art_ind = 20

#lista cu toate articolele
list_of_articles = [(article, size)
                    for article in articles
                    for size in sizes
                    for nr_ord in range(nr_art_ind)
                    ]

print(list_of_articles)
print(len(list_of_articles))

#vanzare ultimului articol adaugat
last_art = list_of_articles.pop()
print(last_art)
print(len(list_of_articles))

#vanzare articol la alegere
art_for_sell = ("scarf", "M")
list_of_articles.remove(art_for_sell)
print(list_of_articles.count(art_for_sell))

#adaugare de articole noi
new_article = ("jacket")
#numarul articolelelor noi pentru fiecare marime
nr_new_art = 5
list_of_new_art = [(new_article, size)
                   for size in sizes
                   for nr_ord in range(nr_new_art)
                                      ]
list_of_articles += list_of_new_art
print(list_of_articles)
print(len(list_of_articles))