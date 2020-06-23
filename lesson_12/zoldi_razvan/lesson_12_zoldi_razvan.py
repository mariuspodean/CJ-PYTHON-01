# Challenge: Fix CrayonsBox so that it fully conforms to MutableSequence.

from collections.abc import MutableSequence
from random import shuffle


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __delitem__(self, index):
        del self._crayons[index]

    def insert(self, index, crayon):
        self._crayons.insert(index, crayon)

    def __setitem__(self, index, item):
        self._crayons[index] = item



crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)
# print numbers of crayons in box
print(len(crayons_box))
# get item at index 3
print(crayons_box[3])  # ths crayon is red
# delete crayon Red
crayons_box.__delitem__(3)
print()
# test if crayon red still in box
for item in crayons_box:
    print(item)
print()
# insert back red crayon into box
crayons_box.insert(3, 'Red')
# test if crayon red back in box
for item in crayons_box:
    print(item)
print()
# replace crayon onto the box
crayons_box.__setitem__(0, 'Dark green')
# test if white crayon was replaced by dark green
for item in crayons_box:
    print(item)
print()
# lets shuffle them (funny)
shuffle(crayons_box)
for item in crayons_box:
    print(item)
print()

