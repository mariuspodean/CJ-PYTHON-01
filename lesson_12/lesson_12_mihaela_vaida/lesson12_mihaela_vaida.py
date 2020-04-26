from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __setitem__(self, index, value):
        self._crayons[index] = value

    def insert(self, index, value):
        return self._crayons.insert(index, value)

    def __delitem__(self, index):
        del (self._crayons[index])


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

print(isinstance(crayons_box, CrayonsBox))

crayons.__delitem__(3)
print(crayons)
# ['White', 'Yellow', 'Blue', 'Green', 'Black', 'Brown']
crayons.insert(0, 'Pink')
crayons.__setitem__(2, 'White')
crayons.__setitem__(2, 'White')
print(crayons)
