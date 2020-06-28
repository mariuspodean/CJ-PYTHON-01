from final_project.final_project_turcu_alexandru import Player, zones, leave_or_stay
import unittest
import logging


class LoggerMixin:
    def logger(self):
        name = '.'.join([
            self.__module__,
            self.__class__.__name__
        ])
        return logging.getLogger(name)


class TestPlayerName(unittest.TestCase):

    def setUp(self):
        self.player1 = Player()

    @classmethod
    def StartTesting(cls) -> None:
        print('Started testing..')

    @classmethod
    def StopTesting(cls) -> None:
        print('Stopped testing..')

    def test_username_length(self):
        name = 'SomeVeryLongNameInsertedHere'
        result = self.player1.username_is_valid(name)
        self.assertFalse(result)

    def test_username_with_illegal_space(self):
        name = 'Name with Spaces'
        result = self.player1.username_is_valid(name)
        self.assertFalse(result)

    def test_username_with_no_uppercase(self):
        name = 'name'
        result = self.player1.username_is_valid(name)
        self.assertFalse(result)

    def test_username_valid(self):
        name = 'Alexandru'
        result = self.player1.username_is_valid(name)
        self.assertTrue(result)


class Testing(unittest.TestCase):
    def test_string(self):
        zones = 'same thing'
        zones.player1 = 'same thing'
        self.assertEqual(zones, zones.player1)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

class TestPlayerLevel(unittest.TestCase):
    def setUp(self):
        self.completion = 1
        self.level_up = 0.5

    def test_completion_sum(self):
        result = sum(self.completion, self.level_up)
        self.assertEqual(result, self.completion + self.level_up)


class TestZones(unittest.TestCase):
    def test_dictionary_attributes(self):
        self.assertHasAttr({zones}, 'Scenario')  # should succeed
        self.assertHasAttr({zones}, 'SomeRandomZoneName')  # should fail
        if not hasattr(obj, name):
            pass

    def assertHasAttr(self, param, param1):
        pass

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
