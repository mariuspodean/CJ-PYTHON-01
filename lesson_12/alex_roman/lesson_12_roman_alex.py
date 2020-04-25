from collections.abc import MutableSequence

class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, ind):
        return self._crayons[ind]

    def __delitem__(self, ind):
        del (self._crayons[ind])

    def __setitem__(self, ind, val):
        if not (0 <= ind <= len(self)):
            raise IndexError('Index is out of range')
        self._crayons[ind] = val

    def insert(self, ind, val):
        self._crayons.insert(ind, val)


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

# Testing "__delitem__"
crayons_box.__delitem__(1)

# Testing "__setitem__"
crayons_box.__setitem__(1, "Black")

# Testing "insert"
crayons_box.insert(1, "Black")
