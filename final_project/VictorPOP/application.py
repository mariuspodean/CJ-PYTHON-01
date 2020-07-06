import logging
import time
from random import randint
from contextlib import contextmanager


def welcome():
    texts = [
        'Hello and welcome to the best',
        'COMPUTER CONFIGURATOR',
        'we are here to help you choose a PC',
        'for the things you need',
    ]
    for txt in texts:
        print(txt)


def main(keywords, config_parts):
    key_input = None
    while key_input != 666:
        print('please enter a keyword for your computer')
        print(keywords)
        print('type exit to quit')
        key_input = input(' :: ')
        if key_input in keywords:
            custom_build = configure_computer(key_input, config_parts, keywords[key_input])
            print(f'\n{custom_build} price : {custom_build.price} lei\n')
        if key_input == 'exit':
            print(f'you have configured {len(config_list)} builds')
            print(config_list)
            save_to_txt(str(config_list))
            print('thank you and DO come back')
            key_input = 666


# mixin class
class DisplayMixin:
    # custom repr
    def __repr__(self):
        the_text = f'{len(self.items)} parts : \n'
        for part in self.items:
            the_text += f'{part.part_type} '
        return the_text

    # custom str
    def __str__(self):
        the_text = f'{self.name} build has {len(self.items)} parts :\n'
        for _ in self.items:
            the_text += f'{_.part_type} - {_.name} - {_.price}\n'
        return the_text


# muttable mapping
class KeyWords_Map:
    def __init__(self, name='noname', keywords=None):
        self.name = name
        self.items = keywords

    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del (self.items[key])

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __eq__(self, other):
        return self.items == other

    def __ne__(self, other):
        return self.items != other

    def keys(self):
        return self.items.keys()

    def items(self):
        return self.items.items()

    def values(self):
        return self.items.values()

    def get(self, item):
        return self.items[item]

    def pop(self):
        return self.items.pop

    def clear(self):
        pass
        # return clear(self.items)

    def update(self):
        pass

    def setdefault(self):
        pass

    def __repr__(self):
        return self.name

    def __str__(self):
        return ' - '.join(self.items)


class PCpart():

    def __init__(
            self, name='noname', part_type=None, speed=None, ram=None,
            maxram=None, socket=None, m2=None, price=0
    ):
        self.name = name
        self.part_type = part_type
        self.speed = speed
        self.ram = ram
        self.maxram = maxram
        self.socket = socket
        self.m2 = m2
        self.price = price

    def __len__(self):
        return 1

    # custom repr
    def __repr__(self):
        the_text = f'{self.name} - {self.part_type} - {self.price}'
        return the_text

    # custom str
    def __str__(self):
        the_text = f'part description:\n'
        for test in self.__dict__.keys():
            if self.__dict__[test] is not None:
                the_text += f'{test} : {self.__dict__[test]}\n'
        return the_text


# inheritance
# sequence - mutable sequence
class PartsList(DisplayMixin):

    def __init__(self, name='noName', *args):
        self.name = name
        self.items = list(args)

    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del (self.items[key])

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def append(self, item):
        self.items.append(item)

    def reverse(self):
        self.items.reverse()

    def extend(self, other):
        return self.items.extend(other)

    def pop(self):
        return self.items.pop()

    def remove(self, item):
        self.items.remove(item)

    # operator overload
    def __add__(self, other):
        if len(other) > 1:
            raise ValueError('too many arguments')
        self.items.append(other)
        return self

    def sort_part(self, part):
        the_list = []
        for _ in self.items:
            if _.part_type == part:
                the_list.append(_)
        return the_list

    def pick_random_part(self, part):
        the_list = []
        for _ in self.items:
            if _.part_type == part:
                the_list.append(_)
        return the_list[randint(0, len(the_list) - 1)]

    @staticmethod
    def _index_of_score(the_list, value_list, score):
        sorted_list = []
        sorted_value_list = sorted(value_list)
        for _ in sorted_value_list:
            sorted_list.append(the_list[value_list.index(_)])
        # print(sorted_list)
        score_index = int(score / 100 * (len(sorted_list) - 1))
        return sorted_list[score_index]

    def pick_pro(self, score=50):
        the_list = []
        value_list = []
        for _ in self.items:
            if _.part_type == 'PRO':
                the_list.append(_)
                value_list.append(_.speed * _.ram)
        return self._index_of_score(the_list, value_list, score)

    def pick_mtb(self, score=50, socket=4):
        the_list = []
        value_list = []
        for _ in self.items:
            if _.part_type == 'MTB' and _.socket == socket:
                the_list.append(_)
                value_list.append(_.maxram)
        return self._index_of_score(the_list, value_list, score)

    def pick_vid(self, score=50):
        the_list = []
        value_list = []
        sorted_list = []
        for _ in self.items:
            if _.part_type == 'VID':
                the_list.append(_)
                value_list.append(_.speed * _.maxram)
        return self._index_of_score(the_list, value_list, score)

    def pick_ram(self, score=50):
        the_list = []
        value_list = []
        for _ in self.items:
            if _.part_type == 'RAM':
                the_list.append(_)
                value_list.append(_.maxram)
        return self._index_of_score(the_list, value_list, score)

    def pick_ssd(self, score=50):
        the_list = []
        value_list = []
        for _ in self.items:
            if _.part_type == 'SSD':
                the_list.append(_)
                value_list.append(_.maxram)
        return self._index_of_score(the_list, value_list, score)


class ComputerConfig(DisplayMixin):

    def __init__(self, name='noName', *args):
        self.name = name
        self.items = list(args)
        should_have = ['MTB', 'VID', 'PRO', 'RAM', 'SSD']
        for item in list(args):
            if item.part_type in should_have:
                should_have.remove(item.part_type)
            else:
                raise ValueError('you should have one of each component')
        if should_have:
            raise ValueError('you are missing : ' + str(should_have))
        if len(args) < 5:
            raise ValueError('the computer is missing components')
        self.price = 0
        for _ in list(args):
            self.price += _.price


config_list = []


def log_configurator(fnc):
    def inner_func(name, config_parts, values):
        configure_computer = fnc(name, config_parts, values)
        config_list.append(configure_computer.name)
        return configure_computer

    return inner_func

# logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


# decorator
@log_configurator
def configure_computer(name, config_parts, values):
    start = time.time()
    proc = config_parts.pick_pro(values[0])
    mtbd = config_parts.pick_mtb(values[1])
    vide = config_parts.pick_vid(values[2])
    rams = config_parts.pick_ram(values[3])
    ssds = config_parts.pick_ssd(values[4])
    end = time.time()
    logger.info(f'configuration took {end - start} seconds')
    return ComputerConfig(name, proc, mtbd, vide, rams, ssds)


# context manager, decorator and generator
@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()

def save_to_txt(txt='no text entered'):
    with open_file('computer_history.txt') as f:
        f.write(txt)
