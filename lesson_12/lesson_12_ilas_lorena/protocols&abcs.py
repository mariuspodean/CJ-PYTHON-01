from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        print('seapeleaza')
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __setitem__(self, index, value):
        self._crayons[index] = value

    def __delitem__(self, index):
        del (self._crayons[index])

    def insert(self, index, value):
        self._crayons.insert(index, value)


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

print(isinstance(crayons_box, MutableSequence))

print(crayons_box)
print(len(crayons_box))
print(crayons_box[3])

print(crayons_box[0])
crayons_box[0] = 'porpora'
print(crayons_box[0])

crayons_box.remove(crayons_box[1])
print(crayons_box[1])

crayons_box.insert(6, 'magenta')
print(crayons_box[6])
