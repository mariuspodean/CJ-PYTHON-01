# Lesson 12 - Protocols and ABCs


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
