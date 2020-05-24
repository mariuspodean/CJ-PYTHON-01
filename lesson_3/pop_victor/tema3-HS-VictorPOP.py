#Granny Knitting Hobby shop by Victor POP
#
#HobyShop
#Requirements:
#    Have at least 400 articles in the shop
#    Have at least four types of articles (shirt, scarf, glove, heat)
#    Have at least five sizes (S M L XL XXL) for each type of article
#    To be able to sell the latest article that was added to the shop
#    To be able to sell any item that is in the shop
#    To restock the shop with new items
#
#Extras:
#    Loading and saving the articles/types & sizes in a .txt file
#    Modifying the structure of the articles and sizes
#    Automatic generation of the aticles database
#    Console interface to operate the requirements and extras


def hs_write(htype,hsize,hstock):
    with open('stoc.txt',mode='w') as filew:
        filew.writelines(str(htype)+'\n')
        filew.writelines(str(hsize)+'\n')
        filew.writelines(str(hstock))


def hs_print_stoc():
    print('numar total de articole in stock : '+str(len(hs_stock)))


def anulare():
    print('Alegere gresita !! Actiune anulata :)')


def hs_stoc_initial():
    global hs_type
    hs_type=['shirt','scarf','glove','hat']
    global hs_size
    hs_size=['S','M','L','XL','XXL']
    global hs_stock
    hs_stock=[(x,y) for x in hs_type for y in hs_size]*20
    print('stoc initial generat cu success in stoc.txt')
    hs_print_stoc()
    hs_write(hs_type,hs_size,hs_stock)


def hs_ver_stock():
    print('stockul actual : ')
    j=1
    for x in hs_type:
        for y in hs_size:
            print(str(j).zfill(2)+'. articol : '+x.ljust(7)+' marimea : '+y.rjust(3)+' bucati : '+str(hs_stock.count((x,y))).zfill(2))
            j+=1
    hs_print_stoc()
    print(hs_type)
    print(hs_size)


def hs_alege():
    print('Alege tipul de articol:')
    for s in range(len(hs_type)):
        print(str(s+1)+'. '+hs_type[s])
    try:
        styp=int(input('aleg : '))-1
    except ValueError:
        anulare()
        return None
    if styp not in list(range(len(hs_type))):
        print('Elementul ales nu exista')
        return None
    for s2 in range(len(hs_size)):
        print(str(s2+1)+'. '+hs_size[s2])
    try:
        ssiz=int(input('aleg : '))-1
    except ValueError:
        anulare()
        return None
    if ssiz not in list(range(len(hs_size))):
        print('Elementul ales nu exista')
        return None
    print('Ai ales un articol '+str(hs_type[styp])+' marimea '+str(hs_size[ssiz])+' stoc actual :'+str(hs_stock.count((hs_type[styp],hs_size[ssiz]))))
    return ((hs_type[styp],hs_size[ssiz]))


def hs_sell():
    global hs_stock
    sell_tuple=hs_alege()
    if sell_tuple is None:
        return
    try:
        sell_buc=int(input('bucati : '))
    except ValueError:
        anulare()
        return
    if sell_buc <= hs_stock.count(sell_tuple):
        print('Ai vandut '+str(sell_buc)+ ' bucati, mai ai pe stoc :'+str(hs_stock.count(sell_tuple)-sell_buc))
        for _ in range(sell_buc):
            hs_stock.remove(sell_tuple)
    else:
        print('Nu poti vinde mai mult decat ai STOC !! Actiune anulata :)')
    hs_print_stoc()


def hs_restock():
    global hs_stock
    articol=[hs_alege()]
    if articol==[None]: return
    bucati=int(input('bucati : '))
    if bucati < 1 :
        anulare()
        return               
    hs_stock+=articol*bucati
    print('stockul a crescut cu '+str(bucati)+' bucati')
    hs_print_stoc()


def hs_mod_ada(tipmas):
    element=input('Denumirea : ')
    if element=='':
        anulare()
        return
    if tipmas=='un tip':
        global hs_type
        hs_type.append(element)
        print('lista noua :')
        print(hs_type)
    else:
        global hs_size
        hs_size.append(element)
        print('lista noua :')
        print(hs_size)


def hs_mod_ste(tipmas2):
    if tipmas2=='un tip':
        global hs_type
        for ht in range(len(hs_type)):
            print(str(ht)+'. '+hs_type[ht])
        try:
            del hs_type[int(input('alege : '))]
        except (IndexError, ValueError):
            anulare()
        print('lista noua :')
        print(hs_type)
    else:
        global hs_size
        for hs in range(len(hs_size)):
            print(str(hs)+'. '+hs_size[hs])
        try:
            del hs_size[int(input('alege : '))]
        except (IndexError, ValueError):
            anulare()
        print('lista noua :')
        print(hs_size)


def hs_mod_alege(carac):
    print('1. adauga '+carac)
    print('2. sterge '+carac)
    try:
        opt_mod=int(input('alege : '))
    except ValueError:
        anulare()
        return
    if opt_mod==1:
        hs_mod_ada(carac)
    elif opt_mod==2:
        hs_mod_ste(carac)
    else:
        anulare()


print('Welcome to Granny Knitting SHOP')


try:
    with open('stoc.txt',mode='r') as filer:
        hs_type=filer.readline().strip("['']\n").split("', '")
        hs_size=filer.readline().strip("['']\n").split("', '")
        hs_stoc_import=filer.readline().replace('), (',').(').strip("['']").split('.')
        hs_stock=[]
        for i in range(len(hs_stoc_import)):
            hs_stock.append(tuple(map(str, hs_stoc_import[i].strip(")''(").split("', '"))))
    print('se importa stocul din stoc.txt')
    hs_print_stoc()
    print('tipurile de articole : ')
    print(hs_type)
    print('selectia de marimi : ')
    print(hs_size)
except FileNotFoundError:
    hs_stoc_initial()
opt = 0
while opt! = 666:
    print('   --- OPTIUNI ---')
    print(' 1. Afisare stoc detaliat')
    print(' 2. Sell - vazarea ultimului articol: '+'\033[1m'+str(hs_stock[-1][0])+' - '+str(hs_stock[-1][1])+'\033[0m')
    print(' 3. Sell - vanzare din stockul actual')
    print(' 4. Restock - adaugare articole')
    print('11. Modificare tipuri')
    print('12. Modificare marimi')
    print('20. Regenerare stoc initial')
    print('orice alta tasta = SAVE&EXIT')
    opt = input('aleg : ')
    if opt=='1':
        hs_ver_stock()
    elif opt=='2':
        print('Sold last article : '+str(hs_stock.pop()))
        print('numar total de articole in stock : '+str(len(hs_stock)))
    elif opt=='3':
        hs_sell()
    elif opt=='4':
        hs_restock()
    elif opt=='11':
        print('tipuri de articole :')
        print(hs_type)
        hs_mod_alege('un tip')
    elif opt=='12':
        print('marimile articolelor')
        print(hs_size)
        hs_mod_alege('o marime')
    elif opt=='20':
        hs_stoc_initial()
    else:
        hs_write(hs_type,hs_size,hs_stock)
        print('SAVE&EXIT executed')
        opt=666
