# Hobby Shop: > ##### Requirements: >
# * Have at least 400 articles in the shop > *
# Have at least four types of articles (shirt, scarf, glove, heat) >
# * Have at least five sizes (S M L XL XXL) for each type of article >
# * To be able to sell the latest article that was added to the shop >
# * To be able to sell any item that is in the shop >
# * To restock the shop with new items * * *


articles_types = ['shirt', 'scarf', 'glove', 'hat']
sizes = ['S', 'M', 'L', 'XL', 'XXL']

size_type_articles = []

for article_type in articles_types:
    for size in sizes:
        article = (article_type, size)
        size_type_articles.append(article)

all_articles = size_type_articles * 20

print(all_articles)
print(len(all_articles))

all_articles.pop()

print(all_articles)
print(len(all_articles))

all_articles.remove(size_type_articles[0])

print(all_articles)
print(len(all_articles))

article = ('hat', 'S')
all_articles.insert(len(all_articles), article)

print(all_articles)
print(len(all_articles))
