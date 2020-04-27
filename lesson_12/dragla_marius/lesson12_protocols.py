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

    def insert(self, index, object):
        self._crayons.insert(index, object)


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

test_mutable_seq = MutableSequence

print(f'is MutableSequence: {isinstance(crayons_box, test_mutable_seq)}')
print('---')

print(f'_crayons list: {crayons}')
print('---')

print(f'len test: {len(crayons_box)}')
print('---')

print(f'getitem test (item at index 3): {crayons_box[3]}')
print('---')

crayons_box.remove(crayons_box[3])

print(f'delitem test (new item at index 3 after removal of previous item): {crayons_box[3]}')
print('---')

print(f'length of list after removal: {len(crayons_box)}')
print('---')

crayons_box[3] = 'red'

print(f'setitem test (item at index 3 after setting new value): {crayons_box[3]}')
print('---')

crayons_box.insert(3,'orange')

print(f'insert test (item at index 3 after inserting new value): {crayons_box[3]}')
print('---')

print(f'length of list after insertion: {len(crayons_box)}')

