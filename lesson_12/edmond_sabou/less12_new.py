from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __setitem__(self, key, value):
        self._crayons[key] = value

    def __delitem__(self, key):
        del self._crayons[key]

    def insert(self, index, item):
        return self._crayons.insert(index, item)

    def __str__(self):
        return "({0})".format(self._crayons)


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

abcs = [MutableSequence]
for abc in abcs:
    print(
        'stud_collection is a {}: {}'.format(
            abc.__name__, isinstance(crayons_box, abc))
    )


print(len(crayons_box))
print(crayons_box.__getitem__(2))
crayons_box.__setitem__(2, "Pink")
print(crayons_box)
crayons_box.__delitem__(2)
print(crayons_box)
crayons_box.pop(2)

crayons_box.reverse()
print(crayons_box)

crayons_box.insert(2, "Fox")
print(crayons_box)
