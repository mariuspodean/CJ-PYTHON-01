from random import randint
from FinalProject.application import PCpart, welcome, PartsList, ComputerConfig, main, KeyWords_Map

the_list_of_parts = [
    ['Intel® Core™ i5-10400 Comet Lake', 'PRO', 2900, 12, None, 1200, None, 959],
    ['Intel® Core™ i3-9100F Coffee Lake', 'PRO', 3600, 6, None, 1151, None, 356],
    ['AMD Ryzen™ 7 3700X', 'PRO', 4400, 36, None, 4, None, 879],
    ['AMD Ryzen™ 5 1600AF', 'PRO', 3600, 16, None, 4, None, 468],
    ['Intel® Core™ i7-10700K', 'PRO', 3800, 16, None, 1200, None, 2089],
    ['AMD Ryzen™ 9 3900X', 'PRO', 4600, 70, None, 4, None, 2289],

    ['Asus prime', 'MTB', None, 'DDR4', 32, 1151, 1, 272],
    ['Asus Z170l', 'MTB', None, 'DDR4', 64, 1151, 2, 930],
    ['Asus WS C422 PRO/SE', 'MTB', None, 'DDR4', 512, 1200, 1, 1169],
    ['Gigabyte Z490M', 'MTB', None, 'DDR4', 128, 1200, 1, 779],
    ['MSI A320M-A PRO', 'MTB', None, 'DDR4', 32, 4, 0, 269],
    ['Asus TUF X470', 'MTB', None, 'DDR4', 64, 4, 2, 879],

    ['ASUS GeForce RTX 2070 MINI', 'VID', 14003, 'GDDR6', 8, None, None, 2199],
    ['ASUS GeForce GTX 1650 TUF', 'VID', 8002, 'GDDR5', 6, None, None, 699],
    ['XFX Radeon RX 580 GTS', 'VID', 8100, 'GDDR5', 8, None, None, 829],
    ['ASUS ROG Strix Radeon™ RX 5700', 'VID', 14000, 'GDDR6', 8, None, None, 2299],
    ['Zotac nVidia GeForce GT 710', 'VID', 1600, 'GDDR3', 2, None, None, 209],
    ['ASUS ROG Strix GeForce® GTX 1660', 'VID', 14002, 'GDDR6', 6, None, None, 1299],
    ['Gigabyte GeForce® RTX 2070', 'VID', 14003, 'GDDR6', 8, None, None, 2929],

    ['HyperX Fury RGB', 'RAM', 3000, 'DDR4', 8, None, None, 244],
    ['Corsair Vengeance LPX Black', 'RAM', 3000, 'DDR4', 16, None, None, 388],
    ['HyperX Fury RGB 2*8GB', 'RAM', 3200, 'DDR4', 16, None, None, 431],
    ['Corsair Vengeance RGB PRO 2*16GB', 'RAM', 3000, 'DDR4', 32, None, None, 842],
    ['HyperX Fury Black', 'RAM', 3200, 'DDR4', 64, None, None, 1729],

    ['Silicon Power A55', 'SSD', None, None, 512, None, True, 359],
    ['Kingston A2000', 'SSD', None, None, 250, None, True, 223],
    ['Western Digital', 'SSD', None, None, 120, None, True, 156],
    ['Samsung 970 EVO Plus', 'SSD', None, None, 2048, None, True, 2483],
    ['Samsung 860 EVO', 'SSD', None, None, 1024, None, True, 849],
]

all_parts = []
for each_part in the_list_of_parts:
    all_parts.append(PCpart(*[each_small_part for each_small_part in each_part]))
config_parts = PartsList('Configuration parts', *all_parts)
print(all_parts)
print(config_parts)
print('printing random part:\n')
print(config_parts[randint(0, len(config_parts)-1)])

first_build = ComputerConfig('first build', *[config_parts[_] for _ in [2,8,14,20,28]])
print('first computer build 1')
print(first_build)

new_part = PCpart('Added Hard 50', 'SSD', None, None, 1024, None, True, 666)
config_parts += new_part
# config_parts += config_parts
print(config_parts)

print(new_part)

ssduri = config_parts.sort_part('SSD')
print(ssduri[randint(0,len(ssduri)-1)])

print(config_parts.pick_random_part('VID'))

cfg = config_parts.pick_random_part
build_2 = ComputerConfig('2nd build', cfg('MTB'),cfg('VID'),cfg('PRO'),cfg('RAM'),cfg('SSD'))
print(build_2)
print(build_2.price)

value= 50
test = config_parts.pick_pro(value)
print(test)
test2 = config_parts.pick_mtb(value,test.socket)
print(test2)
test3 = config_parts.pick_vid(value)
print(test3)
test4 = config_parts.pick_ram(value)
print(test4)
test5 = config_parts.pick_ssd(value)
print(test5)
second_build = ComputerConfig('sec build', test,test2,test3,test4,test5)
print(second_build)
print(second_build.price)

# third_build = configure_computer('3rd time', config_parts, [10,20,30,40,50])
# print(third_build)
# print(third_build.price)
# forth_build = configure_computer('best', config_parts, [100,100,100,100,100])
# fifth_build = configure_computer('cheap', config_parts, [0,0,0,0,0])
# print(complete_configurations())

# save_to_txt(str(complete_configurations()))
keywords = KeyWords_Map('keywords', {
    # 'name':[pro,mtb,vid,ram,ssd]
    'gaming':[100,100,100,69,78],
    'office':[23,0,15,10,10],
    'space ship': [100, 100, 100, 100, 100],
    'minimal':[0,0,0,0,0],
    'middle point':[50,50,50,50,50],
    'video edit':[100,60,100,66,100],
    'storage':[0,0,0,0,100],
    'AI':[100,100,0,100,43],
})
print(keywords)
print('finish line')
print(f'\n\n\n\n\n')

welcome()
main(keywords, config_parts)
