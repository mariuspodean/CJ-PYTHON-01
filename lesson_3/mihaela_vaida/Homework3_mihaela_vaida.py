#HobyShop
#Requirements:
#Have at least 400 articles in the shop
#Have at least four types of articles (shirt, scarf, glove, heat)
#Have at least five sizes (S M L XL XXL) for each type of article
#To be able to sell the latest article that was added to the shop
#To be able to sell any item that is in the shop
#To restock the shop with new items
article=['shirt', 'scarf', 'glove', 'heat']*20
sizes=('S', 'M', 'L', 'XL', 'XXL')

all_articles=[(x,y)
              for x in article
              for y in sizes]
print("The number of total articles in the store is :", len(all_articles))
#The number of total articles in the store is : 400
all_articles  #pentru a vedea cele 400 de articole si marimea lor 

sold_last_article=all_articles.pop()
print(" The latest article that was added to the shop and now is sold : ", sold_last_article)

sold_any_article=all_articles.pop(0)  #se va vinde elementul cu indexul dat-0 in acest caz
print(" The   article that was  sold with requested index is  ", sold_any_article)
# alta varianta cu remove , articolul si marimea vanduta
all_articles.remove(('shirt', 'L'))


len(all_articles)
#394

#restock the shop with new items
all_articles.append(('shirt', 'L'))

new_articles=[(a,y)
              for a in['pants','mom jeans']
              for y in sizes]


all_articles+new_articles

# or we can restock using extend method :
article.extend(['mom jeans','hat'])
all_articles=[(x,y)
...               for x in article
...               for y in sizes]
all_articles
len(all_articles)

