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
        self.player1 = leave_or_stay.Player()

    @classmethod
    def StartTesting(cls) -> None:
        print('Started testing..')

    @classmethod
    def StopTesting(cls) -> None:
        print('Stopped testing..')

    def test_user_init(self):
        name = "Lorena"
        test_player = leave_or_stay.Player()
        assert hasattr(test_player, 'name'), 'Class does not have a name yet'
        assert hasattr(test_player, 'difficulty'), 'Class does not have a difficulty yet'

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


class TestPlayerLevel(unittest.TestCase):
    def setUp(self):
        self.completion = 1
        self.level_up = 0.5

    def test_completion_sum(self):
        result = sum(self.completion, self.level_up)
        self.assertEqual(result, self.completion + self.level_up)


if __name__ == '__main__':
    unittest.main()
