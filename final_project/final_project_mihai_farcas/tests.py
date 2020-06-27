import application
import unittest
from application import Order, Stock


class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nstart test")

    @classmethod
    def tearDownClass(cls):
        print("\nend test")

    def test_order_has_attr(self):
        order_date = "2020-05-05"
        client = " "
        address = "Stejarilor"
        order_details = {
            'KONICA 9000 MAG': 1,
            'KONICA 9000 YLL': 1,
            'KONICA 9000 CYA': 1,
            'KONICA 9000 BLK': 1
        }

        test_orders = application.Order(order_date, client, address, order_details)

        assert hasattr(test_orders, 'order_date'), 'Class Order is missing order_date attribute'
        assert hasattr(test_orders, 'client'), 'Class Order is missing client attribute'
        assert hasattr(test_orders, 'address'), 'Class Order is missing address attribute'
        assert hasattr(test_orders, 'order_details'), 'Class Order is missing order_details attribute'

    def test_check_order(self):
        cosma_2020_02_10 = Order(
            "2020-02-10", "Cosma", "Trandafirilor nr.1",
            {
                'HP 2500 BLK': 1,
                'HP 2500 MAG': 1,
                'HP 2500 CYA': 1,
                'HP 2500 YLL': 1,
                'HP 3002 YLL': 2,
                'KONICA 9000 MAG': 2
            }
        )
        print(cosma_2020_02_10)

        self.assertEqual(type(cosma_2020_02_10.order_details), dict)


class TestStock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nstart test")

    @classmethod
    def tearDownClass(cls):
        print("\nend test")

    def test_stock_init(self):
        stock = Stock()
        stock.append('KONICA 9000 MAG', 1)
        stock.append('HP 2500', 5)

        print(stock)
        assert isinstance(stock, Stock)
        print(stock.inks)
        self.assertEqual(type(stock.inks), dict)


if __name__ == '__main__':
    unittest.main(verbosity=2)
