from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    ##############################################

    def __setitem__(self, index, value):
        self._crayons[index] = value

    def __delitem__(self, index):
        del self._crayons[index]

    def insert(self, index, item):
        return self._crayons.insert(index, item)

    def append(self, item):
        return self._crayons.append(item)

    def reverse(self):
        return self._crayons.reverse()

    def extend(self, iterable):
        return self._crayons.extend(iterable)

    def __add__(self, other):
        return str(self) + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

    def pop(self, index: int = ...):
        return self._crayons.pop(index)

    def __str__(self):
        return"({0})".format(self._crayons)




crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

# muttablesequence
abcs = [MutableSequence]
for abc in abcs:
    print(
        'crayons is a {}: {}'.format(
            abc.__name__, isinstance(crayons, abc))
    )
# iadd
# crayons_box += "Purple"
# print(crayons_box)
'''what is happening here?'''
crayons += "Pink"
print(crayons)

# pop
crayons_box.pop(0)
print(crayons_box)

# extend
newlist= ['Bordoe']
crayons_box.extend(newlist)
print('New Color: ', crayons_box)


# reverse

crayons_box.reverse()
print(crayons_box)

# append
crayons_box.append('Vernil')
print(crayons_box)

# insert

crayons_box.insert(1, 'Orange')
print(crayons_box)

# delitem

crayons_box.__delitem__(0)
print(crayons_box)

# setitem

crayons_box.__setitem__(0, 'Aqua_Light')
print(crayons_box)

# getitem

print(crayons_box.__getitem__(0))

# len

print(crayons_box.__len__())

# Challenge!
# Fix CrayonsBox so that it fully conforms to MutableSequence.