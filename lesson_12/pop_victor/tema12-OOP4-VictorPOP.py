from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __delitem__(self, value):
        self._crayons.remove(self._crayons[value])

    def __setitem__(self, index, value):
        self._crayons[index] = value

    def insert(self, index, value) -> None:
        self._crayons.insert(index, value)

    def __str__(self):
        return str(self._crayons)


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

print(crayons_box)

crayons_box.remove('Red')
crayons_box[1] = 'Magenta'
crayons_box.insert(2, 'Pink')

print(crayons_box)
print(isinstance(crayons_box, MutableSequence))
