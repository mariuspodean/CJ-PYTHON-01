from contextlib import ContextDecorator


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@singleton
class Player:
    def __init__(self):
        self.name = 'name'
        self.difficulty = 0
        self.location = "Scenario"
        self.completion = 0

    def __getitem__(self):
        return self.name

    def __len__(self):
        return len(self.location)

    def __repr__(self):
        return self.completion

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name

    def level_up(self):
        self.completion += 0.5


class LocationIterable:
    def __init__(self):
        self._locations = ['Scenario', 'Dark dungeon', 'Secret tunnel', 'Beach', 'Hello friend']

    def __getitem__(self, index):
        return self._locations[index]

    def __setitem__(self, location, index):
        self._locations[index] = location

    def __delitem__(self, index):
        self._locations.remove(index)

    def __len__(self):
        return len(self._locations)

    def __iter__(self):
        for elem in self._locations:
            yield elem

    def __repr__(self):
        return str(self._locations)

    def __str__(self):
        return str(self._locations)


class AsciiHeader(ContextDecorator):

    def __init__(self):
        self.line = '########################################################################################'

    def __enter__(self):
        print(self.line)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
