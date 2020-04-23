from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __setitem__(self, index, value):
        return self._crayons[index] == value

    def insert(self, index) :
        return crayons.append(crayons_box[index])

    def __delitem__(self, index):
        del (self._crayons[index])


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

print(isinstance(crayons_box, CrayonsBox))
