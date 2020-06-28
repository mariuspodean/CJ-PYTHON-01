from final_project.final_project_turcu_alexandru import Player, leave_or_stay
import unittest
import logging


class LoggerMixin:
    def logger(self):
        name = '.'.join([
            self.__module__,
            self.__class__.__name__
        ])
        return logging.getLogger(name)


class TestData(unittest.TestCase):

    @classmethod
    def StartTesting(cls) -> None:
        print('Started testing..')

    @classmethod
    def StopTesting(cls) -> None:
        print('Stopped testing..')

    def test_player(self):
        pass

    def test_game(self):
        pass


if __name__ == '__main__':
    unittest.main()
