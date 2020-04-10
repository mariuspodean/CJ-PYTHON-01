Homework = ['400Articles', '4types', '5sizes', 
'To be able to sell the latest article that was added to the shop',
 'To be able to sell any item that is in the shop', ' To restock the shop with new items']

types = ['Shirts', 'Hats', 'Shoes', 'Gloves']
sizes = ['Slim', 'Normal', 'Medium', 'Large', 'Giga']
colors = ['green','blue', 'red', 'black', 'white']
articles = []

for product in types:
    for size in sizes:
      for color in colors:
        articles.append([product, size, color])
articles = articles * 20

store_merchandise = len(articles)
print(store_merchandise)
store_soldProducts = ['Hats', 'Slim', 'black']

for article in articles:
  if store_soldProducts == article:
    print(article)


articles.remove(['Hats', 'Slim', 'black'])
print('--------------------------------')

for article in articles:
  if store_soldProducts == article:
    print(article)
print(len(articles))

articles.pop()
print(len(articles))
print('--------------------------------')
restock = [['Hats', 'Slim', 'black'], ['Gloves', 'Giga', 'white']]
restock.count('Hats')
restock.sort(key=None, reverse=False)
for item in restock:
  articles.append(item)
print(len(articles))
