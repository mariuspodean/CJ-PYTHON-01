from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __delitem__(self, key):
        del self._crayons[key]

    def __setitem__(self, key, value):
        self._crayons[key] = value

    def insert(self, index, element):
        self._crayons.insert(index, element)

    def get_items(self):
        return self._crayons


crayons = 'White Yellow Blue Red Green Black Brown'.split()

crayons_box = CrayonsBox(crayons)

print(crayons)
print(crayons.__getitem__(0))
crayons_box.__delitem__(5)
crayons_box.__setitem__(1, 'Green')
crayons_box.insert(0, 'Purple')
print(crayons_box.get_items())