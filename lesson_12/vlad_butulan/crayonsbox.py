from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):
    """MutableSequence class type"""

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]
    
    def __setitem__(self, index, value):
        self._crayons[index] = value
    
    def __delitem__(self, index):
        del self._crayons[index]
    
    def insert(self, index, value):
        self._crayons.insert(index, value)


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

print(f"Is crayons_box a mutable list: {isinstance(crayons_box, MutableSequence)}")

print(f"Original crayons list: {crayons_box._crayons}")
print(f"Testing __getitem__(3): {crayons_box.__getitem__(3)}")

crayons_box.__setitem__(2, 'Purple')
print(f"Crayons list after calling __setitem(2, 'Purple'): {crayons_box._crayons}")

crayons_box.__delitem__(0)
print(f"Crayons list after calling __delitem__(0): {crayons_box._crayons}")

crayons_box.insert(6, 'Blue')
print(f"Crayons list after calling insert(6, 'Blue'): {crayons_box._crayons}")

