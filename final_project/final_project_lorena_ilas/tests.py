import application
import playground
import unittest


class TestUser(unittest.TestCase):
    def test_user_init(self):
        name = "Lorena"
        password = "abc123"
        user_type = "customer"

        test_user = application.User(name, password, user_type)

        assert hasattr(test_user, 'name'), 'Class Customer is missing name attribute'
        assert hasattr(test_user, 'password'), 'Class Customer is missing password attribute'
        assert hasattr(test_user, 'user_type'), 'Class Customer is missing user_type attribute'

    def test_parcel_init(self):
        length = 2
        height = 4
        weight = 6
        address = "Regele Ferdinand 22-26 Cluj"

        test_parcel = application.Parcel(length, height, weight, address)

        assert hasattr(test_parcel, 'length'), 'Class Parcel is missing name attribute'
        assert hasattr(test_parcel, 'height'), 'Class Customer is missing height attribute'
        assert hasattr(test_parcel, 'weight'), 'Class Customer is missing weight attribute'
        assert hasattr(test_parcel, 'address'), 'Class Customer is missing address attribute'

    def test_login_success(self):
        name = "Lorena"
        password = "abc123"

        test_login_ok = application.Login()

        self.assertTrue(test_login_ok.check(name, password), "Login successful")

    def test_login_failed(self):
        name = "lol"
        password = "bla"

        test_login_failed = application.Login()

        self.assertFalse(test_login_failed.check(name, password), "Login failed")

    @unittest.skip()
    def test_check_parcel(self):
        length = 2
        height = 4
        weight = 6
        address = "Regele Ferdinand 22-26 Cluj"

        test_check_parcel = application.Parcel(length, height, weight, address)

        self.assertFalse(test_check_parcel.check(), "Parcel Accepted")


if __name__ == '__main__':
    unittest.main()
