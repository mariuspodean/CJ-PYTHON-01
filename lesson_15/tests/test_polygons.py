import unittest

from lesson_15.mihai_farcas import polygons


def test_triangle():
    s1, s2, s3 = 3, 4, 5

    test_triangle = Triangle(s1, s2, s3)

    assert hasattr(test_triangle, 's1'), "dd"
    assert hasattr(test_triangle, s2), "doi"
    assert hasattr(test_triangle, s3), "trei"


test_triangle()
if __name__ == '__main__':
    unittest.main()