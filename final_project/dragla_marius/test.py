import unittest
from final_project.dragla_marius.playground import *
from collections.abc import MutableMapping, Sequence

class CollectionsTest(unittest.TestCase):

    def test_sequence(self):
        category_sales_instance = AllCategorySales(category_sales)
        self.assertIsInstance(category_sales_instance, Sequence)

    def test_mutable_mapping(self):
        self.assertIsInstance(sales, MutableMapping)


if __name__ == '__main__':
    unittest.main()



class SalesTest(unittest.TestCase):

    def test_get_total_category_sales(self):
        self.assertEquals(sum(category_sales.values()), 1331901.99)

    def test_get_customer_category_sales(self):
        self.assertEquals(sum(sales.customers[1]), 13900.39)



if __name__ == '__main__':
    unittest.main()

