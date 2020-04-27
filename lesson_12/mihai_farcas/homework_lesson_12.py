from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __delitem__(self, key):
        del (self._crayons[key])

    def __setitem__(self, index, value):
        self._crayons[index] = value

    def insert(self, index, value):
        return self._crayons.insert(index, value)


def display_crayons_box_elements():
    for i in range(len(crayons_box)):
        print(crayons_box[i])


def title(title_name):
    print('_' * 20, '{} {}'.format(title_name, ('_' * 20)))


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

title('len() exemple')
print('{} is the initial len() '.format(crayons_box.__len__()))
display_crayons_box_elements()

title('insert() exemple')
crayons_box.insert(3, 'Element on the third position')
print(crayons_box[3])
print('insert the following on 3 position : {}'.format(crayons_box[3]))
display_crayons_box_elements()
print('{} is the len() after the insert of {}'.format(crayons_box.__len__(), crayons_box[3]))

title('setitem() exemple')
print("__setitem__(2,'Gigel')")
crayons_box.__setitem__(2, 'Gigel')
display_crayons_box_elements()

title('delitem() exemple for crayons_box[2]')
display_crayons_box_elements()
print('{} : is the element we want to delete and it is on crayons_box[2] '.format(crayons_box[2]))
crayons_box.__delitem__(2)
print('{} : is the new element on the crayons_box[2]'.format(crayons_box[2]))
display_crayons_box_elements()
