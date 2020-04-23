# Lesson 12 - Protocols and ABCs
'''

We have the following code:

```python3
from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)
```

Fix **CrayonsBox** so that it fully conforms to **MutableSequence**.
'''

from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __delitem__(self, item):
        del (self._crayons[self._crayons.index(item)])

    def __setitem__(self, index, item):
        self._crayons[index] = item

    def insert(self, index, item):
        self._crayons.insert(index, item)


def iteration(obj):
    for x in obj:
        print(x)


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

print('\ncrayons_box iterable:')
iteration(crayons_box)
print('len = ', len(crayons_box))

print('\ncrayons_box __getitem__ :')
print('position 2 item : ', crayons_box[2], '\n')
iteration(crayons_box)
print('len = ', len(crayons_box))

print('\ncrayons_box __delitem__ :')
crayons_box.__delitem__('Blue')
iteration(crayons_box)
print('len = ', len(crayons_box))

print('\ncrayons_box __setitem__ :')
crayons_box.__setitem__(5, 'Blue')
iteration(crayons_box)
print('len = ', len(crayons_box))

print('\ncrayons_box insert :')
crayons_box.insert(3, 'Brown')
iteration(crayons_box)
print('len = ', len(crayons_box))
