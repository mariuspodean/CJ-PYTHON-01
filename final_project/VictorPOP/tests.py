from FinalProject.application import PCpart
import unittest


class TestPCpart(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Let the testing begin!')

    @classmethod
    def tearDownClass(cls) -> None:
        print('The END')

    def test_part_list(self):
        pc_part = PCpart('AMD Ryzen™ 9 3900X', 'PRO', 4600, 70, 32, 4, 2, 2289)
        self.assertIsInstance(pc_part, PCpart)

    def test_pc_part(self):
        name = 'AMD Ryzen™ 9 3900X'
        part_type = 'PRO'
        speed = 4600
        ram = 70
        maxram = 32
        socket = 4
        m2 = 2
        price = 2289
        pc_part = PCpart(name, part_type, speed, ram, maxram, socket, m2, price)
        pc_part_attributes =['name', 'part_type', 'speed', 'ram', 'maxram', 'socket', 'm2', 'price']
        for _ in pc_part_attributes:
            assert hasattr(pc_part, _), 'PcPart is missing {_}'
