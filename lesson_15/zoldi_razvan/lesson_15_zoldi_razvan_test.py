import unittest
from lesson_15_zoldi_razvan import Country


class TestCountry(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("start test")

    @classmethod
    def tearDownClass(cls):
        print("end test")

    def test_country_init(self):
        name = 'Bulgaria'
        continent = 'Europe'
        position = 'Central Europe'
        area = '110994'

        test_country = Country(name, continent, position, area)

        assert hasattr(test_country, 'name'), 'Class Country is missing name attribute'
        assert hasattr(test_country, 'continent'), 'Class Country is missing continent attribute'

    def test_continent(self):
        name = 'Egypt'
        continent = 'Africa'
        position = 'Northern Africa'
        area = '1 million km2'

        test_continent = Country(name, continent, position, area)

        location = test_continent.continent_ver
        print(location())

        self.assertEqual(location(), 'Different continent')

    def test_continent_2(self):
        name = 'Romania'
        continent = 'Europe'
        position = 'Central Europe'
        area = '238400 km2'

        test_continent_2 = Country(name, continent, position, area)

        location2 = test_continent_2.continent_ver_2
        print(location2())

        self.assertNotEqual(location2(), 'Different continent')

    def test_continent_3(self):
        name = 'Austria'
        continent = 'Europe'
        position = 'Central Europe'
        area = '83879 km2'

        test_continent_3 = Country(name, continent, position, area)

        location3 = test_continent_3.continent_ver_3
        print(location3())

        self.assertTrue(location3())

    def test_continent_4(self):
        name = 'France'
        continent = 'Europe'
        position = 'Western Europe'
        area = '643801 km2'

        test_continent_4 = Country(name, continent, position, area)

        location4 = test_continent_4.continent_ver_3
        print(location4())
        # failure intention
        self.assertFalse(location4())


if __name__ == '__main__':
    unittest.main()
