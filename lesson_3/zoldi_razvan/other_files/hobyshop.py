scarfs = []
for article in range (20):
    for article in ['scarf']:
        for size in ['small', 'medium', 'large', 'extralarge', 'extraextralarge']:
            scarfs.append([article,size])
            
shirts = []
for article in range (20):
    for article in ['shirt']:
        for size in ['small', 'medium', 'large', 'extralarge', 'extraextralarge']:
            shirts.append([article,size])
            
gloves = []
for article in range (20):
    for article in ['glove']:
        for size in ['small', 'medium', 'large', 'extralarge', 'extraextralarge']:
            gloves.append([article,size])
            
hats = []
for article in range (20):
    for article in ['hat']:
        for size in ['small', 'medium', 'large', 'extralarge', 'extraextralarge']:
            hats.append([article,size])

articles = hats + shirts + gloves + scarfs 
len(articles)

